import hashlib
import argparse
import sys
import os
from sets import Set
import time

parser = argparse.ArgumentParser(description='Synopsis v1.0.0 by ThanhMinh', epilog='Use the -h -l command to get a list of the type of encryption')
parser.add_argument('-i','--input', help='Insert the file path to encrypt')
parser.add_argument('-o','--output',help='Insert the file path to output data')
parser.add_argument('-f','--format',help='Type of encryption')

class Middleware:

    #Check the input arguments
    def __init__(self,lengthArg):
        self.Pick = None
        if (lengthArg == 6):
            self.ConvertFileToFile()
        elif (lengthArg == 2):
            self.ShowListEncryption()
        else:
            self.ShowHelp()

    def ConvertFileToFile(self):
        if (sys.argv[1].find('-i') != -1  and sys.argv[3].find('-o') != -1 and sys.argv[5].find('-f') != -1):
            self.pick = "FileToFile"
        else:
            print(sys.argv[5].find('-f'))
            self.ShowHelp()

    def ShowListEncryption(self):
        if (sys.argv[1].find('-h') != -1 and sys.argv[2].find('-l') != -1):
            listHash = []
            for hs in hashlib.algorithms_available:
                listHash.append(hs.lower())
            listHash = Set(listHash)
            print 'Synopsis v1.0.0 has' ,len(listHash),'type of encryption: \n' 
            for hs in listHash:
                print hs
            parser.exit()
        else:
            self.ShowHelp()

    def ShowHelp(self):
        parser.print_help()
        parser.exit()


start = Middleware(len(sys.argv[1:]))

args = parser.parse_args()

class Handler:
    def __init__(self,pick):
        #Check the encoding that is in the list of supported encodings
        if args.format.lower() in hashlib.algorithms_available:

            if (pick == 'FileToFile'):
                self.start_time = time.clock()
                print 'The process begins... \n'
                try:
                    fopen = open(args.input,'r')
                    fwrite = open(args.output,'w')
                    countLine = 0
                    for line in fopen:
                        if '\n' in line:
                            line = line.replace('\n','')
                            countLine += 1
                        sw = self.Handler(line,args.format)
                        fwrite.write(sw + '\n')
                    fopen.close()
                    fwrite.close()
                    self.Done(countLine)
                except:
                    print 'No such file or directory:',args.input
                    parser.print_help()

        else:
            print 'Type of encrytion not found'
            parser.print_help()

    def GetFileSize(self,num):
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            num /= 1024.0

    def Done(self,line):
        print 'The process is completed: \n'
        print 'Output Location: ',args.output
        print 'Input Size: ',self.GetFileSize(os.stat(args.input).st_size)
        print 'Output Size: ',self.GetFileSize(os.stat(args.output).st_size)
        print 'Number of lines: ',line
        print 'Type of encryption: ',args.format
        print 'Time: ',time.clock() - self.start_time, "seconds"

    def Handler(self,hashString, hashType):
        try:
            hashString = hashString.encode()
            hs = hashlib.new(hashType)
            hs.update(hashString)
        except ValueError:
            return 'Hash not found';
        else:
            return hs.hexdigest();

handling = Handler(start.pick)
