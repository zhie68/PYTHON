from itertools import combinations
word, num = input().split(" ")
for i in range(1, int(num)+1):
    for j in combinations(sorted(word), i):
        print (''.join(j))
        
        
#Sample Input

HACK 2

#Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK
