N=input()
left=[]
right=[]

for i in range(len(N)//2):
  left.append(int(N[i]))
  
for i in range(len(N)//2,len(N)):
  right.append(int(N[i]))

sumleft=sum(left)
sumright=sum(right)

if sumleft==sumright:
  print("LUCKY")
else:
  print("READY")

