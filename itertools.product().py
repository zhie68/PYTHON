from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*product(a, b))



# sample input :
# 1 2
# 3 4

# sample output :
# (1, 3) (1, 4) (2, 3) (2, 4)
