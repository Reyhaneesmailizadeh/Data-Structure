

def count(list, word):
    n = len(list)
    count = 0
    for i in range(n):
        if list[i][0] == word:
            count = count + 1
    if count >= 5:
        return True
    return False


def drive(list):
    n = len(list)
    for i in range(n):
        str = list[i]
        list[i]=str[0]
    list1=[]
    for k in range(n):
        if list[k] not in list1:
            list1.append(list[k])
    return list1


list=[]
n = int(input())
for i in range(n):
    sound = input()
    sound.lower()
    list.append(sound)
listt = []
listt  = drive(list)
m = len(listt)
lo5=[]
for j in range(m):
    a = listt[j]
    if(count(list, a)):
        lo5.append(a)
j = len(lo5)
lo5.sort()
for e in range(j):
    print(lo5[e], end='')

if j==0:
    print("How long must I suffer")



