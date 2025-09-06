import sys

input = sys.stdin.readline

n= int(input())

count =0
end =0
while True:
    end += 1
    if "666" in str(end):
        count += 1
    
    if count ==n:
        print(str(end))
        break
        
    