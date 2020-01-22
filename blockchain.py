# importing library
from decimal import *


# creating a variable to hold our blockchain
blockchain = [[0]]

# adding value/transaction to the chain
def add_value(_amount):
    """ adds :_amount: to the our blockchain. """
    blockchain.append([get_last_blockchain_value(), _amount])

# retreiving value from the chain
def get_last_blockchain_value():
    return blockchain[-1]

# getting the user input
def get_user_input():
    user_input = input('Enter a transaction:')
    return Decimal(user_input)


add_value(get_user_input())
add_value(get_user_input())
add_value(get_user_input())

print(blockchain)