print("_"*10,"PRIME_CHECK","_"*10)

user = input("Do you want to Start the Game(yes/no) : ")
if user == "yes" or user == "Yes" or user == "YES" or user == "YEs" or user == "YeS" or user == "yES":

    while True:
        u = int(input("Enter a Number here: "))
        
        if u ==1:
            print(u," is not 'Prime', not 'Composite' number.")
                
        elif u<=3:
            print(u, " is 'Prime' number.")   
                 
        elif u % 2 == 0 or u % 3 == 0:
            print(u, "is 'Composite' number.")
                
        else:
            print(u," is 'Prime' number.")
            
            
        user = input("Do you want to Stop ? (Yes/No): ")   
        if user == "yes" or user== "Yes" or user== "YES" or user== "YEs" or user== "yES" or user== "YeS":
            
            break  

else:
    print("Error !")        
print("_"*10,"THANK_YOU_","_"*10)


        
