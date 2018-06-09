#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect
import hash_it
import hash_crack

hashes=[]
cracked="Not cracked (yet)"

app = Flask(__name__)

@app.route('/')
def hasher():
	return render_template("hash.html", hashes = hashes, cracked = cracked)

#not used directly, the form in index.html posts data to /new_msg
@app.route('/hish-hash', methods = ['POST'])
def hish_hash():
	
	if request.method == "POST":

		source_string=request.form['source_string']

		hashes.clear()

		hashes.append({"type":"MD5", "digest": hash_it.hash_md5(source_string)})
		hashes.append({"type":"SHA1", "digest": hash_it.hash_sha1(source_string)})
		hashes.append({"type":"SHA224", "digest": hash_it.hash_sha224(source_string)})
		hashes.append({"type":"SHA256", "digest": hash_it.hash_sha256(source_string)})
		hashes.append({"type":"SHA384", "digest": hash_it.hash_sha384(source_string)})
		hashes.append({"type":"SHA512", "digest": hash_it.hash_sha512(source_string)})

	return redirect('/')

@app.route('/crick-crack', methods = ['POST'])
def crick_crack():
	
	if request.method == "POST":

		target_hash=request.form['target_hash']

		cracked=hash_crack.crack512(target_hash)

	return redirect('/')

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug = True)
