import threading
import time

def my_function(id):
    for i in range(1, 4):
        print(f"Thread {id}: {i}")
        time.sleep(1)

# Créer des threads
thread1 = threading.Thread(target=my_function, args=(1,))
thread2 = threading.Thread(target=my_function, args=(2,))

# Démarrer les threads
thread1.start()
thread2.start()

# Attendre que les threads se terminent
thread1.join()
thread2.join()

print("Fin des threads")
