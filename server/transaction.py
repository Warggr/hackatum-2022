from create_acc import *
from create_certificate import *
from algosdk.v2client import algod
from algosdk.future.transaction import AssetTransferTxn, wait_for_confirmation



def transferAssets(algod_client, sender, receiver, asset_id):
  print("--------------------------------------------")
  print("Transfering Alice's token to Bob......")
  params = algod_client.suggested_params()
  # comment these two lines if you want to use suggested params
  # params.fee = 1000
  # params.flat_fee = True
  txn = AssetTransferTxn(
      sender=sender['pk'],
      sp=params,
      receiver=receiver["pk"],
      amt=100,
      index=asset_id)
  stxn = txn.sign(sender['sk'])
  txid = algod_client.send_transaction(stxn)
  print(txid)
  # Wait for the transaction to be confirmed
  confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
  print("TXID: ", txid)
  print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round']))
  # The balance should now be 10.
  #print_asset_holding(algod_client, bob['pk'], asset_id)

print("Starting transaction")
algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algod_client = algod.AlgodClient(algod_token, algod_address)
student = create_acc()
uni = create_acc()
f = open("./server/TUM-certificate.json", "r")
asset_Id = create_certificate(uni, f, "./server/TUM-certificate.json")
transferAssets(algod_client, uni, student, asset_Id)