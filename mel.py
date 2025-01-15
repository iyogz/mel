import time
import sys
import random
import string

def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{username}@gmail.com"

def fake_loading(message, total_steps=100, delay=0.05):
    for i in range(total_steps + 1):
        progress = f"{message} [{('#' * (i // 2)).ljust(50)}] {i}%"
        sys.stdout.write(f"\r{progress}")
        sys.stdout.flush()
        time.sleep(delay)
    print(" ✅")

def main():
    print("Opening melodai.pro/airdrop")
    time.sleep(1)
    
    print("Connecting wallet...")
    fake_loading("  Progress", total_steps=100, delay=0.03)
    
    time.sleep(1)
    random_email = generate_random_email()
    print(f"\nEntering email: {random_email}")
    time.sleep(1)

    print("Verifying email...")
    time.sleep(2)
    print("  Verification complete ✅")

    time.sleep(1)
    print("Claiming 50 $MELAI...")
    time.sleep(2)
    print("  Claim successful ✅")

if __name__ == "__main__":
    main()
