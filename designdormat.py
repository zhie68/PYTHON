N, M = map(int, input().split(" "))
a = ".|."
for i in range(N):
    if i < (N-1)/2:
        print((a * (2*i+1)).center(M, "-"))
    elif i == (N-1)/2:
        print("WELCOME".center(M, "-"))
    else:
        print((a * (2*(N-1-i)+1)).center(M, "-"))
