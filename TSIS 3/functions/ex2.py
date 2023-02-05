def temp(F):
    C = (5 / 9) * (F-32)
    return C
F=input("temperature in F=")
print(temp(float(F)))