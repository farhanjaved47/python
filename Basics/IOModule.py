
"""
Farhan Javed - 11-19-2019
Basic file manipulation including getting the information about files
Basic shell utlity operations like zipping files as well.
"""
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time
import shutil
from zipfile import ZipFile


def main():
    #
    #   Creating, writing and appending to a file.
    #
    file = open("textfile.txt", "w+")
    # arguments are file name and the operation mode in which the file is to be accessed.
    # + means to create the file if it doesn't exist.
    file.write("Writing to this file using Python \r\n")
    for i in range(1,11):
        file.write("Line number : " + str(i) + "\r\n")
    file.close()

    another_file = open("textfile.txt", "a")
    another_file.write("Appending using the operator a")
    for i in range(11, 16):
        another_file.write("Appending line number " + str(i) + "\r\n")

    another_file.close()

    #
    # Reading from a file
    #

    readfile = open("textfile.txt", "r")  # r is read mode.
    if readfile.mode == 'r':
        # contents = readfile.read()     # Read entire content of a file
        print("File opened in read mode")
        fl = readfile.readlines()  # Read the file line by line
        for line in fl:
            print(line)

    print(os.name)
    print("Item exists : " + str(path.exists("textfile.txt")))
    print("Item is a file : " + str(path.isfile("textfile.txt")))
    print("Item is a directory : " + str(path.isdir("textfile.txt")))

    print("Asolute path : " + str(path.realpath("textfile.txt")))
    print("Item path and name: " + str(path.split(path.realpath("textfile.txt"))))

    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    td = datetime.datetime.now() - datetime.datetime.fromtimestamp((
        path.getmtime("textfile.txt")
    ))
    print("It has been " + str(td) + " since the file was last modified")
    print("Or " + str(td.total_seconds()) + " seconds")

    if path.exists("textfile.txt"):
        source = path.realpath("textfile.txt")
        destination = source + ".bak"
        shutil.copy(source, destination)  # only copies the contents over
        # shutil.copystat(source, destination)  # copies over the meta data as well

        # os.rename("textfile.txt", "renamedfile.txt")

        # root_dir, tail = path.split(source)
        # shutil.make_archive("archive", "zip", root_dir)

        with ZipFile("testzip.zip", "w") as newzip :
            newzip.write("textfile.txt")
            newzip.write("textfile.txt.bak")

main()
