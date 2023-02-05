def spy_game(list):
    spy_list=[]
    for x in range(len(list)):
        if list[x]==0 or list[x]==7:
            spy_list.append(list[x])
        else:
            continue
    if spy_list==[0,0,7]:
        return True
    else:
        return False
list=[4,0,1,5,7]
print(spy_game(list))