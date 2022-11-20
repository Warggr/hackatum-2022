import os
from algosdk import account, mnemonic
from fund_acc import fund

def create_acc():
    
    print("Creating acc\n\n")
    # Generate new account for this transaction
    acc = {}
    acc['sk'], acc['add'] = account.generate_account()
    print("My private key: {}".format(acc.get('sk')))
    acc['m'] = mnemonic.from_private_key(acc.get('sk'))
    print("My address: {}".format(acc.get('add')))
    acc['pk'] = mnemonic.to_public_key(acc.get('m'))

    private_key = mnemonic.to_private_key("witness minor police loud ability vintage cattle entire spread poverty proof rail tomato near swamp raven network future tunnel neglect advice early bundle absorb youth")
    address = "7BEIK53QNADEMME4JZ57LSPTBODQ4TRHCI7VZZLYTCMP6DECR644B7OILQ"
    fund(private_key, address, acc['add'])

    return acc