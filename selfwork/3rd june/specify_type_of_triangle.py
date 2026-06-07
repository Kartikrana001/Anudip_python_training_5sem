angle_1=float(input("Enter angle one: "))
angle_2=float(input("Enter angle two: "))
angle_3=float(input("Enter angle three: "))
if((angle_1 <= 0 or angle_2 <= 0 or angle_3 <= 0 or (angle_1 + angle_2 + angle_3) != 180)):
    print("invelid input..")
else:
    if angle_1 == 60 and angle_2 == 60 and angle_3 == 60:
        print("Equilateral Triangle")
    elif angle_1 == angle_2 or angle_2 == angle_3 or angle_1 == angle_3:
        print("Isosceles Triangle")
    elif angle_1 == 90 or angle_2 == 90 or angle_3 == 90:
        print("Right-Angled Triangle")
    elif angle_1 < 90 and angle_2 < 90 and angle_3 < 90:
        print("Acute-Angled Triangle")
    elif angle_1 > 90 or angle_2 > 90 or angle_3 > 90:
        print("Obtuse-Angled Triangle")
    else:
        print("Scalene Triangle")
