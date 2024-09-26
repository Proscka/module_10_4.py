from threading import Thread
from random import randint
import time
from queue import Queue
class Table:
    def __init__(self,number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(randint(3,10))

class Cafe:
    def __init__(self,*tables):
        self.queue = Queue()
        self.tables = tables
    def guest_arrival(self,*guests):
        for guest in guests:
            table = self.find_free_table()
            if table:
                table.guest = guest
                guest.start()
                print(f"{guest.name} сел за стол номер {table.number}")
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очередь")
    def discuss_guests(self):
        while not self.queue.empty() or self.any_guest_still_seated():
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал и ушёл")
                    print(f"Стол номер{table.number} свободен")
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    next_guest = self.queue.get()
                    table.quest = next_guest
                    next_guest.start()
                    print(f"{next_guest.name} вышел из очереди и сел за стол номер{table.number}")

    def find_free_table(self):
        for table in self.tables:
            if table.guest is None:
                return table
        return None

    def any_guest_still_seated(self):
        return any(table.guest is not None for table in self.tables)

tables = [Table(number)for number in range(1,6)]
guests_names = ["Maria","Oleg","Vakhtang","Sergey","Darya","Arman","Viktoria","Nikita","Galina","Pavel","IIya","Alexandr"]
guests =[Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()





