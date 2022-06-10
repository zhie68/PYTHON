from itertools import permutations

word, num = input().split(" ")
permutations = list(permutations(word, int(num)))
permutations.sort()

for i in permutations:
    print("".join(i))





#sample input

HACK 3
#sample output

ACH
ACK
AHC
AHK
AKC
AKH
CAH
CAK
CHA
CHK
CKA
CKH
HAC
HAK
HCA
HCK
HKA
HKC
KAC
KAH
KCA
KCH
KHA
KHC
