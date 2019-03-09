temperatures=[10,-20,-289,100]
def temp(celsius):
    if float(celsius) < -273.15:
        return "It's not possible"
    else:
        fahrenheit = (float(celsius)* 9/5) + 32
        return fahrenheit
for t in temperatures:
    print(temp(t))
