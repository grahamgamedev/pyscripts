def sub(x, y):
    ans = x + int("-" + str(y))
    return(ans)

def mul(x, y):
    ans = 0
    for i in range(y):
        ans += x
    return(ans)

def div(x, y, places=2):
    ans = str(divmod_(x, y)[0]) + "."
    for i in range(places):
        x = int(str(divmod_(x, y)[1]) + "0")
        ans += str(divmod_(x, y)[0])
    return(ans)

def divmod_(x, y):
    count = 0
    while x >= y:
        x = sub(x, y)
        count += 1
    return(count, x)

def pow(x, y):
    ans = x
    for i in range(y-1):
        ans = mul(ans, x)
    return(ans)

print(div(7, 2))
