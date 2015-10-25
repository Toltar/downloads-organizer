'''
Author: Matthew Dickens
Email: matthew@matthew-dickens.com
GitHub: github.com/toltar
VCS: git

'''
import os
import errno
import shutil
import sys
import time
import re
FILETYPE = ['png','PNG','ppt','PPT','jpg','jpeg','JPG','gif','GIF','doc','DOC','pdf','PDF','exe','zip','ZIP','msi','MSI','txt','TXT','md']
REGEX = '^.*\.(.*)$'
PATH_DOWNLOADS = "c:\\Users\\"+os.getenv("USERNAME")+"\\Downloads\\"
FILES = os.listdir(PATH_DOWNLOADS)


#Methods
def main():
    pattern = re.compile(REGEX)
    for _file_ in FILES:
        match = pattern.match(_file_)
        if match:
            directory = PATH_DOWNLOADS + match.group(1)
            if not os.path.exists(directory):
                file_path_creation(directory)
            print ('Moving -> ' + _file_)
            os.rename(PATH_DOWNLOADS+match.group(0),PATH_DOWNLOADS+match.group(1)+"\\"+match.group(0))
        else:
            print ('Not a file, must be a directory ->' + _file_)
    printEnv()

def printEnv():
    print FILETYPE
    print REGEX
    print PATH_DOWNLOADS
    print FILES
def file_path_creation(path):
    try:
        print ('Creating non existant directory' + os.path.splitext(path)[-1].lower())
        os.makedirs(path)
        print ('Directory successfully created')
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

#Call Main Process
main()
