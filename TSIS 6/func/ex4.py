def all_true(my_tuple):
    return all(my_tuple)
tuple1 = (True, True, True,True,True)
tuple2 = (True, False, True,False,False)
print(all_true(tuple1),all_true(tuple2))