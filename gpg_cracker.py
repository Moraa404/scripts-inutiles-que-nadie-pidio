import argparse
import gnupg
import threading

def print_success(v):
    print("\033[1;32m[+]" + "\033[0m", v)
def print_error(v):
    print("\033[1;31m[-]" + "\033[0m", v)

def test(passwords, gpg_file):
    gpg = gnupg.GPG()
    for password in passwords:
        result = gpg.decrypt_file(gpg_file, passphrase=password)
        if result.ok:
            print_success(f"Password Found:" + password)
            return password
    return None

def run(gpg_file, passwords_file, num_threads=1):
    try:
        with open(passwords_file, 'r') as f:
            passwords = f.read().splitlines()
    except FileNotFoundError:
        print_error(f"Error: Password file not Found" + passwords_file )

    passwords_pt = len(passwords)
    password_ch = [passwords[i:i+passwords_pt] for i in range(0, len(passwords), passwords_pt)]

    threads = []
    for ch in password_ch:
        thread = threading.Thread(target=test, args=(ch, gpg_file))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    hp = argparse.ArgumentParser(description='PGP Pass cracker')
    hp.add_argument("-g", "--file", help="GPG File")
    hp.add_argument("-w", "--wordlist", help="Wordlist")
    hp.add_argument("-t", "--threads", type=int, default=1,help="Number of Threads to use")
    args = hp.parse_args()

print_success(f"Starting password attack!")

run(args.file, args.wordlist, args.threads)

print_success("Complete!")
