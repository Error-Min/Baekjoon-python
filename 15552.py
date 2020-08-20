from sys import stdin
n = int(stdin.readline())

for i in range(0, n):
    b,c = list(map(int, stdin.readline().split()))
    print(b + c)
