records = str(input())
K, A, S = records.split(' ')
if K > A and K > S:
    print(K)
elif A > K and A > S:
    print(A)
else:
    print(S)