def draw_rectangle(width, height):
    
    i=0 

    while i <= width:
        print("","-", end="") 
        i+=1
    
    

    a = 0
    d = 0

    print("\n","")


    while a < height:
        d = 0
        while d <= width :
            if d == 0 :
                print("|","",end="")
            elif d == width :
                print("|\n")
            else :
                print(" ","", end="")
            d = d + 1
        a+=1


    

    c = 0
    while c <= width:
        print("","-", end="") 
        c+=1

 

   

print(draw_rectangle(10, 3))



        






