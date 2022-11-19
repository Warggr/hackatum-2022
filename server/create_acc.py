import os
from algosdk import account, mnemonic

def create_acc():
    
    # Generate new account for this transaction
    acc = {}
    acc['sk'], acc['add'] = account.generate_account()
    print("My private key: {}".format(acc.get('sk')))
    acc['m'] = mnemonic.from_private_key(acc.get('sk'))
    print("My address: {}".format(acc.get('add')))

    return acc

# comment the following two lines if you store the account details somewhere else
acc = create_acc()
# print("private_key: " + acc.get['pk'])