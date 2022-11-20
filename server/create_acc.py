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

    private_key = mnemonic.to_private_key("chapter congress calm absent alter rally account diet spare broccoli describe collect destroy tennis tribe reward demand jungle roof acid indicate exile marriage about address")
    address = "25EKXG3ESZVHD56DAGDE67S6K3YCUDL63EDNXTZOMQOP4GGWC4FDDYKBMY"
    fund(private_key, address, acc['add'])

    return acc