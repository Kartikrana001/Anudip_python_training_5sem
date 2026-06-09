angle1 =float(input("enter first angle"))
if(angle1 <=0):
    exit("angle must be positive")

angle2 =float(input("enter second angle"))
if(angle2 <=0):
    exit("angle must be positive")

angle3 =float(input("enter second angle"))
if(angle3 <=0):
    exit("angle must be positive")


if(angle1 + angle2 + angle3 ==180):
    print("Above angles form a triangle")
else:
    print("above angle do not form any triangle")
