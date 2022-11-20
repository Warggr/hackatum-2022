import os
from algosdk.v2client import algod

BLOCKCHAIN = os.environ['BLOCKCHAIN'] if "BLOCKCHAIN" in os.environ else "localhost"
algod_address = "http://" + BLOCKCHAIN + ":4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algod_client = algod.AlgodClient(algod_token, algod_address)
