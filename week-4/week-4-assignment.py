
# File reading and writing

def read_write():
    file = input('File Name: ')
    try:
        with open(file, 'r') as f:
            data = f.read()
            print()
            print('___Original Data:___')
            print(data)

        # Modify and write the contents to the new file
        
        with open('modified.txt', 'w') as f:
            f.write(data.upper())  

        print('Modified content has been written to "modified.txt".')

    except FileNotFoundError:
        print(f'File "{file}" not found.')

read_write()
