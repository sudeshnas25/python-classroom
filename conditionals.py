def age_func(age):
    new_age = float(age) + 50
    return new_age

age1 = input("enter your age: ")
if float(age1) < 50:
    print(age_func(age1))
elif float(age1) == 50:
    print(age_func(age1)+10)
else:
    print("Age cannot be greater than 50")
