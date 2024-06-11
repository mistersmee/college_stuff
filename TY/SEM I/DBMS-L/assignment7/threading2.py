import threading

class Database:
    def __init__(self):
        self.data = {}
        self.locks = {}  # Locks for each data item

    def read(self, transaction_id, item):
        if item not in self.data:
            print(f"Transaction {transaction_id} is reading item {item}: Item not found")
            return None

        with self.locks.get(item, threading.Lock()):
            print(f"Transaction {transaction_id} is reading item {item}: {self.data[item]}")

    def write(self, transaction_id, item, value):
        with self.locks.get(item, threading.Lock()):
            self.data[item] = value
            print(f"Transaction {transaction_id} is writing item {item}: {value}")

def transaction(transaction_id, database):
    item = 'A'

    # Simulate a read operation
    database.read(transaction_id, item)

    # Simulate a write operation
    value = transaction_id * 10
    database.write(transaction_id, item, value)

if __name__ == "__main__":
    db = Database()
    num_transactions = 5

    threads = [threading.Thread(target=transaction, args=(i, db)) for i in range(num_transactions)]

    # Add transaction B
    thread_b = threading.Thread(target=transaction, args=('B', db))
    threads.append(thread_b)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
