from itertools import izip
import sys, os

def copyWithoutIfDef(fileName):
  with open(fileName, 'r') as template:
    with open(fileName + '.copy', 'w+') as copy:
      defBlock = False
      for line in template:
        if line.startswith('#ifdef') or line.startswith('#ifndef'):
          defBlock = True
          continue
        if line.startswith('#endif'):
          defBlock = False
          continue
        if not defBlock:
          copy.write(line)

def checkForEditsOutsideIfDef(newFile, originalFile):
  # Status that will be returned
  status = 0

  # Copy all files, but ignore all #ifdef blocks
  copyWithoutIfDef(newFile)
  copyWithoutIfDef(originalFile)

  # Compare copied files
  with open(newFile + '.copy', 'r') as fileA, open(originalFile + '.copy', 'r') as fileB:
    if fileA.readlines() == fileB.readlines():
      status = 1
    else:
      status = -1

  # Clean up
  if os.path.exists(newFile + '.copy'):
    os.remove(newFile + '.copy')
  else:
    print("Couldn't find file to clean up: " + newFile + '.copy')
    status = -1
  if os.path.exists(originalFile + '.copy'):
    os.remove(originalFile + '.copy')
  else:
    print("Couldn't find file to clean up: " + originalFile + '.copy')
    status = -1

  return status

  # Help from:
  # https://codereview.stackexchange.com/questions/30912/compare-file-with-ignore-some-line-last-line
  # https://stackoverflow.com/questions/15343743/copying-from-one-text-file-to-another-using-python
