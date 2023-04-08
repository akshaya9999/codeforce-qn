n,f = map(int, input().split())
x=[]
y=[]
for i in range (n):
  x,y=list(map(int , input().split()))
cf=0
for j in range(n):
  if int(x[j])<int(y[j]) and 2*int(x[j])>=int(y[j]):
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
