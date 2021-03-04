''' Week 1 Lab: Python exercise for Encryption & Decryption '''
''' Bit Manipulation '''

import random 

# 1) Python bitwise and (&), or(|), exclusive or(^) 
qs1 = 8 & 3   # 0
print(qs1)

qs2 = 5 | 3    # 7
print(qs2)

qs3 = 5 ^ 3
print(qs3)      # 6

qs4 = (5 | 3)
print(qs4)      # 7

qs5 = (5 ^ 3) ^ 3
print(qs5)       # 5

# 2)
print(">>> x < 256 ???")  
x = random.randint(0, 100)
print(">>> x is ", x)
task2a =  ((x&0x80)>>7)^((x<<1)&0xFF) 
task2b = ((x&0x01)<<7)^((x>>1)&0x7F) 
print("((x&0x80)>>7)^((x<<1)&0xFF) = ", task2a)
print("((x&0x01)<<7)^((x>>1)&0x7F) = ", task2b)


# 3) In encrypting plain text, it's the bit patterns representing the characters/numerals that are manipulated
# ord() returns the number representing the unicode code of a specified character.
task3a = ord('A') << 2
print("ord('A') << 2 = ", task3a)

task3b = ord('A') >> 1
print("ord('A') >> 1 = ", task3b)

task3c = ord('A') >> 2
print("ord('A') >> 2 = ", task3c)

task3d = (ord('A') >> 2) << 1
print("(ord('A') >> 2) << 1 = ", task3d)        # 66

task3e = (ord('C') >> 2) << 1
print("(ord('C') >> 2) << 1 = ", task3e)        # 32

task3d = ord('A') & 3
print("ord('A') & 3 = ", task3d)                # 1

task3e = ord('A') | 3
print("ord('A') | 3 = ", task3e)                # 67

task3f = ord('A') ^ 3
print("ord('A') ^ 3 = ", task3f)                 # 66

task3g = chr(ord('A')^3)
print("chr<ord('A') ^ 3) = ", task3g)            # B

task3h = chr((ord('A')^23)^23)                  
print("chr((ord('A') ^ 23) ^ 23) = ", task3h)    # A



''' asciibin.py -- reads a printable character '''
''' Outputs its decimal and binary ascii code '''
character1 = input('Input a printable character: ')
acharacter1 = ord(character1)
bits = ''

# computes 7 bit binary code
for i in range(7):
    if(acharacter1 & pow(2,i) == 0):
        bits = '0' + bits
    else:
        bits = '1' + bits
print(">>> asciibin.py")
print("The character {} has a decimal ascii code of {}\n\
    and a 7 bit binary code of {}".format(character1, acharacter1, bits))



''' asciibin2.py -- reads a printable character & '''
''' Outputs its decimal & binary ASCII code '''
character2 = input("Input a printable character: ")
acharacter2 = ord(character2)
bits2 = ''
mask = 1

# computes a 7 bit binary code
for i in range(7):
    if(acharacter2 & mask == 0):
        bits2 = '0' + bits2
    else:
        bits2 = '1' + bits2
    mask <<= 1

print("The character %c has a decimal ASCII code of %d\n\
    and a 7 bit binary code %s" % (character2, acharacter2, bits2))


''' Writes ASCII script that has same functionality as the code blocks above but uses funnction baseconvert '''
# asciibin3.py -- reads a printable character and
# outputs its decimal and binary ascii code

from baseconv import *
character = input('Input a printable character: ')

bits = baseconvert(ord(character),BASE10,BASE2)
print ('The character %c has a decimal ascii code of %d\n\
and a 7 bit binary code of %s' % (character, ord(character), bits))


''' asciibin4.py -- reads a printable character & outputs its decimal and binary ASCII code '''

import sys
# computes binary code        
def bin(i):
    j=0
    if(i!=0):
        j=i

bin(i>>1)
sys.stdout.write(j&1)
character = input('Input a printable character: ')
acharacter = ord(character)
print ('The character %c has a decimal value of %d' % (character,acharacter))
print ('and a binary code of ',; bin(acharacter))






# mystery.py
mask = 0x40                                         # 0x40 (Hexadecimal) = 7th bit
char = input('Input a printable character: ')       # Asks for a user input 
byte = ord(char)                                    # ord returns number representing unicode of string
sys.stdout.write('%c %d %x' % (char,byte,byte))     # outputs: char, byte, byte
for i in range(7):                                  # iterates over 7 times to compute arithmetic shift right operations (>> = rshift)
    sys.stdout.write(((mask >> i) & byte) >> (6-i)) 



