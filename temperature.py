def temp(celsius):

    if float(celsius) < -273.15:
        return "It's not possible"
    else:
        fahrenheit = (float(celsius)* 9/5) + 32
        return fahrenheit

celsius1 = input("Enter temperature in celsius: ")
print(temp(celsius1))
