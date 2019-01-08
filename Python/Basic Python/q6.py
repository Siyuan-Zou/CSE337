#part1
cube = lambda x: x**3
narcissistic = lambda x: True if cube(int(x[0])) + cube(int(x[1])) + cube(int(x[2])) == int(x) else False
narc = list()
for i in range(100, 1000):
    x = str(i)
    if narcissistic(x):
        narc.append(i)

print(narc)

#part2
lst = [1, 4, 20]
a = list(map(lambda x:2**x, lst))
print(a)
b = list(filter(lambda x:x<1000, a))
print(b)

#part3
def part2():
    lst2 = ["word1", "word2", "word3"]

    def funcPos(lst, value):
        return lst.index(value)+1
    countlst = list(map(lambda x:funcPos(lst2,x), lst2))
    def createTuples(lst2, x):
        tup = (lst2[x - 1], x)
        return tup
    tupleList = list(map(lambda x:createTuples(lst2, x), countlst))
    print(tupleList)
    return tupleList