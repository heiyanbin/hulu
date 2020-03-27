#!/usr/bin/env python

ans = []
def newNumByRemove(num, i, k):
    if k == 0: return
    x = '0'
    index = -1
    for j in range(len(num) - k, i - 1, -1):
        if num[j] >= x:
            index = j
            x = num[j]
            
    ans.append(x) 
    newNumByRemove(num, index + 1, k - 1)

a = input('input a number:\n')
newNumByRemove(a, 0, 4)
print(''.join(ans))


