def fun1():
    for i in range(2,101):
        j=2
        for j in range(2,i):
            if i%j==0:
                break
        else:
            yield i

for i in fun1():
    print(i)
