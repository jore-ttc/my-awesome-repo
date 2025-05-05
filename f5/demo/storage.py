from .record import User, Account

class BankStorage:
    """Base storage class for bank database."""
    
    def __init__(self):
        """Initialize a new storage instance."""
        pass
    
    def save_user(self, user):
        """Save a user record."""
        raise NotImplementedError("Subclasses must implement save_user()")
    
    def get_user(self, user_id):
        """Get a user by ID."""
        raise NotImplementedError("Subclasses must implement get_user()")
    
    def delete_user(self, user_id):
        """Delete a user by ID."""
        raise NotImplementedError("Subclasses must implement delete_user()")
    
    def get_all_users(self):
        """Get all users."""
        raise NotImplementedError("Subclasses must implement get_all_users()")
    
    def save_account(self, account):
        """Save an account record."""
        raise NotImplementedError("Subclasses must implement save_account()")
    
    def get_account(self, account_id):
        """Get an account by ID."""
        raise NotImplementedError("Subclasses must implement get_account()")
    
    def delete_account(self, account_id):
        """Delete an account by ID."""
        raise NotImplementedError("Subclasses must implement delete_account()")
    
    def get_all_accounts(self):
        """Get all accounts."""
        raise NotImplementedError("Subclasses must implement get_all_accounts()")
    
    def get_user_accounts(self, user_id):
        """Get all accounts for a user."""
        raise NotImplementedError("Subclasses must implement get_user_accounts()")


class MemoryStorage(BankStorage):
    """In-memory implementation of the BankStorage interface."""
    
    def __init__(self):
        """Initialize a new memory storage instance."""
        super().__init__()
        self._users = {}  # user_id -> User
        self._accounts = {}  # account_id -> Account
        self._next_user_id = 1
        self._next_account_id = 1
    
    def save_user(self, user):
        """Save a user to memory storage."""
        if user.id is None:
            user.id = str(self._next_user_id)
            self._next_user_id += 1
        
        self._users[user.id] = user
        return user
    
    def get_user(self, user_id):
        """Get a user from memory storage."""
        return self._users.get(user_id)
    
    def delete_user(self, user_id):
        """Delete a user from memory storage."""
        if user_id in self._users:
            del self._users[user_id]
            # Also delete all associated accounts
            account_ids = [
                acc_id for acc_id, acc in self._accounts.items() 
                if acc.user_id == user_id
            ]
            for acc_id in account_ids:
                del self._accounts[acc_id]
            return True
        return False
    
    def get_all_users(self):
        """Get all users from memory storage."""
        return list(self._users.values())
    
    def save_account(self, account):
        """Save an account to memory storage."""
        if account.id is None:
            account.id = str(self._next_account_id)
            self._next_account_id += 1
        
        self._accounts[account.id] = account
        return account
    
    def get_account(self, account_id):
        """Get an account from memory storage."""
        return self._accounts.get(account_id)
    
    def delete_account(self, account_id):
        """Delete an account from memory storage."""
        if account_id in self._accounts:
            del self._accounts[account_id]
            return True
        return False
    
    def get_all_accounts(self):
        """Get all accounts from memory storage."""
        return list(self._accounts.values())
    
    def get_user_accounts(self, user_id):
        """Get all accounts for a specific user."""
        return [acc for acc in self._accounts.values() if acc.user_id == user_id]