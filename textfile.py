import time as t
from os import path,remove


def createFile(dest):
    """
    Creating a file
    """
    date = t.localtime(t.time())
    name = '%d_%d_%d.html' % (date[1], date[2], (date[0] % 100))

    if fileCheck(dest + name):
        print "File Exists"
        removeFile(dest + name)

    if not (path.isfile(dest + name)):
        f = open(dest + name, 'w')
        for i in range(11):
            f.write(str(i) + '\n')
        f.close()
        print "File Created"
        openFile(dest + name)
        removeFile(dest + name)


def fileCheck(dest):
    """
    Verification
    """
    if (path.isfile(dest)):
        return True
    else:
        return False


def removeFile(dest):
        remove(dest)
        print "File has been Deleted....!!"

def openFile(dest):
        f = open(dest, 'r')
        read_Data = f.read()
        print read_Data
        f.close()

def cFile(dest):
    date = t.localtime(t.time())
    for i in range(6):
        i = i + 1
        name = '%d_%d_%d_%d_%d.html' % (date[1], date[2], (date[0] % 100), date[5], i)
        open(dest + name + str(i), 'a').close()
        if (path.isfile(dest + name + str(i))):
            print dest + name + str(i)
            remove(dest + name + str(i))
    print " 5 Files created... And Delted!!"




if __name__ == '__main__':
    destination = "/home/rameshshihora/python/"
    createFile(destination)
    cFile(destination)

    #raw_input("Done\n")
