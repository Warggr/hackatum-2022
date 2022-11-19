import os
from algosdk import account, mnemonic
from algosdk.v2client import algod
from algosdk import kmd
from algosdk.wallet import Wallet


def create_student():
    
    # Generate new account for this transaction
    student = {}
    student['pk'], student['add'] = account.generate_account()
    print("My private key: {}".format(student.get('pk')))
    student['m'] = mnemonic.from_private_key(student.get('pk'))
    print("My address: {}".format(student.get('add')))

    return student

student = create_student()
