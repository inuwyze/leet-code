stk=[]
inp=input()
l=0
r=0
for x in inp:
    print(stk)
    if x==')' or (x=='*' and l>r):
        r+=1
        if stk:
            stk.pop()
        else:

            break
    else:
        if x =='(':
            l+=1
        
        stk.append(x)

if stk.count(')') or stk.count('('):
    print(stk)
    print( False)
    
else:
    print(True)
