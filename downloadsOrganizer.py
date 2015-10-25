'''
Author: Matthew Dickens
Email: matthew@matthew-dickens.com
GitHub: github.com/toltar
VCS: git
'''
import os
import sys
import time
import re
FILETYPE = ['png','PNG','ppt','PPT','jpg','jpeg','JPG','gif','GIF','doc','DOC','pdf','PDF','exe','zip','ZIP','msi','MSI','txt','TXT','md']
REGEX = '^.*\.(png|PNG|ppt|PPT|jpg|jpeg|JPG|gif|GIF|doc|DOC|pdf|PDF|exe|zip|ZIP|msi|MSI|txt|TXT|md)$'
PATH_DOWNLOADS = "c:\\Users\\"+os.getenv("USERNAME")+"\\Downloads\\"
FILES = os.listdir(PATH_DOWNLOADS)


#Methods
def main():
    pattern = re.compile(REGEX)
    for _file_ in FILES:
        match = pattern.match(_file_)
        if match:
            extension = os.path.splitext(PATH_DOWNLOADS+_file_)[-1].lower()
            if extension in ".pdf":
                print extension
        else:
            print 'Filetype doesn\'t match'
    printEnv()

def printEnv():
    print FILETYPE
    print REGEX
    print PATH_DOWNLOADS
    print FILES


#Call Main Process
main()
