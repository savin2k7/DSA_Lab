def search(emp):
    i=int(input('Enter employee ID: '))
    for n in range(len(emp)):
        if emp[n]==i:
            print('employee found at index:',n)
            break
    else:
        print('no such id exist')
emp=[101,102,103,104,105,106,107,108,109]
search(emp)