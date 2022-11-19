import json
import base64
import create_acc
from algosdk import account, mnemonic, constants
from algosdk.v2client import algod
from algosdk.future import transaction



def transferAssets(algod_client, alice, bob, asset_id):
  print("--------------------------------------------")
  print("Transfering Alice's token to Bob......")
  params = algod_client.suggested_params()
  # comment these two lines if you want to use suggested params
  # params.fee = 1000
  # params.flat_fee = True
  txn = AssetTransferTxn(
      sender=alice['pk'],
      sp=params,
      receiver=bob["pk"],
      amt=100,
      index=asset_id)
  stxn = txn.sign(alice['sk'])
  txid = algod_client.send_transaction(stxn)
  print(txid)
  # Wait for the transaction to be confirmed
  confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
  print("TXID: ", txid)
  print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round']))
  # The balance should now be 10.
  #print_asset_holding(algod_client, bob['pk'], asset_id)
  transferAssets(algod_client, accounts[0], accounts[1], asset_id)
