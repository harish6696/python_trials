def swap(c,d):
    global a,b
    temp=c
    c=d
    d=temp
    a=c
    b=d
a=8
b=9
swap(a,b)
print(str(a),str(b),sep=' & ')
