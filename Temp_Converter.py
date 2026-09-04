# Celsius → Fahrenheit: C × 9/5 + 32
# Fahrenheit → Celsius: (F - 32) × 5/9

def convert():
    choice = input("Which unit do you wanna convert to? (C/F): ")
    temp = int(input("Enter Temp to convert: "))

    if(choice == "F" or choice == "f"):
        temp = temp * 9/5 + 32
        print("The Temperature is: ",temp)
    elif(choice == "c" or choice == "C"):
        temp = (temp - 32) * 5/9
        print("The Temperature is: ", temp)
    else:
        print("Something Went Wrong")

convert()