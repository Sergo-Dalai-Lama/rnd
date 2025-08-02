import random
import time

while True:
    with open("rnd.txt", "a") as f:
        num = random.randint(1, 100)
        f.write(f"{num}\n")
    time.sleep(10)