for row in range (7):
    for column in range(7):
        if(column==0 or column==6) or(row==2 and column!=1 and column!=3 and column!=5)or(row==3 and column==3):
            print("*",end="")
        else:
            print(end=" ")
    print( )
