from create_acc import *
from create_certificate import *
from fund_acc import *
from algosdk.v2client import algod
from algosdk.future.transaction import AssetTransferTxn, wait_for_confirmation, AssetConfigTxn, PaymentTxn

def optIn(receiver, asset_id):

  algod_address = "http://localhost:4001"
  algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  algod_client = algod.AlgodClient(algod_token, algod_address)

  print("--------------------------------------------")
  print("Opt-in to accept token......")
  # Check if asset_id is in Bob's asset holdings prior
  # to opt-in
  params = algod_client.suggested_params()
  # comment these two lines if you want to use suggested params
  # params.fee = 1000
  # params.flat_fee = True

  account_info = algod_client.account_info(receiver['pk'])
  holding = None
  idx = 0
  for my_account_info in account_info['assets']:
      scrutinized_asset = account_info['assets'][idx]
      idx = idx + 1    
      if (scrutinized_asset['asset-id'] == asset_id):
          holding = True
          break

  if not holding:
    # Use the AssetTransferTxn class to transfer assets and opt-in
    txn = AssetTransferTxn(
        sender=receiver['pk'],
        sp=params,
        receiver=receiver["pk"],
        amt=0,
        index=asset_id)
    stxn = txn.sign(receiver['sk'])
    txid = algod_client.send_transaction(stxn)
    print(txid)
    # Wait for the transaction to be confirmed
    confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
    print("TXID: ", txid)
    print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round']))
    # Now check the asset holding for that account.
    # This should now show a holding with a balance of 0.
    # print_asset_holding(algod_client, receiver['pk'], asset_id)

def transferAssets(alice, bob, asset_id):

  algod_address = "http://localhost:4001"
  algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  algod_client = algod.AlgodClient(algod_token, algod_address)

  print("--------------------------------------------")
  print("Transfering Alice's token to Bob......")

  print("Client created\n\n")

  params = algod_client.suggested_params()
  # comment these two lines if you want to use suggested params
  # params.fee = 1000
  # params.flat_fee = True
  txn = AssetTransferTxn(
      sender=alice['pk'],
      sp=params,
      receiver=bob["pk"],
      amt=1000,
      index=asset_id)
  stxn = txn.sign(alice['sk'])
  print("Transaction signed")
  txid = algod_client.send_transaction(stxn)
  print("trans sent")
  print(txid)
  # Wait for the transaction to be confirmed
  confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
  print("TXID: ", txid)
  print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round']))
  # The balance should now be 10.
  #print_asset_holding(algod_client, bob['pk'], asset_id)