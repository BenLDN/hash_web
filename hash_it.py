#!/usr/bin/env python3

import hashlib

#defining hash functions

def hash_md5(pw):    
    return hashlib.md5(pw.encode('utf-8')).hexdigest().upper()

def hash_sha1(pw):    
    return hashlib.sha1(pw.encode('utf-8')).hexdigest().upper()

def hash_sha224(pw):    
    return hashlib.sha224(pw.encode('utf-8')).hexdigest().upper()

def hash_sha256(pw):    
    return hashlib.sha256(pw.encode('utf-8')).hexdigest().upper()

def hash_sha384(pw):    
    return hashlib.sha384(pw.encode('utf-8')).hexdigest().upper()

def hash_sha512(pw):    
    return hashlib.sha512(pw.encode('utf-8')).hexdigest().upper()




