from web3 import Web3

RPC_ENDPOINT="<YOUR_RPC_ENDPOINT_HERE>"

web3 = Web3(Web3.HTTPProvider(RPC_ENDPOINT))

print(f"ChainID: {hex(web3.eth.chainId)}")

block_latest = web3.eth.get_block(hex(16152249))
print(block_latest)

print(f"Latest block number: {block_latest['number']}")
print(f"Transaction count: {len(block_latest['transactions'])}")

transaction = web3.eth.get_transaction(block_latest["transactions"][0])
print(transaction)

address_to = transaction["to"]
address_from = transaction["from"]

balance_to = web3.fromWei(web3.eth.get_balance(address_to), "ether")
balance_from = web3.fromWei(web3.eth.get_balance(address_from), "ether")

print(f"Balance of {address_to} ('to' address) is {balance_to}")
print(f"Balance of {address_from} ('from' address) is {balance_from}")

