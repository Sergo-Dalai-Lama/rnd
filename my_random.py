import random
import time
import threading
import sys

def generate_numbers():
    while not stop_flag.is_set():
        num = random.randint(1, 100)
        with open("rnd.txt", "w") as f:  # 'w' - перезапись файла
            f.write(f"{num}\n")
        time.sleep(10)

def wait_for_exit():
    input("Нажмите Enter для остановки...\n")
    stop_flag.set()

if __name__ == "__main__":
    stop_flag = threading.Event()
    
    # Запускаем генерацию чисел в отдельном потоке
    generator_thread = threading.Thread(target=generate_numbers)
    generator_thread.start()
    
    # Ожидаем нажатия Enter в основном потоке
    wait_for_exit()
    
    # Дожидаемся завершения потока с генерацией
    generator_thread.join()
    
    print("Программа остановлена")