import re

directory = {
    'Gurcharan Singh':['1234567890'],
    'Naveen Bassi': ['234654'],
    'Ankit Billa' : ['12343456','2345634567765']
}

def multipleEntry(key):
    tempList = directory[key]
    index = 1
    for element in tempList:
        print(index, ".", key + ':', element)
        index += 1
    
    choice = int(input('Your selection: '))
    # print(directory[key][choice-1])
    return directory[key][choice-1]

def addEntry(key, val):
        if(key in directory.keys()):
            directory[key].append(val)
        else:
             directory[key] = [val]

def searchEntry(key):
    tempDir = {}
    str = '[a-zA-Z]*'+key+'[a-zA-Z]*'
    search = re.compile(str, re.IGNORECASE)

    for entry in directory:
        if search.findall(entry):
            tempDir[entry] = directory[entry]
    
    return tempDir

def deleteEntry(key):
    if key.lower() not in directory.keys():
        return None
    if len(directory[key])> 1:
        val = multipleEntry(key)
        directory[key].remove(val)
    else:
        del directory[key]

def updateEntry(key,newVal):
    if key not in directory.keys():
        return None
    if len(directory[key])> 1:
        val = multipleEntry(key)
        directory[key].remove(val)
        addEntry(key,newVal)
    else:
        directory[key] = [newVal]

def printDirectory():
    for entry in directory:
        print(entry, "-", directory[entry])


if __name__ == "__main__":
    print("TELEPHONE DIRECTORY")
    print('Actions : ')

    while(True):
        print('1. Add Entry \n 2. Remove Entry \n 3. Update Entry \n 4. Search \n 5. Print All Entries \n 6. Exit')

        
        choice = input('What do you want to do ? ')

        if choice == '1':
            name = input('Enter Contact Name:')
            number = input('Enter Contact Number:')
            addEntry(name,number)
        elif choice == '2':
            name = input('Enter Contact Name:')
            value = deleteEntry(name)
            if value is None:
                print('The Entry does not exist')
            else:
                print('Entry Removed')
        elif choice == '3':
            name = input('Enter Key:')
            number = input('Enter Number:')
            val = updateEntry(name,number)
            if val is None:
                print('The Entry does not exist')
            else:
                print('Entry Updated')
        elif choice == '4':
            key = input('Enter Key to search:')
            tempDir = searchEntry(key)
            if not tempDir:
                print('No Entry Matches your Search')
            for entry in tempDir:
                print(entry,'-',tempDir[entry])
        elif choice == '5':
            printDirectory()
        elif choice == '6':
            break
        else:
            print('---Invalid Input---')