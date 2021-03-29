def nombrepremier():
    nombre=0
    while nombre <= 100:
        if nombre % 3 == 0 and nombre % 5 != 0:
            print("Fizz")
            nombre+=1
        elif nombre % 5 == 0 and nombre % 3 != 0:
            print("Buzz")
            nombre+=1
        elif nombre % 3 == 0 and nombre % 5 == 0:
            print("FizzBuzz")
            nombre+=1
        else:
            print(nombre)
            nombre+=1

print(nombrepremier())        
            
            
       
    
    
    
    
    
    