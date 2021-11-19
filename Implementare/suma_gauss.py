n = 10

def gaus(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

print(gaus(n))