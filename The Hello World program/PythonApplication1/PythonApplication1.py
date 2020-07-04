mystring = "Hello World"
myfloat = 10.0
myint = 20

if mystring == "Hello World":
    print("String: " + mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer:", myint)