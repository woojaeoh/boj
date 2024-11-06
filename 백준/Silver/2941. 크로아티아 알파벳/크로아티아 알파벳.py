import sys

croatia=["c=","c-","dz=","d-","lj","s=","nj","z="]
s= sys.stdin.readline().strip()


for c in croatia:
    s=s.replace(c,'*')
    
print(len(s))
