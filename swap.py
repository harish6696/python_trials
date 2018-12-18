def swap(c,d):
    global a,b
    temp=c
    c=d
    d=temp
    a=c
    b=d
a=1
b=2
swap(a,b)
print(str(a),str(b),sep=' & ')