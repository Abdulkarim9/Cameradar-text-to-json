#!/usr/bin/env python3

import sys
import json


input_file_usernames = ""
input_file_passwords = ""

if len(sys.argv) < 3:
	print(f"usage: python3 {__file__} usernames.txt passwords.txt")
else:
	input_file_usernames = sys.argv[1]
	input_file_passwords = sys.argv[2]


usernames = []
passwords = []

with open(input_file_usernames, 'r') as file:
	for line in file:
		username = line.strip()
		usernames.append(username)


with open(input_file_passwords, 'r') as file:
	for line in file:
		password = line.strip()
		passwords.append(password)


data = {"usernames": usernames, "passwords": passwords}

json_string = json.dumps(data, indent=4)

with open("output.json", "w") as json_file:
    json_file.write(json_string)

print("conversion JSON format completed successfully.")


