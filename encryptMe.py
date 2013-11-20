from Crypto.Util import number
from Crypto.Cipher import AES
import random

def getPrimeP():
   return number.getStrongPrime(512)

def getS():
   return number.getRandomNBitInteger(500)

def bitLen(int_type):
     length = 0
     while (int_type):
         int_type >>= 1
         length += 1
     return(length)

def testBit(int_type, offset):
   mask = 1 << offset
   return(int_type & mask)

def modExpo(b, exp, mod):
   
   multiplier   = b
   total        = 1
   expBitLength = bitLen(exp)
   bitCheck     = 1

   for i in range(0,expBitLength):
      if exp & bitCheck:
         total *= multiplier
         total %= mod
      bitCheck   *= 2
      multiplier *= multiplier
      multiplier %= mod
   
   return total


if __name__ == '__main__':
   message = "The answer is noThe answer is noThe answer is no"
   k  = 'aoqirj.xmbnajsiq'
   iv = '29581948572-1948'

   print "\nECB Mode:"
   obj = AES.new(k, AES.MODE_ECB)
   ciphertext = obj.encrypt(message)
   print ":".join("{00:x}".format(ord(c)) for c in ciphertext)

   obj2 = AES.new(k,AES.MODE_ECB)
   ans  = obj2.decrypt(ciphertext)
   print ans
   
   print "\nCBC Mode:"
   obj3 = AES.new(k, AES.MODE_CBC,iv)
   ciphertext = obj3.encrypt(message)
   print ":".join("{00:x}".format(ord(c)) for c in ciphertext)

   obj4 = AES.new(k,AES.MODE_CBC,iv)
   ans  = obj4.decrypt(ciphertext)
   print ans

   

   
      