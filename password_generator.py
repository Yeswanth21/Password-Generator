import random 
import string 
def password_generator(length = 12, use_upper = True, use_digit = True, use_symbol = True):
    if length <= 8:
        raise ValueError("Password length must be greater than 8 for better security.")
    
    if not(use_upper and use_digit and use_symbol):
        raise ValueError("Password must contain uppercase, lowercase, symbol and a digit for better security.")
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = upper+lower+symbols+digits
    
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols)
        ]
    
    while len(password) < length:
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return ''.join(password)

if __name__ == '__main__':
    print('🔐 Secure Password Generator 🔐')

    while True:
        try:
            length = int(input("Enter password length (must be > 8):"))
            if length <= 8:
                print("❌ Password length must be greater than 8. Try again.")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number.")

    
    print("For security reasons password will include:")
    print("✅ Uppercase letters\n ✅ Digits\n ✅ Symbols\n (This is required for strong password enforcement.)")

    try:
        password = password_generator(length, use_upper=True, use_digit=True, use_symbol=True)
        print(f"✅ Generated password:{password}")
    except ValueError as ve:
        print(f'\n Error: {ve}')