import os
from algosdk import account, mnemonic

def create_acc():
    
    print("Creating acc\n\n")
    # Generate new account for this transaction
    acc = {}
    acc['sk'], acc['add'] = account.generate_account()
    print("My private key: {}".format(acc.get('sk')))
    acc['m'] = mnemonic.from_private_key(acc.get('sk'))
    print("My address: {}".format(acc.get('add')))
    acc['pk'] = mnemonic.to_public_key(acc.get('m'))

    return acc

if __name__ == "__main__":
    # comment the following two lines if you store the account details somewhere else
    acc = create_acc()
    print("private_key: " + acc.get['pk'])
