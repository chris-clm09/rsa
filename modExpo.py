from Crypto.Util import number
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
   #p = getPrimeP()
   #p = 11221004304600885294104188659916931712956092136446145137932759967304036081615804872183979662824692621670474559770822794365004871518767876140018573394223719

   print "P = ", p
   #s = getS()
   #s = 3269960453160682642769365586258995739204260563922575188966172441606671053198702927851889139826665492193107482775389788624665295763069400554709271487262

   print "S = ", s
   #b = 5
   #b = 46418414992560342058537048437946602126221815133022677185587291033816043133307824747113510263909100398691366334463978207220469548140912716433576050585787
    
   pK = modExpo(b,s,p)
   print "Public Key = ", pK
   
      