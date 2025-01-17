#!/usr/bin/python

import os
from fnmatch import fnmatch
from fakeflac_calculator import CalculateFakeFlacValue

fakeFlacFile = 'fakeflac.txt'

def sanitizeFileName(fileName):
    # Check if the last character is a trailing / or \
    if (fileName[-1:] in ['/', '\\']):
        fileName = fileName[:-1]  # Strip the last character
    return fileName

# Body 
import argparse
parser = argparse.ArgumentParser(description='Detect fake flac\'s')

parser.add_argument('sourcefolder', metavar='sourcefolder', type=str, help='root-folder containing music files (flac)')
parser.add_argument('-s', '--scan', help="scan for fake flac files in given sourcefolder (default)", action="store_true")
#parser.add_argument('-r', '--report', help="report for all " + fakeFlacFile + " files", action="store_true")   
parser.add_argument('--extension', type=str, help="files with 'extension' are being scanned; 'flac' is default",  nargs=1) 

args = parser.parse_args()

source_tree = sanitizeFileName(args.sourcefolder)
scanMode = args.scan
extension = args.extension
#reportMode = args.report

#if not scanMode and not reportMode:
#    scanMode = True
#if scanMode and reportMode:
#    reportMode = False

if not scanMode:
    scanMode = True
if not extension:
    extension = 'flac'
else:
    extension = args.extension[0]

for dir, dirNames, fileNames in os.walk(source_tree):
    dirNames.sort()

    if scanMode:
        print(dir)
        for fileName in sorted(fileNames):
            fullFileName = os.path.join(dir, fileName)
            if fnmatch(fullFileName, "*." + extension):   
#                fakeFlacFileFound = False         
#                for fileName in sorted(fileNames):
#                    fullFileName = os.path.join(dir, fileName)
#                    if fnmatch(fullFileName, "*/" + fakeFlacFile):
#                        fakeFlacFileFound = True
#                        break
#                if not fakeFlacFileFound:
#                    os.system('dr14_tmeter "' + dir + '"')
                CalculateFakeFlacValue(fullFileName)
#                break
'''
    if reportMode:
        for fileName in sorted(fileNames):
            fullFileName = os.path.join(dir, fileName)
            if fnmatch(fullFileName, "*/" + fakeFlacFile):
                valueAsAstring = os.popen('cat "' + dir + '/dr14.txt" | grep "Official DR value:" | cut -c24-27 &> /dev/null').read().strip()
                if len(valueAsAstring) < 2:
                    valueAsAstring = '0' + valueAsAstring
                dirName = dir.replace(source_tree + '/', '')
                print(valueAsAstring + ' ' + dirName)
                break        
'''
