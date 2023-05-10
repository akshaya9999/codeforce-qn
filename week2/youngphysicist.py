n=int(input())
xsum=0
ysum=0
zsum=0
for i in range(n):
  a = list(map(int, input().strip().split()))
  xsum=xsum+a[0]
  ysum=ysum+a[1]
  zsum=zsum+a[2]

if xsum==ysum==zsum==0:
  print("YES")
else:
  print("NO")
