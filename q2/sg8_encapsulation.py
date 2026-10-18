class BankAccount:
    
#A class as a bank account.

    def __init__(self, account_number: str, initial_balance: float = 0.0):
        
#Initializes the object (Bank account) with an account number and balance.

        self.__account_number = account_number
        
        if initial_balance < 0:
            raise ValueError("The balance must not be a negative number.")
        self.__balance = float(initial_balance)

# - Account number methods -

    def get_account_number(self) -> str:
      
#Gets and returns the unique account number
        
        return self.__account_number

    def set_account_number(self, account_number: str) -> None:
        
#Sets and checks account number for value errors

        if not account_number or not str(account_number).strip():
            raise ValueError("Account number must not be empty.")
        self.__account_number = str(account_number).strip()
        

# - Balance methods -

    def get_balance(self) -> float:

#Gets and returns the balance
        
        return self.__balance

    def set_balance(self, amount: float) -> None:
        
#Sets and checks account number for value errors
        
        if amount < 0:
            raise ValueError("Account balance must not be negative.")
        self.__balance = float(amount)
