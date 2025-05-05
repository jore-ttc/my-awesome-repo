class BankRecord:
    """Base class for bank database records."""
    
    def __init__(self, record_id=None):
        """Initialize a new record.
        
        Args:
            record_id: Unique identifier for this record
        """
        self.id = record_id
    
    def to_dict(self):
        """Convert the record to a dictionary representation."""
        raise NotImplementedError("Subclasses must implement to_dict()")
    
    def __str__(self):
        """String representation of the record."""
        return f"{self.__class__.__name__}(id={self.id})"


class User(BankRecord):
    """User record representing a bank customer."""
    
    def __init__(self, user_id=None, name=None, email=None, address=None):
        """Initialize a new user.
        
        Args:
            user_id: Unique identifier for this user
            name: User's full name
            email: User's email address
            address: User's physical address
        """
        super().__init__(user_id)
        self.name = name
        self.email = email
        self.address = address
    
    def to_dict(self):
        """Convert the user to a dictionary representation."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "address": self.address
        }
    
    def __str__(self):
        """String representation of the user."""
        return f"User(id={self.id}, name={self.name}, email={self.email})"


class Account(BankRecord):
    """Account record representing a bank account."""
    
    def __init__(self, account_id=None, user_id=None, account_type=None, balance=0.0):
        """Initialize a new account.
        
        Args:
            account_id: Unique identifier for this account
            user_id: ID of the user who owns this account
            account_type: Type of account (checking, savings, etc.)
            balance: Current account balance
        """
        super().__init__(account_id)
        self.user_id = user_id
        self.account_type = account_type
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money into the account.
        
        Args:
            amount: Amount to deposit
            
        Returns:
            New balance
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        """Withdraw money from the account.
        
        Args:
            amount: Amount to withdraw
            
        Returns:
            New balance
            
        Raises:
            ValueError: If amount is negative or greater than balance
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance
    
    def to_dict(self):
        """Convert the account to a dictionary representation."""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "account_type": self.account_type,
            "balance": self.balance
        }
    
    def __str__(self):
        """String representation of the account."""
        return f"Account(id={self.id}, user_id={self.user_id}, type={self.account_type}, balance=${self.balance:.2f})"