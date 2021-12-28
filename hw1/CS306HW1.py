#Nick Guo
#I pledge my honor that I have abided by the Stevens Honor System
import collections
from operator import itemgetter

hexString = []
arr = []
filename = 'hw1.txt'
frequentArr = []
order = [' ','.',',']
keys = []
column = []
strings=[]

for i in range(26):
    order.append(chr(ord('a')+i))
    order.append(chr(ord('A')+i))

def getHexString():
    file1 = open(filename,'r')
    while True:
        line = file1.readline()
        if not line:
            break
        if line[-1] == '\n':
            line = line[:-1]
        hexString.append(line)
    file1.close()


    	
def convertToHeximal():
    for n in hexString:
        c = []
        for i in range(33):
            ind = 2*i
            num = "".join(n[ind:ind+2])
            c.append(hex(int(num,16)))
        arr.append(c)

def CountFrequency(arr):
    return collections.Counter(arr)
     
def findFrequency():
    for i in range(33):
        temp = []
        for j in range(11):
            temp.append(arr[j][i])
        freq = CountFrequency(temp)
        fre = []
        high = 0
        fre = freq.items()
        frelist = sorted(fre, key = itemgetter(1))
        for (key,value) in frelist:
            if value == high:
                high = value
                fre.append(key)
            elif value > high:
                high = value
                fre = []
                fre.append(key)
        frequentArr.append(fre)

def isValid(num):
    return chr(num) in order

def xorCipher(ele,key):
    return isValid(int(ele,16)^int(key,16))


def cipher_valid(array,key):
    result = True
    for n in array:
        if not xorCipher(n,key):
            result = False
            break;
    return result


def generateKeys():
    getHexString()
    convertToHeximal()
    findFrequency()
    for i in range(33):
        temp = []
        for j in range(11):
            temp.append(arr[j][i])
        column.append(temp)
    for i,n in enumerate(frequentArr):
        keyFound = False
        j = 0
        while not keyFound and j < len(n):
            item = n[j]
            num = int(item,16)
            for m in order:
                testXOR = hex(num^ord(m))
                if cipher_valid(column[i],testXOR):
                    keys.append(testXOR)
                    keyFound = True
                    break;
            j += 1
        if not keyFound:
            print("Could not find key for",n)
def printoutmessages():
    generateKeys()
    k = ""
    print("KEYS")
    for n in keys:
        k = k+n[2:]+" "
    print(k)
    print("------------------------------")
    #keys[-3]='0x21'
    for sentences in arr:
        sentence = []
        for i in range(33):
            s = chr(int(sentences[i],16)^int(keys[i],16))
            sentence.append(s)
        strings.append("".join(sentence))
    for st in strings:
        print(st)
            
printoutmessages()

            
