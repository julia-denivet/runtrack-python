def Stock():
    i = 0 
    List = []
    while i < 4:
        x  =int(  input("veuillez renseigner un nombre entier"))
        List.append(x)
        i+=1
        List.sort()
        
    return List 

print(Stock())


    