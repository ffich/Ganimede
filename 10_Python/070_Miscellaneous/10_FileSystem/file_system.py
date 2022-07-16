import os

FOLDER_NAME = 'my_dir'
FILE_NAME = 'my_file.txt'
ERASE_FOLDER = False

if ERASE_FOLDER is True:
    try:
        os.remove(FOLDER_NAME + '/' + FILE_NAME)
        os.rmdir(FOLDER_NAME)
        print('Existing content deleted')
    except OSError as e:
        print('Trying to delete the content on the file system: ' + str(e))

try:
    # Creating a new folder
    os.mkdir(FOLDER_NAME)
except OSError as e:
    print('Trying to create a new folder: ' + str(e))

try:
    # Entering in the new folder
    os.chdir(FOLDER_NAME)
except OSError as e:
    print('Trying to access the folder: ' + str(e))

# Print working directory
print('The current working directory is: ' + os.getcwd())

# List elements in the current directory
elements = os.listdir()
print('In the current directory the following elements are present: ' + str(elements))


if FILE_NAME in elements:
    # Open existing file
    file = open(FILE_NAME)
    content = file.read()
    print('File content: ', content)
else:
    # Create a new file
    file = open(FILE_NAME, 'w')
    # Write some content in the new file
    file.write('Sample content')
    print('New file created')

file.close()
