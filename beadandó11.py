# import timeit
# start = timeit.default_timer()

def feladat():
    max = 0
    szam1 = 0
    szam2 = 0
    for i in range(100,1000):
        for j in range(100,1000):
            x = i*j
            if str(x)==str(x)[::-1]:
                if x>max:
                    max = x
                    szam1 = i
                    szam2 = j
    return '{0} * {1} = {2}'.format(szam1,szam2,max)
print(feladat())

# stop = timeit.default_timer()
# print(stop - start)
