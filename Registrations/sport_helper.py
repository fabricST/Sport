import random
import string

def random_email():
    email = "storchak.eugene+" + str(random.randint(1, 999)) + "@gmail.com"
    return email



def random_phone():
    phone = random.randint(00000000, 9999999)
    return phone


def random_name(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


def random_surname(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))




