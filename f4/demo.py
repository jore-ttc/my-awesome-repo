class SimpleDatabase:
    def __init__(self):
        self.data = {}

    def insert(self, key, value):
        """Insert a key-value pair into the database"""
        self.data[key] = value

    def get(self, key):
        """Retrieve a value by key"""
        return self.data.get(key, None)

    def delete(self, key):
        """Delete a key-value pair from the database"""
        if key in self.data:
            del self.data[key]
            return True
        return False

    def update(self, key, value):
        """Update value for existing key"""
        if key in self.data:
            self.data[key] = value
            return True
        return False

    def list_all(self):
        """Return all items in the database"""
        return self.data.items()

# Example usage
if __name__ == "__main__":
    db = SimpleDatabase()
    db.insert("user1", {"name": "John", "age": 30})
    db.insert("user2", {"name": "Alice", "age": 25})
    
    print(db.get("user1"))  # Get user data
    db.update("user1", {"name": "John", "age": 31})  # Update user
    db.delete("user2")  # Delete user