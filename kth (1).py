list = []
list = input().split(' ')
n = int(list[0])
m = int(list[1])
q = int(list[2])


matrix = [([0] * n) for i in range(m)]

for i in range(q):
    locate = []
    locate = input().split(' ')
    i = int(locate[0])
    j = int(locate[1])
    matrix[m - j][i - 1] = 1
    
    b = 0
    z = 0
    for u in range(1,m+1,1):
        count = 0
        for e in range(1,n+1,1):
            nn = matrix[m - u][e - 1]
            if nn == 1:
                count += 1
                if count == n or e == n:
                    b +=1
                    count = 0
            else:
                if count != 0:
                    b += 1
                count = 0

    
    for e in range(1,n+1):
        count = 0
        for u in range(1,m+1):
            nn = matrix[m - u][e - 1]
            if nn == 1:
                count += 1
                if count == m or u == m:
                    z += 1
                    count = 0

            else:
                if count != 0:
                    z += 1
                count = 0
    print(b + z)
    