for row in range (7):
    for column in range(5):
        if(((column==0 or column==4) and(row<2 or row>4))or((column==1 or column==3) and(row==2 or row==4) or(column==2 and row==3))):
            print("*",end="")
        else:
            print(end=" ")
    print( )
