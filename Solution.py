import numpy

matrix = []

n = input()
n = int(n.split(" ")[0])

for y in range(n):
    inp = input()
    inp = inp.split(" ")
    temp = []
    for x in range(len(inp)):
        inp[x] = int(inp[x])
        temp.append(inp[x])
    matrix.append(temp)

min =  numpy.min(matrix, axis = 1)
max = numpy.max(min)
print(max)
    


