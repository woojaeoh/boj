from itertools import permutations

data=[]

for i in range(9):
  data.append(int(input()))

result=list(permutations(data,7))

data2=[]

for i in result:
  if(sum(i)==100):
      data2=list(i)
      break

data2.sort()
for i in data2:
  print(i)




      

