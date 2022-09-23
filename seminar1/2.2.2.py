a = int(input("Input quarter number:"))

if a == 1:
    print("xcoord > 0 and ycoord > 0")
elif a == 2:
    print("xcoord < 0 and ycoord > 0")
elif a == 3:
    print("xcoord < 0 and ycoord < 0")
elif a == 4:
    print("xcoord > 0 and ycoord < 0")
else:
    print("Wrong quarter")
