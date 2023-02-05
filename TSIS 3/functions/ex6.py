def has_33(numbers):
    for x in range(len(numbers)):
        if numbers[x] == 3 and numbers[x+1]==3:
            return True
        else:
            continue
    else:
        return False
list=[0,4,5,3,4,4,5]
print(has_33(list))