import requests
import sys
import webbrowser
import os
import time
import codecs

ttl = 5

def main():
	if len(sys.argv) == 2:
		start_request(sys.argv[1], "tmp.html")
	elif len(sys.argv) > 2:
		start_request(sys.argv[1], sys.argv[2])
	else:
		print("Not enough arguments")

def start_request(url, filename):
	r = requests.get(url)
	if r.status_code != 200:
		print("Wrong HTTP status code: " + str(r.status_code))
		return
	file = codecs.open(filename, 'w', "utf-8")
	file.write(r.text)
	file.close()

	webbrowser.open(filename, new = 2)
	print("Downloaded page and waiting " + str(ttl) + "s until file gets removed")
	time.sleep(ttl)
	os.remove(filename)
	print("File removed")

if __name__ == "__main__":
	main()
