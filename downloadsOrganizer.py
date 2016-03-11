'''
Author: Matthew Dickens
Email: matthew@matthew-dickens.com
GitHub: github.com/toltar
VCS: git

'''
import os
import errno
import re
from sys import platform as _platform

FILETYPE = ['png','PNG','ppt','PPT','jpg','jpeg','JPG','gif','GIF','doc','DOC','pdf','PDF','exe','zip','ZIP','msi','MSI','txt','TXT','md']
REGEX = '^.*\.(.*)$'

#1 = windows
#2 = linux
flag = 1

if (_platform == "linux" or _platform == "linux2"):
    #linux
    PATH_DOWNLOADS = "/home/" + os.getenv("USERNAME") + "/Downloads"
    flag = 2

elif (_platform == "win32"):
    #Windows
    PATH_DOWNLOADS = "c:\\Users\\"+os.getenv("USERNAME")+"\\Downloads\\"
    flag = 1

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

            if(flag == 1):
                os.rename(PATH_DOWNLOADS+match.group(0),PATH_DOWNLOADS+match.group(1)+"\\"+match.group(0))
            elif(flag == 2):
                os.rename(PATH_DOWNLOADS+match.group(0),PATH_DOWNLOADS+match.group(1)+"/"+match.group(0))
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
