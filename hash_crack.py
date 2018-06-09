#!/usr/bin/env python3

import hashlib
import itertools
import time

#defining the function that generates the SHA-512 hash of a string
def hash512(pw):    
    return hashlib.sha512(pw.encode('utf-8')).hexdigest().upper()

#iterating function from here: http://stackoverflow.com/questions/11747254/python-brute-force-algorithm
def bruteForce(charset, maxlength): 
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

#the actual cracking algorithm
def crack512(hashToCrack):

    #defining our char set - we're not using chars_cap yet but it might be useful later if I decide to take over the world
    chars_small='abcdefghijklmnopqrstuvwxyz'
    chars_cap=chars_small.upper()

    #pw not cracked just yet (haven't even started trying...)
    cracked=False

    #check all the possible combinations of strings up to 6 character
    for pwTry in bruteForce(chars_small,3):
        if hash512(pwTry)==hashToCrack:
            cracked=True
            break
    #if cracked, return the pw
    if cracked==True:
        return pwTry

    #otherwise accept defeat
    else:
        return "0"
