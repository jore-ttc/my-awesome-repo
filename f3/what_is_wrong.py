# This file contains several bugs that need to be fixed
# Try asking Copilot to help you identify and fix them!


# Example 1: Function to validate a password
def validate_password(password):
    # Should check for:
    # - Minimum length of 8 characters
    # - At least one uppercase letter
    # - At least one number
    # - At least one special character
    if len(password) >= 8:
        if password.lower() != password:
            if any(c.isdigit() for c in password):
                return True
    return False

# Example 2: Class to manage a bank account
class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
    
    def deposit(amount):
        balance += amount
    
    def withdraw(amount):
        balance -= amount



# Example 3: Class to represent a rectangle
class Rectangle:
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    

R = Rectangle()
area = R.area()
perimeter = R.perimeter()


# Example 4: Function to find the maximum value in a list
def remove_duplicates(items):
    result = []
    for i in range(len(items)):
        if items[i] not in result:
            result.append(items[i])
    return result
