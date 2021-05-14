def arearectangle(length,breadth=4):
    area = length*breadth
    return area
def main():
    length = int(input("enter the length:"))
    area = arearectangle(length)
    print(area)
if __name__ == '__main__':
    main()
print('\n>>>>>End of the program<<<<<')
