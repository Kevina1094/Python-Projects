import os

def main():
    path = input('Enter the file location: ')
    path = path.replace('\\', '/')  
    print(path)

    Directory = os.listdir(path)
    print(Directory)

    for count, picture_name in enumerate(Directory):
        new_name = f'Picture{count}.jfif'
        old_name = os.path.join(path, picture_name)
        new_name = os.path.join(path, new_name)
        os.rename(old_name, new_name)

if __name__ == '__main__':
    main()
    


    

