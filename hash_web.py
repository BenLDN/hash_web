#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect
import hash_it
import hash_crack
import time

#default (starting) values of the variables used in the app
hashes=[]
cracked="Not cracked (yet)"
crack_time="n/a"

app = Flask(__name__)
app.config['APPLICATION_ROOT'] = "/fun-with-hashes"
prefix="/fun-with-hashes"

@app.route(prefix+'/')
def hasher():

	return render_template("hash.html", hashes = hashes, cracked = cracked, crack_time = crack_time, prefix=prefix)

#when the user clicks on the "Hish Hash" button, the key from the input box is passed to the hasher module
@app.route(prefix+'/hish-hash', methods = ['POST'])
def hish_hash():

	if request.method == "POST":

		source_string=request.form['source_string']

		del hashes[:]
		#hashes.clear()

		hashes.append({"type":"MD5", "digest": hash_it.hash_md5(source_string)})
		hashes.append({"type":"SHA1", "digest": hash_it.hash_sha1(source_string)})
		hashes.append({"type":"SHA224", "digest": hash_it.hash_sha224(source_string)})
		hashes.append({"type":"SHA256", "digest": hash_it.hash_sha256(source_string)})
		hashes.append({"type":"SHA384", "digest": hash_it.hash_sha384(source_string)})
		hashes.append({"type":"SHA512", "digest": hash_it.hash_sha512(source_string)})

	return redirect(prefix+'/')

#When the user clicks on the "Crick Crack" button, the hash from the input box and the chosen hash function are passed to the cracker module
@app.route(prefix+'/crick-crack', methods = ['POST'])
def crick_crack():

	start = time.time()

	#varibales should are used by the main function (hasher) as well
	global cracked
	global crack_time
	
	if request.method == "POST":

		target_hash=request.form['target_hash'].strip()
		cracked=hash_crack.crack_it(target_hash, request.form["hash_type"])

	end = time.time()
	
	crack_time = str(end - start)

	return redirect(prefix+'/')

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug = True)
