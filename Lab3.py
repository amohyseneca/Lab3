#!/usr/bin/env python3

def writeToFile(fileName, text):
  file.open(fileName, 'w')
  file.write(text + '\n')
  file.close

def helloWorld():
  print("Hello World")



if __name__ == '__main__':
  helloWorld()
  writeToFile(test.txt, 'Hello.')
