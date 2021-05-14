def traingle(side1,side2,side3):
    s =(side1+side2+side3)/2
    area = (s*(s-side1)*(s-side2)*(s-side3))**0.5
    print(area)

def main():
    side1 = float(input("enter the side 1:"))
    side2 = float(input("enter the side 2:"))
    side3 = float(input("enter the side 3"))
    assert side3 < side1+side2
    traingle(side1,side2,side3)
if __name__ == '__main__':
    main()
