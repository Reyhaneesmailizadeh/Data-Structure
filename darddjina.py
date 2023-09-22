def maximumNumber(list1, list2, nu):
    n, m = len(list1), len(list2)
    final = []
    def helper(list, c_length):
        answer = []
        lenn = len(list)
        for index, value in enumerate(list):
            while answer and answer[-1] < value and lenn-index > c_length-len(answer):
                answer.pop(-1) 
            if len(answer) < c_length:
                answer.append(value)
        return answer

    for ss in range(max(0, nu-m), min(nu, n)+1):
        pp1, pp2 = helper(list1, ss), helper(list2, nu-ss)
        final = max(final, [max(pp1, pp2).pop(0) for _ in range(nu)])
    return final



n = int(input())
list1 = [] 
list1 = input().split(" ")
list2= []
list2 = input().split(" ")
l = maximumNumber(list1, list2, n)
for ele in l:
    print(ele, end = " ")