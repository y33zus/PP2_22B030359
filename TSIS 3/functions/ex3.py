def solve(numheads,numlegs):
    #C+R=numheads
    #2*C + 4*R = numlegs
    #C+2*R=numlegs/2
    R=numlegs/2-numheads
    C=numheads-R
    solution = "number of rabbits is {} number of chikkens is {}".format(R,C)
    return solution
numheads=input("number of heads")
numlegs=input("number of legs")
print(solve(float(numheads),float(numlegs)))