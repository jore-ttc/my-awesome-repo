from .record import User, Account

class Query:
    """Class for building and executing queries against the database."""
    
    def __init__(self, database):
        """Initialize a new query for the given database.
        
        Args:
            database: The database to query
        """
        self.database = database
        self.conditions = []
        self.sort_field = None
        self.sort_reverse = False
        self.limit_value = None
        self.skip_value = 0
    
    def filter(self, field, operator, value):
        """Add a filter condition to the query.
        
        Args:
            field: The field to filter on
            operator: The operator to use (e.g., "=", ">", "<", "!=", "in", "contains")
            value: The value to compare against
        
        Returns:
            self for method chaining
        """
        self.conditions.append((field, operator, value))
        return self
    
    def sort(self, field, reverse=False):
        """Add a sort condition to the query.
        
        Args:
            field: The field to sort on
            reverse: If True, sort in descending order
            
        Returns:
            self for method chaining
        """
        self.sort_field = field
        self.sort_reverse = reverse
        return self
    
    def limit(self, limit_value):
        """Limit the number of results.
        
        Args:
            limit_value: Maximum number of results to return
            
        Returns:
            self for method chaining
        """
        self.limit_value = limit_value
        return self
    
    def skip(self, skip_value):
        """Skip a number of results.
        
        Args:
            skip_value: Number of results to skip
            
        Returns:
            self for method chaining
        """
        self.skip_value = skip_value
        return self
    
    def _matches_conditions(self, record):
        """Check if a record matches all conditions."""
        if not self.conditions:
            return True
            
        for field, operator, value in self.conditions:
            record_value = record.get(field)
            
            if operator == "=":
                if record_value != value:
                    return False
            elif operator == ">":
                if not (record_value and record_value > value):
                    return False
            elif operator == "<":
                if not (record_value and record_value < value):
                    return False
            elif operator == "!=":
                if record_value == value:
                    return False
            elif operator == "in":
                if record_value not in value:
                    return False
            elif operator == "contains":
                if not (record_value and value in record_value):
                    return False
            elif operator == "starts_with":
                if not (isinstance(record_value, str) and record_value.startswith(value)):
                    return False
            elif operator == "ends_with":
                if not (isinstance(record_value, str) and record_value.endswith(value)):
                    return False
        
        return True
    
    def execute(self):
        """Execute the query and return matching records."""
        # Try to use an index if available
        results = []
        
        # If no index is available or useful, scan all records
        for record in self.database.get_all_records():
            if self._matches_conditions(record):
                results.append(record)
        
        # Apply sorting if specified
        if self.sort_field:
            results.sort(
                key=lambda r: r.get(self.sort_field) or "", 
                reverse=self.sort_reverse
            )
        
        # Apply skip and limit
        if self.skip_value:
            results = results[self.skip_value:]
            
        if self.limit_value and len(results) > self.limit_value:
            results = results[:self.limit_value]
            
        return results
    
    def count(self):
        """Count the number of matching records."""
        return len(self.execute())
    
    def first(self):
        """Get the first matching record.""" 
        results = self.execute()
        return results[0] if results else None


