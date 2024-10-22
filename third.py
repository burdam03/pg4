def je_prvocislo(cislo):
    if cislo <= 1:
        return False
    if cislo == 2:
        return True
    else:
        for i in range(2, cislo):
            if (cislo % i ==0 and i!=cislo):
                return False
            else:
                if i== cislo-1:
                    return True
                else:
                    i+=1



def vrat_prvocisla(maximum):
    maximum1=int(maximum)
    maximum2=[]
    for i in range (1, maximum1+1):
        if je_prvocislo(i)==True:
            maximum2.append(i)
        i+=1
    return maximum2