data=input().split('-')

a=[] #앞에 -가 있는 값들을 다더해서 대입하는 리스트

for i in data:
    sum=0
    for j in i.split('+'):
      sum+=int(j)
    a.append(sum) #'-'를 기준으로 나뉜 데이터들중
                  #'+'값으로 엮여있는경우 다 더한다.(min값을 만들기 위해 괄호 처리)
result=a[0]
for i in range(1,len(a)):
  result-=a[i]

print(result)
  
  
  
