"""
    ############################################################################
    File manipulation will be performed here, basically we will do these below
    [x] Read a single file
    [x] List out all the contents inside the file
    [x] Convert string list into a string to make it splitable
    [x] Use dict to count all the words inside the file
    [x] Read all files from a defined folder
    [x] List out all the contents inside those files
    [x] Handle line breaks
    ############################################################################
"""

from pathlib import Path
from collections import Counter

# Define text folder
FILE_FOLDER = (Path(__file__).resolve().parent).joinpath('Texts')

def read_single_file(file):
    """
        read a single file and return its content
    """
    if(file.exists()):
        read_file = open(file)
        return read_file.readlines()
    else:
        print("Sorry, the file cannot be found!")

def splitter(list):
    # convert list to a string
    new_string = ' '.join(list)
    return new_string.split()


def get_words_list(folder_name):
    """
        Compile all words from the input folders list 
        and return a list of words
        Input: a list of folder
        Output: a list of words compiled from the input folders
    """
    files_list = [x for x in folder_name.glob('**/*.txt')]

    words_list = []
    for i in files_list:
        words_list.extend(open(i).readlines())
    
    return dict(Counter(splitter(words_list)))

def write_output(word_dict):
    """
        Write a words dict to a Output.txt
        Input: a dict
        Output: a Output.txt
    """
    # create an empty output.txt file
    output = open('output.txt', 'w')

    for i in words_dict:        
        output.write(i + " : " + str(words_dict[i]) + "\n")


# an example of reading a single file
content = read_single_file(FILE_FOLDER.joinpath('text1.txt'))
print(content)
print(dict(Counter(splitter(content))))

# read all txt files from defined folder
# if you want to just get the file name, do it x.name

words_dict = get_words_list(FILE_FOLDER)

write_output(words_dict)