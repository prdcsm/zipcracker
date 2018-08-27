#!/usr/bin/python3

import zipfile
import argparse

def Main():
    parser = argparse.ArgumentParser("-z <zipfile> -d <dictionary>")
    parser.add_argument("-z", dest="zip", help="name of the zip file")
    parser.add_argument("-d", dest="dict", help="name of the dictionary file")
    options = parser.parse_args()
    if (options.zip == None) | (options.dict == None):
        parser.print_help()
        exit(0)
    else:
        zname = options.zip
        dname = options.dict

    zip = zipfile.ZipFile(zname)
    with open(dname, 'r', encoding='latin1') as f:
        for line in f.readlines():
            pw = line.strip('\n')
            try:
                zip.extractall(pwd=pw.encode())
                print("password found: " + pw)
                break

            except:
                pass

if __name__ == '__main__':
    Main()