#!/usr/bin/py
import requests
import sys
import os
import webbrowser

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
	file = open(filename, 'w')
	file.write(r.text)
	file.close()
	webbrowser.open(filename, new = 2)
	#os.remove(filename)
	# wait for enter
	# afterwards delete the file and end the program

if __name__ == "__main__":
	main()
