def percent(marks,maxmarks):
    percentage = (marks/maxmarks)*100
    return percentage

def main():
    maxmarks = int(input("enter the maximum marks:"))
    assert maxmarks>=-100 and maxmarks<=500
    marks = int(input("enter the marks obntained:"))
    assert marks>=-100 and marks<=maxmarks
    result = percent(marks,maxmarks)
    print('percentage is:',result)
if __name__ == '__main__':
    main()
print('\n****End of the program****')
