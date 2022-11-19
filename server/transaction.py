import create_acc
import create_certificate
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

  student = create_acc
  uni = create_acc
  f = open("./TUM-certificate.json", "r")
  asset_Id = create_certificate(uni.get('pk'), f, "./TUM-certificate.json")
  transferAssets(algod_client, uni, student, asset_Id)
