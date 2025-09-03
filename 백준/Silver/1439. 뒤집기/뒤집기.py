import sys

input = sys.stdin.readline

num = input()

k = num[0]
count = 0

for i in num:
    if i != k:
        count += 1
        k = i
        
print(count//2)