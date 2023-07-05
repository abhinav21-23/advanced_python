i=1
j=5
for row in range (7):
    for column in range(7):
        if(row==0 or row==6):
            print("*",end="")
        elif(row==i and column==j):
            i=i+1
            j=j-1
            print("*",end="")      
        else:
            print(end=" ")
    print( )
