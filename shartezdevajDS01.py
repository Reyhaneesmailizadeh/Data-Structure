
def GCD(x , y):
    if y == 0:
        return x
    r = int(x % y)
    return GCD(y , r)


b, n = [int(b) for b in input().split()]
l = b%n
if l!=0:
    lnc = n - GCD(l, n)
else:
    lnc = n - GCD(b, n)
lnc=int(lnc)

print(lnc)