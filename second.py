def cislo_text(cislo):
    itky = str(cislo)
    if int(cislo)<=100:
        desitky = ["","","dvacet","třicet","čtyřicet","padesát","šedesát", "sedmdesát","osmdesát","devadesát"]
        jednotky = ["", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "děvět"]

        if len(itky)==3:
            if (itky[0]=="1" and itky[1]=="0" and itky[2]=="0"):
                cislo_cislo = "sto"

        if len(itky)==2:
            if itky[0] == "1":
                teens = ["deset", "jedenáct","dvanáct","třináct","čtrnáct", "patnáct", "šestnáct","sedmnáct", "osmnáct","devatenáct"]
                cislo_cislo = teens[int(itky[1])]
            else:
                cislo_cislo = desitky[int(itky[0])]+ " " + jednotky[int(itky[1])]
        if len(itky)==1:
            jednotky[0] = "nula"
            cislo_cislo = jednotky[int(itky[0])]
    else:
        cislo_cislo = "Větší než sto"
    return cislo_cislo


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
  
