#!/usr/bin/env python3

import hashlib
import itertools
import time
import hash_it

#function to iterate through the possible combinations
#source: http://stackoverflow.com/questions/11747254/python-brute-force-algorithm
def bruteForce(charSet, maxLength): 
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charSet, repeat=i)
        for i in range(1, maxLength + 1)))

#the actual cracking algorithm
def crack_it(hashToCrack, hashType):

    #defining our char set - we're not using chars_cap yet but it might be useful later if I decide to take over the world
    chars_small='abcdefghijklmnopqrstuvwxyz'
    chars_cap=chars_small.upper()

    #pw not cracked just yet (haven't even started trying...)
    cracked=False

    #check all the possible combinations of strings up to 4 character
    for pwTry in bruteForce(chars_small,4):
        if hashType=="md5":
            if hash_it.hash_md5(pwTry)==hashToCrack:
                cracked=True
                break
        elif hashType=="sha1":
            if hash_it.hash_sha1(pwTry)==hashToCrack:
                cracked=True
                break
        elif hashType=="sha224":
            if hash_it.hash_sha224(pwTry)==hashToCrack:
                cracked=True
                break
        elif hashType=="sha256":
            if hash_it.hash_sha256(pwTry)==hashToCrack:
                cracked=True
                break
        elif hashType=="sha384":
            if hash_it.hash_sha384(pwTry)==hashToCrack:
                cracked=True
                break
        elif hashType=="sha512":
            if hash_it.hash_sha512(pwTry)==hashToCrack:
                cracked=True
                break


    #if cracked, return the pw
    if cracked==True:
        return pwTry

    #otherwise accept defeat
    else:
        return "I couldn't crack it :("
