class Index:
    """Class for indexing database records by specific fields."""
    
    def __init__(self, field):
        """Initialize a new index for a specific field.
        
        Args:
            field: The field name to index on
        """
        self.field = field
        self._index = {}  # Maps field values to sets of record IDs
    
    def add(self, record):
        """Add a record to the index."""
        if not record or not record.id:
            return False
            
        # Get the value to index on
        value = record.get(self.field)
        
        # Skip if the record doesn't have the field
        if value is None:
            return False
            
        # Make sure the value is hashable
        if not isinstance(value, (str, int, float, bool, tuple)):
            value = str(value)
            
        # Add the record ID to the index
        if value not in self._index:
            self._index[value] = set()
        self._index[value].add(record.id)
        return True
    
    def remove(self, record):
        """Remove a record from the index."""
        if not record or not record.id:
            return False
            
        # Get the value to index on
        value = record.get(self.field)
        
        # Skip if the record doesn't have the field
        if value is None:
            return False
            
        # Make sure the value is hashable
        if not isinstance(value, (str, int, float, bool, tuple)):
            value = str(value)
            
        # Remove the record ID from the index
        if value in self._index and record.id in self._index[value]:
            self._index[value].remove(record.id)
            if not self._index[value]:  # Clean up empty sets
                del self._index[value]
            return True
        return False
    
    def find(self, value):
        """Find all record IDs with the given field value."""
        if not isinstance(value, (str, int, float, bool, tuple)):
            value = str(value)
            
        return self._index.get(value, set())
    
    def update(self, record, old_value=None):
        """Update the index for a record."""
        # If old value is provided, remove it first
        if old_value is not None:
            if not isinstance(old_value, (str, int, float, bool, tuple)):
                old_value = str(old_value)
                
            if old_value in self._index and record.id in self._index[old_value]:
                self._index[old_value].remove(record.id)
                if not self._index[old_value]:  # Clean up empty sets
                    del self._index[old_value]
                    
        # Add the record with its new value
        return self.add(record)
    
    def clear(self):
        """Clear the index."""
        self._index = {}
        
    def values(self):
        """Get all unique values in this index."""
        return list(self._index.keys())

class BankIndex:
    """Class for indexing bank users and accounts by specific fields."""
    
    def __init__(self, field):
        """Initialize a new index for a specific field.
        
        Args:
            field: The field name to index on
        """
        self.field = field
        self._index = {}  # Maps field values to sets of record IDs
    
    def add_user(self, user):
        """Add a user to the index.
        
        Args:
            user: The user to index
            
        Returns:
            True if indexed, False otherwise
        """
        if not user or not user.id:
            return False
            
        # Get the value to index on
        value = None
        if self.field == "email":
            value = user.email
        elif self.field == "name":
            value = user.name
        elif hasattr(user, self.field):
            value = getattr(user, self.field)
            
        # Skip if the user doesn't have the field or it's None
        if value is None:
            return False
            
        # Make sure the value is hashable
        if not isinstance(value, (str, int, float, bool, tuple)):
            value = str(value)
            
        # Add the user ID to the index
        if value not in self._index:
            self._index[value] = set()
        self._index[value].add(user.id)
        return True
    
    def add_account(self, account):
        """Add an account to the index.
        
        Args:
            account: The account to index
            
        Returns:
            True if indexed, False otherwise
        """
        if not account or not account.id:
            return False
            
        # Get the value to index on
        value = None
        if self.field == "user_id":
            value = account.user_id
        elif self.field == "account_type":
            value = account.account_type
        elif hasattr(account, self.field):
            value = getattr(account, self.field)
            
        # Skip if the account doesn't have the field or it's None
        if value is None:
            return False
            
        # Make sure the value is hashable
        if not isinstance(value, (str, int, float, bool, tuple)):
            value = str(value)
            
        # Add the account ID to the index
        if value not in self._index:
            self._index[value] = set()
        self._index[value].add(account.id)
        return True
    
    def find(self, value):
        """Find all record IDs with the given field value.
        
        Args:
            value: The value to search for
            
        Returns:
            A set of record IDs matching the value
        """
        if value is None:
            return set()
            
        if not isinstance(value, (str, int, float, bool, tuple)):
            value = str(value)
            
        return self._index.get(value, set())
    
    def remove(self, record_id, value):
        """Remove a record from the index.
        
        Args:
            record_id: The ID of the record to remove
            value: The value to remove it from
            
        Returns:
            True if removed, False otherwise
        """
        if value is None or record_id is None:
            return False
            
        if not isinstance(value, (str, int, float, bool, tuple)):
            value = str(value)
            
        if value in self._index and record_id in self._index[value]:
            self._index[value].remove(record_id)
            if not self._index[value]:  # Clean up empty sets
                del self._index[value]
            return True
        return False
    
    def clear(self):
        """Clear the index."""
        self._index = {}
        
    def values(self):
        """Get all unique values in this index."""
        return list(self._index.keys())