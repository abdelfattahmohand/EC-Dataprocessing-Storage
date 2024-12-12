class InMemoryDB:
    def __init__(self):
        self.committed_store = {}
        self.in_progress_store = None
        self.in_transaction = False

    def begin_transaction(self):
        if self.in_transaction:
            raise Exception("Transaction already in progress")
        self.in_progress_store = {}
        self.in_transaction = True

    def put(self, key, value):
        if not self.in_transaction:
            raise Exception("No transaction in progress")
        self.in_progress_store[key] = value

    def get(self, key):
        if self.in_transaction and key in self.committed_store:
            return self.committed_store[key]
        return self.committed_store.get(key, None)

    def commit(self):
        if not self.in_transaction:
            raise Exception("No transaction in progress")
        self.committed_store.update(self.in_progress_store)
        self.in_progress_store = None
        self.in_transaction = False

    def rollback(self):
        if not self.in_transaction:
            raise Exception("No transaction in progress")
        self.in_progress_store = None
        self.in_transaction = False

def main():
    db = InMemoryDB()

    print(db.get("A"))  # Prints None, A doesnt exist
    try:
        db.put("A", 5)  # Should raise an exception, no transaction in progress
    except Exception as e:
        print(f"Error: {e}")

    db.begin_transaction()  # Start new transaction
    db.put("A", 5)  # Set key A to 5, not yet committed
    print(db.get("A"))  # Should print None

    db.put("A", 6)  # Update key A to 6
    db.commit()  # Commit transaction
    print(db.get("A"))  # Should print 6

    try:
        db.commit()  # Should raise an exception, no transaction in progress
    except Exception as e:
        print(f"Error: {e}")
    
    try:
        db.rollback()  # Should raise an exception, no transaction in progress
    except Exception as e:
        print(f"Error: {e}")
    
    print(db.get("B"))  # Should print none, B doesnt exist

    db.begin_transaction()  # Start new transaction
    db.put("B", 10)  # Set key B to 10, not yet committed
    db.rollback() # Clear in progress store changes, B should not be 10

    print(db.get("B"))  # Should print None, B was never committed
    
if __name__ == "__main__":
    main()