# hackatum-2022

# Usage

- Get the [Algorand sandbox](https://github.com/algorand/sandbox) running
- Pick one account with at least 1000 microalgos from `./sandbox goal account list`
    - Export the private key of that account as a mnemonic with `./sandbox goal account export --address ${ACCOUNT_ID}`
    - Copy both the resulting mnemonic (25 words) and the account ID to [server/create\_acc.py](server/create_acc.py)
