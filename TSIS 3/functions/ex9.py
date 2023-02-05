def unique(list):
    uni_list=[]
    for x in range(len(list)):
        if list[x] not in uni_list:
            uni_list.append(list[x])
    return uni_list
list=[1,1,1,1,1,2,2,2,2,23,3,3,3,3,3,4,4,4,4,5,5,5,5,5]
print(unique(list))