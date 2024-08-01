n,c=map(int,input().split())

data=[]
for _ in range(n):
  data.append(int(input()))

data.sort()

start=1
end=data[n-1]-data[0]


result=0 #결과

while(start<=end):
  maxgap=(start+end)//2
  value=data[0] #첫번째 요소부터 공유기를 설치하고 시작한다.
  count=1 #설치된 공유기의 수
  for i in range(1,n):
    if data[i]-value>=maxgap:
      value=data[i]
      count+=1
  if count>=c: #c개 이상의 공유기 설치가 가능한 경우
    start=maxgap+1
    result=maxgap
  else:
    end=maxgap-1
    
print(result)