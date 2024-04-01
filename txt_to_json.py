#!/usr/bin/env python3

import argparse
import json
import sys

class Converter:
    def __init__(self, usernames_file, passwords_file, output_file):
        self.usernames_file = usernames_file
        self.passwords_file = passwords_file
        self.output_file = output_file

    def read_usernames(self):
        usernames = []
        try:
            with open(self.usernames_file, 'r') as file:
                for line in file:
                    username = line.strip()
                    usernames.append(username)
        except FileNotFoundError:
            print(f"Error: {self.usernames_file} not found.")
            sys.exit(1)
        return usernames

    def read_passwords(self):
        passwords = []
        try:
            with open(self.passwords_file, 'r') as file:
                for line in file:
                    password = line.strip()
                    passwords.append(password)
        except FileNotFoundError:
            print(f"Error: {self.passwords_file} not found.")
            sys.exit(1)
        return passwords

    def convert_to_json(self):
        usernames = self.read_usernames()
        passwords = self.read_passwords()
        data = {"usernames": usernames, "passwords": passwords}
        return json.dumps(data, indent=4)

def main():
    parser = argparse.ArgumentParser(description='Convert usernames and passwords to JSON format')
    parser.add_argument('usernames_file', type=str, help='Path to the usernames file')
    parser.add_argument('passwords_file', type=str, help='Path to the passwords file')
    parser.add_argument('-o', '--output', type=str, help='Output file name (default: output.json)', default='output.json')
    args = parser.parse_args()

    converter = Converter(args.usernames_file, args.passwords_file, args.output)
    json_string = converter.convert_to_json()

    with open(args.output, "w") as json_file:
        json_file.write(json_string)

    print(f"Conversion to JSON format completed successfully. Output saved as '{args.output}'.")

if __name__ == "__main__":
    main()
