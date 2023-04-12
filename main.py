import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generated_password(question_lenght_pass):

    random.shuffle(characters)

    password = []
    for x in range(question_lenght_pass):
        password.append(random.choice(characters))
    random.shuffle(password)


    password = "".join(password)

    return str(password)

