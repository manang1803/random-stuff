import copy

def loadData(data):
    book = open('Assignment3-DataFile.txt')
    x = []
    for i in book:
        x.append(i.strip())

    y = []
    for i in x:
        y.append(i.split(','))

    dict_keys = ['Book ID:', 'Book Name:','Book Author:','Publication Year:','Publisher:','Copies:','Availability:']

    for j in range(len(dict_keys)):
        a = []
        for k in range(len(y)):
            a.append(y[k][j])
        data[dict_keys[j]] = a
    
    return data
        

def main():
    book_records = {}
    book_records = loadData(book_records)
    command = input("Command:")
    while command != 'Quit':
        if command == 'Print All':
            printRecords(book_records)
        elif command=='Print Available':
            printAvailable(book_records)
        elif command=='Insert':
            insertBook(book_records)
        elif command=='Remove':
            removeBook(book_records)
        elif command=='Update':
            updateBook(book_records)
        elif command=='Sort':
            sortBook(book_records)
        elif command=='Search':
            searchBook(book_records)
        else:
            print("Invalid Command, please input a valid one!")
            
        command=input("Command:")
        
    print("BYE")

def printRecords(file):
    print('ABC Bookshop')
    print("=======")
    for i in range(len(file['Book ID:'])):
        for key,val in file.items():
            print(key,val[i])
        print("-------")
    print("End of book information")

def printAvailable(file):
    print('ABC Bookshop')
    print("=======")
    for i in range(3):
        if file['Availability:'][i] == 'Available':
            for key,val in file.items():
                print(key,':',val[i])
            print("-------")
    print("End of book information")
    return file

def insertBook(file):
    dk = ['Book ID:', 'Book Name:','Book Author:','Publication Year:','Publisher:','Copies:','Availability:']
    for i in range(1,6):
        a = []
        a = file[dk[i]]
        z = input(dk[i])
        a.append(z)
        file[dk[i]] = a
    b = []
    b = file[dk[0]]
    b.sort(reverse = True)
    c = int(b[0])+1
    d = str(c)
    b.append(d)
    file[dk[0]] = b
    e = []
    e = file[dk[6]]
    e.append('Available')
    file[dk[6]] = e

    return file

def removeBook(file):
    dk = ['Book ID:', 'Book Name:','Book Author:','Publication Year:','Publisher:','Copies:','Availability:']
    x = input('ID:')
    #for key,val in file.items():
    if x in file['Book ID:']:
        index = file['Book ID:'].index(x)
        for i in range(len(dk)):
            del file[dk[i]][index]
        
    else:
        print('Please input a valid one')

    return file

def updateBook(file):
    dk = ['Book ID:', 'Book Name:','Book Author:','Publication Year:','Publisher:','Copies:','Availability:']
    while True:
        x = input('ID:')
        if x in file[dk[0]]:
            index = file[dk[0]].index(x)
            for i in range(1,7):
                a = input(dk[i])
                if a == 'NA':
                    pass
                else:
                    file[dk[i]][index] = a
            break
        else:
            print('Please input a valid one')

            
    return file

def sortBook(file):
    dk = ['Book ID:', 'Book Name:','Book Author:','Publication Year:','Publisher:','Copies:','Availability:']
    print('ABC Bookshop')
    print("=======")
    newFile = copy.deepcopy(file)
    y = len(file[dk[0]])
    z = file[dk[0]]
    
    for j in range(len(file[dk[0]])):
        x = newFile['Book ID:']
        x = list(map(int, x))
        a = max(x)
        k = x.index(a)
        #print(k)

        for i in dk:
            print(i,newFile[i][k])
            del newFile[i][k]
        print("-------")

def searchBook(file):
    dk = ['Book ID:', 'Book Name:','Book Author:','Publication Year:','Publisher:','Copies:','Availability:']
    a = input(dk[1])
    if a in file[dk[1]]:
        print('ABC Bookshop')
        print("=======")
        x = file[dk[1]].index(a)
        for i in range(len(dk)):
            print(dk[i],file[dk[i]][x])
        print("-------")
        print('End of book information')
    else:
        print('This book does not exist')
    
    
    
main() 
