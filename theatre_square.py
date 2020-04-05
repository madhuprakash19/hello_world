l=int(input())
b=int(input())
a=int(input())
if (l%a)==0:
    x=int(l/a)
else:
   x=int(l/a)+1
if (b%a)==0:
    y=int(b/a)
else:
    y=int(b/a)+1
ans=x*y
print(ans)    
    
