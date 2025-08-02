# my_random.py
import random
import time
import threading
import signal

stop_flag = threading.Event()

def generate_numbers():
    while not stop_flag.is_set():
        num = random.randint(1, 100)
        with open("rnd.txt", "w") as f:
            f.write(f"{num}\n")
        time.sleep(10)

def handle_signal(signum, frame):
    stop_flag.set()

if __name__ == "__main__":
    # Регистрируем обработчик сигнала
    signal.signal(signal.SIGTERM, handle_signal)
    
    generator_thread = threading.Thread(target=generate_numbers)
    generator_thread.start()
    generator_thread.join()