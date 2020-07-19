inp=input()
stk=[]
star=[]
loop1=1
loop2=1
for i,x in enumerate(inp):
    if x==')':
        if stk:
            stk.pop()
        
        elif star:
            star.pop()
        else:
            loop1=0
            break
    elif x=='(':
        stk.append(i)
    else :
        star.append(i)

print(stk,star)
if loop1:
    if not stk:
        print(True)
    else:
        for x in stk:

            if star:
                while 1:
                    print(star[0])
                    if x<=star.pop(0):
                        break
            else:
                loop2=0
                break
        if loop2:
            print(True)
        else:
            print(False)
else:
    print(False)