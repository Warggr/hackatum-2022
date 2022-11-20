import json
import hashlib
from config import algod_address, algod_token, algod_client
from algosdk.future.transaction import AssetConfigTxn, wait_for_confirmation

# issuer is a directory ['sk'] needed! -> but can be changed since only the private key is used
def create_certificate(issuer, f, url_path):
    print("--------------------------------------------")
    print("Creating Asset...")
    # CREATE ASSET
    # Get network params for transactions before every transaction.
    params = algod_client.suggested_params()
    # comment these two lines if you want to use suggested params
    # params.fee = 1000
    # params.flat_fee = True

    #metadataJSON = json.load(f.read())
    #metadataStr = json.dumps(metadataJSON)

    hash = hashlib.new("sha512_256")
    hash.update(b"arc0003/amj")
    hash.update(f)
    file_metadata_hash = hash.digest()

    txn = AssetConfigTxn(
      sender=issuer['pk'],
      sp=params,
      total=1000,
      default_frozen=False,
      asset_name="Certificate",
      manager=issuer['pk'],
      reserve=issuer['pk'],
      freeze=issuer['pk'],
      clawback=issuer['pk'],
      url= url_path,
      metadata_hash=file_metadata_hash,
      strict_empty_address_check=False,
      decimals=0)

    # Sign with secret key of creator
    stxn = txn.sign(issuer['sk'])

    # Send the transaction to the network and retrieve the txid.
    txid = algod_client.send_transaction(stxn)
    print("Asset Creation Transaction ID: {}".format(txid))

    # Wait for the transaction to be confirmed
    confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
    print("TXID: ", txid)
    print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round']))
    try:
        # Pull account info for the creator
        # account_info = algod_client.account_info(accounts[1]['pk'])
        # get asset_id from tx
        # Get the new asset's information from the creator account
        ptx = algod_client.pending_transaction_info(txid)
        asset_id = ptx["asset-index"]
    except Exception as e:
          print(e)
  
    return asset_id

def print_created_asset(algodclient, account, assetid):
  # note: if you have an indexer instance available it is easier to just use this
  # response = myindexer.accounts(asset_id = assetid)
  # then use 'account_info['created-assets'][0] to get info on the created asset
  account_info = algodclient.account_info(account)
  idx = 0
  for my_account_info in account_info['created-assets']:
    scrutinized_asset = account_info['created-assets'][idx]
    idx = idx + 1       
    if (scrutinized_asset['index'] == assetid):
      print("Asset ID: {}".format(scrutinized_asset['index']))
      print(json.dumps(my_account_info['params'], indent=4))
      break
