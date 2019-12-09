"""
Farhan Javed
farhan.javed47@gmail.com
12/9/2019
Basic File I/O
"""


def main():
    infile = open("lines.txt", 'rt')  # r - read only, w - flush file and write, a - append the file, + = read and write
    #  t = text, b = binary. Default is text mode
    #  text files are handled differently by different operating systems.
    #  make sure to explicitly specify the modes as explicit is better than implicit - Python Zen
    outfile = open('lines-copy.txt', 'wt')
    for line in infile:  # this enables us to read the file line by line without loading the entire file into memory
        print(line.rstrip(), file=outfile)  # strips the white spaces at the end of the line.
        # the print function strips the white spaces and adds the line endings for the OS in which the file is running.
        # outfile.write(line)  # alternate method to write files
        print('.', end="", flush=True)
        outfile.close()
        print('\ndone')


if __name__ == '__main__' : main()