class BankQuery:
    """Class for building and executing queries against the bank database."""
    
    def __init__(self, database):
        """Initialize a new query for the given database.
        
        Args:
            database: The bank database to query
        """
        self.database = database
        self._type = None  # "user" or "account"
        self.conditions = []
        self.sort_field = None
        self.sort_reverse = False
        
    def users(self):
        """Query for users.
        
        Returns:
            self for method chaining
        """
        self._type = "user"
        return self
    
    def accounts(self):
        """Query for accounts.
        
        Returns:
            self for method chaining
        """
        self._type = "account"
        return self
    
    def filter_name(self, name):
        """Filter users by name.
        
        Args:
            name: Name to filter by (case-insensitive contains)
            
        Returns:
            self for method chaining
        """
        if self._type != "user":
            self._type = "user"  # Default to users if not specified
        self.conditions.append(("name", "contains", name.lower()))
        return self
    
    def filter_email(self, email):
        """Filter users by exact email.
        
        Args:
            email: Email to filter by
            
        Returns:
            self for method chaining
        """
        if self._type != "user":
            self._type = "user"  # Default to users if not specified
        self.conditions.append(("email", "=", email))
        return self
    
    def filter_user_id(self, user_id):
        """Filter accounts by user ID.
        
        Args:
            user_id: User ID to filter by
            
        Returns:
            self for method chaining
        """
        if self._type != "account":
            self._type = "account"  # Default to accounts
        self.conditions.append(("user_id", "=", user_id))
        return self
    
    def filter_account_type(self, account_type):
        """Filter accounts by type.
        
        Args:
            account_type: Account type to filter by
            
        Returns:
            self for method chaining
        """
        if self._type != "account":
            self._type = "account"  # Default to accounts
        self.conditions.append(("account_type", "=", account_type))
        return self
    
    def filter_min_balance(self, min_balance):
        """Filter accounts by minimum balance.
        
        Args:
            min_balance: Minimum balance to filter by
            
        Returns:
            self for method chaining
        """
        if self._type != "account":
            self._type = "account"  # Default to accounts
        self.conditions.append(("balance", ">=", min_balance))
        return self
    
    def filter_max_balance(self, max_balance):
        """Filter accounts by maximum balance.
        
        Args:
            max_balance: Maximum balance to filter by
            
        Returns:
            self for method chaining
        """
        if self._type != "account":
            self._type = "account"  # Default to accounts
        self.conditions.append(("balance", "<=", max_balance))
        return self
    
    def sort_by(self, field, reverse=False):
        """Sort the results by a field.
        
        Args:
            field: Field to sort by
            reverse: If True, sort in descending order
            
        Returns:
            self for method chaining
        """
        self.sort_field = field
        self.sort_reverse = reverse
        return self
    
    def _matches_conditions(self, record):
        """Check if a record matches all conditions."""
        for field, operator, value in self.conditions:
            # Get the record value
            record_value = None
            
            if hasattr(record, field):
                record_value = getattr(record, field)
            
            # Apply the condition
            if operator == "=":
                if record_value != value:
                    return False
            elif operator == ">":
                if not (record_value and record_value > value):
                    return False
            elif operator == "<":
                if not (record_value and record_value < value):
                    return False
            elif operator == ">=":
                if not (record_value and record_value >= value):
                    return False
            elif operator == "<=":
                if not (record_value and record_value <= value):
                    return False
            elif operator == "!=":
                if record_value == value:
                    return False
            elif operator == "contains":
                # Case-insensitive contains
                if not (record_value and isinstance(record_value, str) and 
                        value.lower() in record_value.lower()):
                    return False
        
        return True
    
    def execute(self):
        """Execute the query and return matching records.
        
        Returns:
            List of matching users or accounts
            
        Raises:
            ValueError: If no query type is specified
        """
        if not self._type:
            raise ValueError("Query type not specified. Call users() or accounts() first.")
        
        # Get all records of the requested type
        if self._type == "user":
            records = self.database.get_all_users()
        else:  # account
            records = []
            for user in self.database.get_all_users():
                records.extend(self.database.get_user_accounts(user.id))
        
        # Filter by conditions
        results = []
        for record in records:
            if self._matches_conditions(record):
                results.append(record)
        
        # Apply sorting
        if self.sort_field:
            results.sort(
                key=lambda r: getattr(r, self.sort_field) if hasattr(r, self.sort_field) else None, 
                reverse=self.sort_reverse
            )
            
        return results
    
    def count(self):
        """Count the number of matching records.
        
        Returns:
            Number of matching records
        """
        return len(self.execute())
    
    def first(self):
        """Get the first matching record.
        
        Returns:
            First matching record or None if no matches
        """
        results = self.execute()
        return results[0] if results else None