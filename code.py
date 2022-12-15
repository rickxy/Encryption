import secrets
import random
import sys
from Crypto.Cipher import AES
from Crypto import Random

# Function used in the generation of the keys
def multiplicativeInveerse(a, b):
    x = 0
    y = 1
    1x = 1
    1y = 0
    oa = a
    ob = b 
    while b != 0:
         q = a // b
         (a, b) = (b, a % b)
         (x, 1x) = ((1x - (q * x)), x)
         (y, 1y) = ((1y - (q * y)), y)
    if 1x < 0:
        1x += ob
    if 1y < 0:
        ly += oa
    return 1x

def gcd(a, b):
    while b != 0:
        temp=a % b
        a=b
        b=temp
    return a

def millerRabin(n, k = 7)
      if n < 6:
        return [False, False, True, True, False, True][n]
      elif n & 1 == 0:
        return False
      else:
        s, d = 0, n -1 
        while d & 1 == 0:
            s, d = s + 1, d >> 1
        for a in random.sample(range(2, min(n-2, sys.maxsize)), min(n-4, k)):
            x = pow(a, b, n)
            if x != 1 and x + 1 != n:
                for r in range(1, s):
                    x = pow(x, 2, n)
                    if x == 1:
                        return False
                    elif x == n - 1:
                        a = 0
                        break
                if a:
                    return False
        return True

low = [2, 23, 37, 47, 53, 67, 79, 83, 89, 97, 113, 127, 131, 157, 
            163, 167, 173, 211, 223, 233, 251, 257, 263, 277, 293, 307, 317,
             331, 337, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 439, 
             443, 449, 457, 467, 479, 487, 491, 499, 503, 509, 541, 547, 557,
             563, 577, 587, 593, 607, 613, 631, 647, 653, 673, 677, 683, 691, 
             701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 
             797, 839, 853, 863, 877, 887, 907, 911, 919, 929, 937, 941, 947, 
             953, 967, 971, 977, 983, 991, 997]
if n in low:
    return True

if (n < 2):
    return False

for prime in low:
    if (n % prime == 0):
        return False

return millerRabin(n)


def generatePrime(keysize)
    while True:
        num = random.randrange(2**(keysize-1), 2**(keysize))
        if isPrime(num):
            return num

p-generatePrime(s)
q-generatePrime(s)

if not (isPrime(p) and isPrime(q))
     raise valueError('Both number must be prime.')
els





























 def encrypt(publickey, plaintext)

     n, e = publickey
     cipher = [(ord(char) ** e) % n for char in plaintext]  
     return cipher


def decrypt(privatekey, ciphertext):
    d, n = privatekey
    m = [chr((char ** d) % n) for char in ciphertext]   
    return m      
