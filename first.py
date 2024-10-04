#program který rozezná sudé a liché číslo
def sudy_nebo_lichy(x):
    if x % 2 == 0:
        print("číslo je",x,"sudé")
    else:
        print("číslo je",x,"liché")

sudy_nebo_lichy(5)

sudy_nebo_lichy(1000000)
        


