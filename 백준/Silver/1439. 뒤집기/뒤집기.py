s = input()
count0 = 0  #연속적인 0을 셀 변수 (전부 1로 바꾸는 경우)
count1 = 0  #연속적인 1을 셀 변수 (전부 0으로 바꾸는 경우)

if s[0] == '0':  # 첫 번째 정수에 대한 카운트 진행
  count0 += 1
else:  # 첫 번째 정수에 대한 카운트 진행
  count1 += 1

for i in range(len(s) - 1):
  if s[i] != s[i + 1]:
    # 다음 수에서 1로 바뀌는 경우
    if s[i + 1] == '1':
      count1 += 1
    else:  #다음수에서 0으로 바뀌는 경우
      count0 += 1

print(min(count0, count1))
