def Puissance(x,n) :
    if n==0 :
        return 1
    else :
        return x*Puissance(x,n-1)

x = int(input("Veuillez renseigner un nombre"))
n = int(input("Veuillez renseigner une puissance"))       

print(Puissance(x,n))
