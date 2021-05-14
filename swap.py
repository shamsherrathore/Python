def test(a, b):
    a = a+b
    b = a-b
    a = a-b
    print('a = ', a)
    print('b = ', b)

def func():
    pass
a = func()
print(a)

def main():
    func()
    test(5,8)

if __name__ == '__main__':
    main()
