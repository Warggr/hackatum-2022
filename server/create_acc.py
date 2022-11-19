import os
from algosdk import account, mnemonic

def create_acc():
    
    # Generate new account for this transaction
    acc = {}
    acc['pk'], acc['add'] = account.generate_account()
    print("My private key: {}".format(acc.get('pk')))
    acc['m'] = mnemonic.from_private_key(acc.get('pk'))
    print("My address: {}".format(acc.get('add')))

    return acc

# comment the following two lines if you store the account details somewhere else
acc = create_acc()
# print("private_key: " + acc.get['pk'])