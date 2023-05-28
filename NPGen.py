import argparse
import random
import string

def genpass(length, pattern):
    password = []
    for char in pattern:
        if char == '@':
            password.append(random.choice(string.ascii_lowercase))
        elif char == ',':
            password.append(random.choice(string.ascii_uppercase))
        elif char == '*':
            password.append(random.choice(string.digits))
        elif char == '^':
            password.append(random.choice(string.punctuation))
        else:
            password.append(char)

    return ''.join(password)

def savepass(password, filename):
    if filename:
        with open(filename, "w") as file:
            file.write(password)
            print(f"Password saved to file: {filename}")

def main():
    parser = argparse.ArgumentParser(description='Password Generator by Moraa')
    parser.add_argument('-t', '--pattern', type=str, help='Pattern for the password, please put the symbols inside \'\' ( @ will insert lower case characters / , will insert upper case characters / * will insert numbers / ^ will insert symbols) (optional)')
    parser.add_argument('-l', '--length', type=int, default=8, help='Length of the password')
    parser.add_argument('-o', '--output', type=str, help='Output file name (optional)')
    parser.add_argument('-n', '--count', type=int, default=1, help='Number of passwords to generate (default: 1)')

    args = parser.parse_args()

    if not args.length:
        parser.print_help()
        return

    if args.length < 8:
        print("Error: Password length should be at least 8 characters for security reasons (12 characters or more are recommended).")
        return

    passwords = []
    for _ in range(args.count):
        if args.pattern:
            password = genpass(args.length, args.pattern)
        else:
            password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=args.length))
        passwords.append(password)

    for password in passwords:
        print("---")
        print(f"Password generated: {password}")
        savepass(password, args.output)
        print("---")

if __name__ == "__main__":
    main()
