import string , random

strings = string.ascii_letters
password = "".join(random.sample(strings,10))
print("your password is :",password)
