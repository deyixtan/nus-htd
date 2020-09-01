from nus_htd import NUSHTD

if __name__ == "__main__":
    nus_htd = NUSHTD("nusstu\\E1234567", "XXXXXXXX")
    result, msg = nus_htd.declare("36.5")
    print(msg)
