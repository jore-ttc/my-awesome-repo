from .record import User, Account
from .storage import BankStorage, MemoryStorage

class BankDatabase:
    """Main bank database class for managing users and accounts."""
    
    def __init__(self, name="MyBank", storage=None):
        """Initialize a new bank database.
        
        Args:
            name: Name of this bank
            storage: BankStorage backend to use, defaults to MemoryStorage
        """
        self.name = name
        # Ensure we're using a BankStorage instance
        if storage is not None and not isinstance(storage, BankStorage):
            raise TypeError("Storage must be an instance of BankStorage")
        self.storage = storage or MemoryStorage()
    
    # User operations
    
    def create_user(self, name, email, address=None):
        """Create a new bank user.
        
        Args:
            name: User's full name
            email: User's email address
            address: User's physical address
            
        Returns:
            The created user
        """
        user = User(name=name, email=email, address=address)
        return self.storage.save_user(user)
    
    def get_user(self, user_id):
        """Get a user by ID.
        
        Args:
            user_id: The ID of the user to get
            
        Returns:
            The user if found, None otherwise
        """
        return self.storage.get_user(user_id)
    
    def update_user(self, user_id, name=None, email=None, address=None):
        """Update a user's information.
        
        Args:
            user_id: The ID of the user to update
            name: New name (optional)
            email: New email (optional)
            address: New address (optional)
            
        Returns:
            The updated user if found, None otherwise
        """
        user = self.storage.get_user(user_id)
        if not user:
            return None
            
        if name is not None:
            user.name = name
        if email is not None:
            user.email = email
        if address is not None:
            user.address = address
            
        return self.storage.save_user(user)
    
    def delete_user(self, user_id):
        """Delete a user and all their accounts.
        
        Args:
            user_id: The ID of the user to delete
            
        Returns:
            True if the user was deleted, False otherwise
        """
        return self.storage.delete_user(user_id)
    
    def get_all_users(self):
        """Get all users in the database.
        
        Returns:
            List of all users
        """
        return self.storage.get_all_users()
    
    # Account operations
    
    def create_account(self, user_id, account_type, initial_balance=0.0):
        """Create a new bank account for a user.
        
        Args:
            user_id: ID of the user who owns this account
            account_type: Type of account (checking, savings, etc.)
            initial_balance: Initial account balance
            
        Returns:
            The created account
            
        Raises:
            ValueError: If the user doesn't exist
        """
        user = self.storage.get_user(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found")
            
        account = Account(
            user_id=user_id, 
            account_type=account_type, 
            balance=initial_balance
        )
        return self.storage.save_account(account)
    
    def get_account(self, account_id):
        """Get an account by ID.
        
        Args:
            account_id: The ID of the account to get
            
        Returns:
            The account if found, None otherwise
        """
        return self.storage.get_account(account_id)
    
    def delete_account(self, account_id):
        """Delete an account by ID.
        
        Args:
            account_id: The ID of the account to delete
            
        Returns:
            True if the account was deleted, False otherwise
        """
        return self.storage.delete_account(account_id)
    
    def get_user_accounts(self, user_id):
        """Get all accounts for a specific user.
        
        Args:
            user_id: The ID of the user
            
        Returns:
            List of user's accounts
        """
        return self.storage.get_user_accounts(user_id)
    
    # Banking operations
    
    def deposit(self, account_id, amount):
        """Deposit money into an account.
        
        Args:
            account_id: ID of the account
            amount: Amount to deposit
            
        Returns:
            The new balance
            
        Raises:
            ValueError: If the account doesn't exist or amount is invalid
        """
        account = self.storage.get_account(account_id)
        if not account:
            raise ValueError(f"Account with ID {account_id} not found")
            
        account.deposit(amount)
        self.storage.save_account(account)
        return account.balance
    
    def withdraw(self, account_id, amount):
        """Withdraw money from an account.
        
        Args:
            account_id: ID of the account
            amount: Amount to withdraw
            
        Returns:
            The new balance
            
        Raises:
            ValueError: If the account doesn't exist, amount is invalid or insufficient funds
        """
        account = self.storage.get_account(account_id)
        if not account:
            raise ValueError(f"Account with ID {account_id} not found")
            
        account.withdraw(amount)
        self.storage.save_account(account)
        return account.balance
    
    def transfer(self, from_account_id, to_account_id, amount):
        """Transfer money between accounts.
        
        Args:
            from_account_id: ID of the source account
            to_account_id: ID of the destination account
            amount: Amount to transfer
            
        Returns:
            A tuple of (from_balance, to_balance)
            
        Raises:
            ValueError: If accounts don't exist, amount is invalid or insufficient funds
        """
        from_account = self.storage.get_account(from_account_id)
        to_account = self.storage.get_account(to_account_id)
        
        if not from_account:
            raise ValueError(f"Source account with ID {from_account_id} not found")
        if not to_account:
            raise ValueError(f"Destination account with ID {to_account_id} not found")
            
        # Withdraw from source account
        from_account.withdraw(amount)
        
        # Deposit to destination account
        to_account.deposit(amount)
        
        # Save both accounts
        self.storage.save_account(from_account)
        self.storage.save_account(to_account)
        
        return (from_account.balance, to_account.balance)
    
    def get_account_balance(self, account_id):
        """Get the current balance of an account.
        
        Args:
            account_id: ID of the account
            
        Returns:
            The current balance
            
        Raises:
            ValueError: If the account doesn't exist
        """
        account = self.storage.get_account(account_id)
        if not account:
            raise ValueError(f"Account with ID {account_id} not found")
            
        return account.balance