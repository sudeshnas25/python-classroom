temperatures=[10,-20,-289,100]
def c_to_f(temperatures,filepath):
    with open(filepath, "w") as file:
        for c in temperatures:
            if c > -273.15:
                f=c*9/5+32
                file.write(str(f) + "\n")

c_to_f(temperatures,"temp.txt")
