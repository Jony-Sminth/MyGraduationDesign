def test(x):
    x += 1
    return (x,x)


x = 9
x,y = test(x)
print(x)
print(y)