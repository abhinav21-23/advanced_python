value=float(input("Enter the value of temperature :"))
temperature=(input("Temperatutre is in (celsius or fahrenite) :"))
if temperature=="celsius":
    print("Temperature in fahrentite is" ,((value/5)*9)+32 ,"F")
elif temperature=="fahrenite":
    print("Temperature in celsius is" ,((value-32)/9)*5,"C")
else :
    print("Invalid dimension")