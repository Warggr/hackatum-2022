import json
import hashlib
from algosdk.v2client import algod
from algosdk.future.transaction import AssetConfigTxn, wait_for_confirmation

# issuer is a directory ['pk'] needed! -> but can be changed since only the private key is used
def create_certificate(issuer, file, url_path):

    #normal algod client config for local blockchain
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)


    print("--------------------------------------------")
    print("Creating Asset...")
    # CREATE ASSET
    # Get network params for transactions before every transaction.
    params = algod_client.suggested_params()
    # comment these two lines if you want to use suggested params
    # params.fee = 1000
    # params.flat_fee = True

    hash = hashlib.new("sha512_256")
    hash.update(b"arc0003/amj")
    hash.update(file.encode("utf-8"))
    file_metadata_hash = hash.digest()

    txn = AssetConfigTxn(
      sender=issuer['pk'],
      sp=params,
      total=1000,
      default_frozen=False,
      asset_name="Certificate",
      reserve=issuer['pk'],
      freeze=issuer['pk'],
      clawback=issuer['pk'],
      url= url_path,
      metadata_hash=file_metadata_hash,
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