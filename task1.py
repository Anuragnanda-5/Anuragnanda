try:
    file = open('sample.txt', 'r')
    reading_file = file.readlines()
    print('reading file content')
    x=1
    for i in reading_file:
        print('line '+ str(x) + ': ' + i)
        x+=1
    file.close()
except FileNotFoundError:
    print('Error: The file sample.txt was not found')