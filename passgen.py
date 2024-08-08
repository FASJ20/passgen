import random
import string
UC= string.ascii_uppercase
LC= string.ascii_lowercase
Dig= string.digits
SP= "!@#$%^&*_+-/|"
all= UC + LC + Dig + SP

def generate_password(length):
    if length< 8:
        raise ValueError("number length invalid")

    password = [random.choice(UC), random.choice(LC), random.choice(Dig), random.choice(SP)]
    password += random.choices(all, k= length - 8)
    random.shuffle(password)
    return ''.join(password)
password_length = 12
password= generate_password(password_length)
print(password)
