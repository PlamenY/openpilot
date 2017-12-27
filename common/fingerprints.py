import os

_FINGERPRINTS = {
  "ACURA ILX 2016 ACURAWATCH PLUS": {
    1024L: 5, 513L: 5, 1027L: 5, 1029L: 8, 929L: 4, 1057L: 5, 777L: 8, 1034L: 5, 1036L: 8, 398L: 3, 399L: 7, 145L: 8, 660L: 8, 985L: 3, 923L: 2, 542L: 7, 773L: 7, 800L: 8, 432L: 7, 419L: 8, 420L: 8, 1030L: 5, 422L: 8, 808L: 8, 428L: 8, 304L: 8, 819L: 7, 821L: 5, 57L: 3, 316L: 8, 545L: 4, 464L: 8, 1108L: 8, 597L: 8, 342L: 6, 983L: 8, 344L: 8, 804L: 8, 1039L: 8, 476L: 4, 892L: 8, 490L: 8, 1064L: 7, 882L: 2, 884L: 7, 887L: 8, 888L: 8, 380L: 8, 1365L: 5,
    # sent messages
    0xe4: 5, 0x1fa: 8, 0x200: 3, 0x30c: 8, 0x33d: 5,
  },
  "HONDA CIVIC 2016 TOURING": {
    1024L: 5, 513L: 5, 1027L: 5, 1029L: 8, 777L: 8, 1036L: 8, 1039L: 8, 1424L: 5, 401L: 8, 148L: 8, 662L: 4, 985L: 3, 795L: 8, 773L: 7, 800L: 8, 545L: 6, 420L: 8, 806L: 8, 808L: 8, 1322L: 5, 427L: 3, 428L: 8, 304L: 8, 432L: 7, 57L: 3, 450L: 8, 929L: 8, 330L: 8, 1302L: 8, 464L: 8, 1361L: 5, 1108L: 8, 597L: 8, 470L: 2, 344L: 8, 804L: 8, 399L: 7, 476L: 7, 1633L: 8, 487L: 4, 892L: 8, 490L: 8, 493L: 5, 884L: 8, 891L: 8, 380L: 8, 1365L: 5,
    # sent messages
    0xe4: 5, 0x1fa: 8, 0x200: 3, 0x30c: 8, 0x33d: 5, 0x35e: 8, 0x39f: 8,
  },
  "HONDA CR-V 2016 TOURING": {
    57L: 3, 145L: 8, 316L: 8, 340L: 8, 342L: 6, 344L: 8, 380L: 8, 398L: 3, 399L: 6, 401L: 8, 420L: 8, 422L: 8, 426L: 8, 432L: 7, 464L: 8, 474L: 5, 476L: 4, 487L: 4, 490L: 8, 493L: 3, 507L: 1, 542L: 7, 545L: 4, 597L: 8, 660L: 8, 661L: 4, 773L: 7, 777L: 8, 800L: 8, 804L: 8, 808L: 8, 882L: 2, 884L: 7, 888L: 8, 891L: 8, 892L: 8, 923L: 2, 929L: 8, 983L: 8, 985L: 3, 1024L: 5, 1027L: 5, 1029L: 8, 1033L: 5, 1036L: 8, 1039L: 8, 1057L: 5, 1064L: 7, 1108L: 8, 1125L: 8, 1296L: 8, 1365L: 5, 1424L: 5, 1600L: 5, 1601L: 8,
    # sent messages
    0x194: 4, 0x1fa: 8, 0x30c: 8, 0x33d: 5,
  },
  "TOYOTA RAV4 2017": {
    36L: 8, 37L: 8, 170L: 8, 180L: 8, 186L: 4, 426L: 6, 452L: 8, 464L: 8, 466L: 8, 467L: 8, 547L: 8, 548L: 8, 552L: 4, 562L: 4, 608L: 8, 610L: 5, 643L: 7, 705L: 8, 725L: 2, 740L: 5, 800L: 8, 835L: 8, 836L: 8, 849L: 4, 869L: 7, 870L: 7, 871L: 2, 896L: 8, 897L: 8, 900L: 6, 902L: 6, 905L: 8, 911L: 8, 916L: 3, 918L: 7, 921L: 8, 933L: 8, 944L: 8, 945L: 8, 951L: 8, 955L: 4, 956L: 8, 979L: 2, 998L: 5, 999L: 7, 1000L: 8, 1001L: 8, 1008L: 2, 1014L: 8, 1017L: 8, 1041L: 8, 1042L: 8, 1043L: 8, 1044L: 8, 1056L: 8, 1059L: 1, 1114L: 8, 1161L: 8, 1162L: 8, 1163L: 8, 1176L: 8, 1177L: 8, 1178L: 8, 1179L: 8, 1180L: 8, 1181L: 8, 1190L: 8, 1191L: 8, 1192L: 8, 1196L: 8, 1227L: 8, 1228L: 8, 1235L: 8, 1237L: 8, 1263L: 8, 1279L: 8, 1408L: 8, 1409L: 8, 1410L: 8, 1552L: 8, 1553L: 8, 1554L: 8, 1555L: 8, 1556L: 8, 1557L: 8, 1561L: 8, 1562L: 8, 1568L: 8, 1569L: 8, 1570L: 8, 1571L: 8, 1572L: 8, 1584L: 8, 1589L: 8, 1592L: 8, 1593L: 8, 1595L: 8, 1596L: 8, 1597L: 8, 1600L: 8, 1656L: 8, 1664L: 8, 1728L: 8, 1745L: 8, 1779L: 8, 1904L: 8, 1912L: 8, 1990L: 8, 1998L: 8
  },
  "TOYOTA PRIUS 2017": {
    36L: 8, 37L: 8, 166L: 8, 170L: 8, 180L: 8, 295L: 8, 296L: 8, 426L: 6, 452L: 8, 466L: 8, 467L: 8, 550L: 8, 552L: 4, 560L: 7, 562L: 6, 581L: 5, 608L: 8, 610L: 8, 614L: 8, 643L: 7, 658L: 8, 713L: 8, 740L: 5, 742L: 8, 743L: 8, 800L: 8, 810L: 2, 814L: 8, 829L: 2, 830L: 7, 835L: 8, 836L: 8, 863L: 8, 869L: 7, 870L: 7, 871L: 2, 898L: 8, 900L: 6, 902L: 6, 905L: 8, 918L: 8, 921L: 8, 933L: 8, 944L: 8, 945L: 8, 950L: 8, 951L: 8, 953L: 8, 955L: 8, 956L: 8, 971L: 7, 975L: 5, 993L: 8, 998L: 5, 999L: 7, 1000L: 8, 1001L: 8, 1014L: 8, 1017L: 8, 1020L: 8, 1041L: 8, 1042L: 8, 1044L: 8, 1056L: 8, 1057L: 8, 1059L: 1, 1071L: 8, 1077L: 8, 1082L: 8, 1083L: 8, 1084L: 8, 1085L: 8, 1086L: 8, 1114L: 8, 1132L: 8, 1161L: 8, 1162L: 8, 1163L: 8, 1175L: 8, 1227L: 8, 1228L: 8, 1235L: 8, 1237L: 8, 1279L: 8, 1552L: 8, 1553L: 8, 1556L: 8, 1557L: 8, 1568L: 8, 1570L: 8, 1571L: 8, 1572L: 8, 1595L: 8, 1777L: 8, 1779L: 8, 1904L: 8, 1912L: 8, 1990L: 8, 1998L: 8
  },
  "CHEVROLET VOLT 2017 PREMIER": {
    0xa1L: 7, 0x106L: 5, 0x300: 8, 0x302L: 2, 0x303L: 2, 0x310L: 2, 0x308L: 7, 0x306L: 8, 0x510L: 7, 0x512L: 8, 0x511L: 8, 0x513L: 8, 0x514L: 8, 0x515L: 8, 0x516L: 8, 0x517L: 8, 0x518L: 8, 0x519L: 8, 0x51aL: 8, 0x51bL: 8, 0x51cL: 8, 0x51dL: 8, 0x51eL: 8, 0x51fL: 8, 0x521L: 7, 0x522L: 7, 0x523L: 7, 0x524L: 7, 0x525L: 7, 0x526L: 7, 0x527L: 7, 0x528L: 7, 0x529L: 7, 0x475L: 8, 0x476L: 8, 0x477L: 8, 0x47aL: 8, 0x47bL: 8, 0x47cL: 8, 0x47dL: 8, 0x47eL: 8, 0x47fL: 8, 0x530L: 8, 0x533L: 8, 0x537L: 8, 0x52aL: 7, 0x52bL: 7, 0x52cL: 7, 0x52dL: 7, 0x52eL: 7, 0x52fL: 7, 0x460L: 8, 0x461L: 8, 0x462L: 8, 0x463L: 8, 0x464L: 8, 0x465L: 8, 0x466L: 8, 0x467L: 8, 0x468L: 8, 0x469L: 8, 0x46aL: 8, 0x46bL: 8, 0x46cL: 8, 0x46dL: 8, 0x46eL: 8, 0x46fL: 8, 0x470L: 8, 0x471L: 8, 0x472L: 8, 0x473L: 8, 0x474L: 8, 0x552L: 8, 0x580L: 8, 0x582L: 6, 0x584L: 8, 0x585L: 5, 0x581L: 8, 0x586L: 7, 0x53aL: 8, 0x540L: 8, 0x741L: 8, 0x743L: 8, 0x780L: 7, 0x135L: 1, 0x409L: 7, 0x40aL: 7, 0x420L: 6, 0x421L: 8, 0x422L: 8, 0x423L: 8, 0x424L: 8, 0x425L: 8, 0x426L: 8, 0x427L: 8, 0x428L: 8, 0x429L: 8, 0x42aL: 8, 0x42bL: 8, 0x42cL: 8, 0x440L: 8, 0x441L: 8, 0x442L: 8, 0x443L: 8, 0x444L: 8, 0x445L: 8, 0x446L: 8, 0x447L: 8, 0x448L: 8, 0x449L: 8, 0x44aL: 8, 0x44bL: 8, 0x44cL: 8, 0x350L: 8, 0x351L: 8, 0x352L: 8, 0x353L: 8, 0x354L: 8, 0x355L: 8, 0x356L: 3,

    # Forwarded from powertrain
    0xbdL: 7, 0xbeL: 6, 0xf1L: 6, 0x135L: 8, 0x184L: 8, 0x1e5L: 8, 0x348L: 5, 0x34aL: 5
  },
}

# support additional internal only fingerprints
try:
  from common.fingerprints_internal import add_additional_fingerprints
  add_additional_fingerprints(_FINGERPRINTS)
except ImportError:
  pass

def eliminate_incompatible_cars(msg, candidate_cars):
  """Removes cars that could not have sent msg.

     Inputs:
      msg: A cereal/log CanData message from the car.
      candidate_cars: A list of cars to consider.

     Returns:
      A list containing the subset of candidate_cars that could have sent msg.
  """
  compatible_cars = []
  for car_name in candidate_cars:
    adr = msg.address
    if msg.src != 0 or (adr in _FINGERPRINTS[car_name] and
                        _FINGERPRINTS[car_name][adr] == len(msg.dat)):
      compatible_cars.append(car_name)
    else:
      pass
      #isin = adr in _FINGERPRINTS[car_name]
      #print "eliminate", car_name, hex(adr), isin, len(msg.dat), msg.dat.encode("hex")
  return compatible_cars

def all_known_cars():
  """Returns a list of all known car strings."""
  return _FINGERPRINTS.keys()

