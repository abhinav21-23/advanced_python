for row in range (7):
    for column in range(5):
        if(column==0 or row==6):
            print("*",end="")
        else:
            print(end=" ")
    print( )
