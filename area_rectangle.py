def arearectangle(length,breadth):
    area = length * breadth
    return area
def main():
    print("<<<<enter the values for rectangle>>>>")
    length = int(input("enter the length:"))
    breadth = int(input("enter the breadth:"))
    arearect = arearectangle(length,breadth)
    print('area of rectangle is:',arearect)
if __name__ == '__main__':
    main()
print('\n>>>>End of the Program<<<<')
