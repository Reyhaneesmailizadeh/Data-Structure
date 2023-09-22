MAX = 500001
parentt = [0] * MAX
Ranking = [0] * MAX
def findit(x):  
    if parentt[x] == x:
        return x
    else:
        return findit(parentt[x])


def mergge(r1, r2):
    if(r1 != r2):
        if(Ranking[r1] > Ranking[r2]):
            parentt[r2] = r1
            Ranking[r1] += Ranking[r2]
        else:
            parentt[r1] = r2
            Ranking[r2] += Ranking[r1]


def minimumOperationns(s1, s2):
    for i in range(1, 26 + 1):
        parentt[i] = i
        Ranking[i] = 1
    anss = []
    for i in range(len(s1)):
        if(s1[i] != s2[i]):
            if(findit(ord(s1[i]) - 96) !=
               findit(ord(s2[i]) - 96)):
                x = findit(ord(s1[i]) - 96)
                y = findit(ord(s2[i]) - 96)
                mergge(x, y)
                anss.append([s1[i], s2[i]])
    print(len(anss))


if __name__ == '__main__':
    s11 = input()
    s22 = input()
    minimumOperationns(s11, s22)