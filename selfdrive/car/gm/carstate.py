import common.numpy_fast as np

import selfdrive.messaging as messaging
from common.realtime import sec_since_boot
from selfdrive.config import Conversions as CV

from selfdrive.car.gm.can_parser import CANParser

# Car button codes
class CruiseButtons:
  UNPRESS     = 2
  RES_ACCEL   = 4
  DECEL_SET   = 6
  CANCEL      = 12
  MAIN        = 10

def get_powertrain_can_parser():
  # this function generates lists for signal, messages and initial values
  dbc_f = 'gm_global_a_powertrain.dbc'
  signals = [
    ("SteeringWheelAngle", 485, 0),
    ("FLWheelSpd", 840, 0),
    ("FRWheelSpd", 840, 0),
    ("RLWheelSpd", 842, 0),
    ("RRWheelSpd", 842, 0),
    ("BrakePedalPosition", 241, 0),
    ("RegenPaddle", 189, 0),
    ("AcceleratorPos", 190, 0),
    ("PRNDL", 309, 0),
    ("LKADriverAppldTrq", 388, 0),
    ("LKATorqueDeliveredStatus", 388, 0)
  ]

  return CANParser(dbc_f, signals)

def get_lowspeed_can_parser():
  # this function generates lists for signal, messages and initial values
  dbc_f = 'gm_global_a_lowspeed.dbc'
  signals = [
    ("CruiseButtons", 276135936, 2),
    ("LKAGapButton", 276127744, 0),
    ("GasPedal", 271360000, 0)
  ]

  return CANParser(dbc_f, signals)

class CarState(object):
  def __init__(self, CP, logcan):
    if CP.carFingerprint != "CHEVROLET VOLT 2017 PREMIER":
      raise ValueError("unsupported car %s" % CP.carFingerprint)

    self.brake_only = CP.enableCruise

    # initialize can parsers
    self.powertrain_cp = get_powertrain_can_parser()
    self.lowspeed_cp = get_lowspeed_can_parser()

    self.car_gas = 0

    self.v_wheel = 0.0

    self.cruise_buttons = CruiseButtons.UNPRESS
    self.lkas_gap_buttons = 0

    # TODO:
    self.left_blinker_on = False
    self.prev_left_blinker_on = False
    self.right_blinker_on = False
    self.prev_right_blinker_on = False

  def update(self, can_powertrain, can_lowspeed):
    powertrain_cp = self.powertrain_cp
    powertrain_cp.update_can(can_powertrain)
    lowspeed_cp = self.lowspeed_cp
    lowspeed_cp.update_can(can_lowspeed)

    self.can_valid = powertrain_cp.can_valid
    self.prev_cruise_buttons = self.cruise_buttons
    self.cruise_buttons = lowspeed_cp.vl[276135936]['CruiseButtons']
    self.lkas_gap_buttons = lowspeed_cp.vl[276127744]['LKAGapButton']

    # calc best v_ego estimate, by averaging two opposite corners
    speed_estimate = (
      powertrain_cp.vl[840]['FLWheelSpd'] + powertrain_cp.vl[840]['FRWheelSpd'] +
      powertrain_cp.vl[842]['RLWheelSpd'] + powertrain_cp.vl[842]['RRWheelSpd']) / 4.0

    self.v_ego = self.v_wheel = speed_estimate / CV.MS_TO_KPH

    self.angle_steers = powertrain_cp.vl[485]['SteeringWheelAngle']
    self.gear_shifter = powertrain_cp.vl[309]['PRNDL']

    self.user_brake = powertrain_cp.vl[241]['BrakePedalPosition']
    # Brake pedal's potentiometer returns near-zero reading
    # even when pedal is not pressed
    self.brake_pressed = self.user_brake > 5

    self.regen_pressed = powertrain_cp.vl[189]['RegenPaddle']
    # Regen braking is braking
    self.brake_pressed = self.brake_pressed or self.regen_pressed

    self.pedal_gas = lowspeed_cp.vl[271360000]['GasPedal']
    self.user_gas = self.pedal_gas
    self.user_gas_pressed = self.user_gas > 0

    self.steer_override = abs(powertrain_cp.vl[388]['LKADriverAppldTrq']) > 3.0

    # 3 - failed, 2 - temporary limited
    self.steer_not_allowed = powertrain_cp.vl[388]['LKATorqueDeliveredStatus'] >= 2

    # TODO:
    self.door_all_closed = True
    self.seatbelt = True
    self.steer_error = False

    self.brake_error = False
    self.esp_disabled = False
    self.main_on = True
    self.can_valid = True

    # Alow Park (0) and D/L (2)
    self.gear_shifter_valid = self.gear_shifter in [0, 2]

