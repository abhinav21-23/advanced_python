for row in range (7):
    for column in range(5):
        if(row==0 or column==2):
            print("*",end="")
        else:
            print(end=" ")
    print( )
