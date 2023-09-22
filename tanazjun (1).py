
#find prime numbers lower than 13*b
def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []
    for i in range(2, limitn):
        if i in not_prime:
            continue
        for f in range(i*2, limitn, i):
            not_prime.add(f)
        primes.append(i)
    return primes

def shift(list, shft=0):
    a = shft % len(list)
    return list[-a:] + list[:-a]


#get input from user
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

#make list of prime numbers
list1 = primes_sieve(12*b)

#make list for the circle of numbers
list=[]
m = a
while m > 0:
    list.append(m)
    m = m - 1
#do the game and update the list to the latest one
for j in range(b):
    i = list1[j]
    m = list[a - 1]
    list.remove(list[a - 1])
    list=shift(list, int(i / a))
    list.insert(((a - 1) - i % (a)), m)

#print c and its neighbor numbers
for t in range(a):
    if list[t] == c:
        if (t == 0):
            print(list[a-1], end =" ")
            print(list[1], end =" ")

        elif (t == a-1):
            print(list[a-2], end =" ")
            print(list[0], end =" ")

        else:
            print(list[t - 1], end =" ")
            print(list[t + 1], end =" ")

