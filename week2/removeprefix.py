t=int(input())
for i in range(t):
    n=int(input())
    a = list(map(int, input().strip().split()))
    x=0
    for c in range(n):
      if(len(set(a)) != len(a)):
        a.pop(0)
        x=x+1
    print(x)