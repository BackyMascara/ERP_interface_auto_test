import random
import time


def get_mobile():
    mobiles = ["130","131","132","133","134"]
    number = str(int(time.time()))[2:]
    mobile = random.choice(mobiles) + number
    return mobile