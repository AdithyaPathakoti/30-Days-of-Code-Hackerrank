# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
for n in range(a):
    s=input()
    for i in range (0,len(s),2):
        print(s[i],end='')
    print(end=' ')
    for j in range (1,len(s),2):
        print(s[j],end='')
    print(end='\n')
