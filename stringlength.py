def string_length(mystring):
    if (type(mystring) == int):
        return "Sorry integers don't have length"
    else:
        return len(mystring)

length1 = input("Enter any string to count its length: ")
print(type(length1))
print(type(string_length(length1)))
print(string_length(length1))
