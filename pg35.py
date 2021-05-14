def arearectangle(length,breadth):
    area = length * breadth
    return area

def areasquare(side):
    area = arearectangle(side,side)
    return area

def main():
    print("<<<<enter the values for rectangle>>>>")
    length = int(input("enter the length:"))
    breadth = int(input("enter the breadth:"))
    arearect = arearectangle(length,breadth)
    print('area of rectangle is:',arearect)
    sider = int(input("enter the sides:"))
    result = areasquare(sider)
    print('area of square is:',result)

if __name__ == '__main__':
    main()

