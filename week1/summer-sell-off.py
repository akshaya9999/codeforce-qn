n,f = map(int, input().split())
x=[]
y=[]
for i in range (n):
  a,b=(map(int , input().split()))
  x.append(a)
  y.append(b)
cf=0
for j in range(n):
  if x[j]<y[j] and 2*x[j]>=y[j]:
    x[j]=2*x[j]
    cf+=1
    if cf==f:
      break
final=0
for k in range(n):
  if y[k]<=x[k]:
    final+=y[k]
  else:
    final+=x[k]
print(final)

  

