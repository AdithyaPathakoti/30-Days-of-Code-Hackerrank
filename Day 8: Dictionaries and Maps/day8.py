# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n=int(input())
pb={}
for i in range(n):
    a=input().strip()
    na,pn=a.split()
    pb[na]=pn

for j in sys.stdin:
    q=j.strip()
    if q in pb:
        print(f'{q}={pb[q]}')
    else:
        print('Not found')
