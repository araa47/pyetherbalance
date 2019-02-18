PyEtherBalance  
=============

`pyetherbalance` is a python module for getting Ethereum and er20 token balances. There are other modules like web3py out there, however the goal of this module is to be super light weight and not depend on too many other modules. 

Installation
------------

Simply clone the project and run `python setup.py install` - or install via pip `pip install pyetherbalance`.

This module only depends on the 'requests' library in python to send post requests


Basic Usage:
----


```python
import pyetherbalance 
# Sign up for https://infura.io/, and get the url to an ethereum node
infura_url = 'https://mainnet.infura.543254324532543254345'
ethereum_address = '0xeb9f035dd1211af75976427d68d2d6dc549c458e'
# Create an pyetherbalance object , pass the infura_url
ethbalance = pyetherbalance.PyEtherBalance(infura_url)
# get ether balance
balance_eth = ethbalance.get_eth_balance(ethereum_address)
print(balance_eth)
# get token balance 
balance_omg = ethbalance.get_token_balance('OMG', ethereum_address)
print(balance_omg)

```

Advanced Usage: 
----

Adding tokens

Currently the module uses https://github.com/ethereum-lists/tokens for a list of tokens. If you want to add your own custom token, you can follow the steps below. This will also work for overwriting internal token contract addresses. 

```python
import pyetherbalance 
# Sign up for https://infura.io/, and get the url to an ethereum node
infura_url = 'https://mainnet.infura.543254324532543254345'
ethereum_address = '0xeb9f035dd1211af75976427d68d2d6dc549c458e'
# Create an pyetherbalance object , pass the infura_url
ethbalance = pyetherbalance.PyEtherBalance(infura_url)
# New token symbol
token = "OMG"
# Token details. The fields below are all required
details = {'symbol': 'OMG', 'address': '0xd26114cd6EE289AccF82350c8d8487fedB8A0C07', 'decimals': 18, 'name': 'OmiseGO'}
# Add token 
erc20tokens = ethbalance.add_token(token, details)
# print list of all internal tokens
print(erc20tokens['OMG'])
```

Getting all tokens:

```python
import pyetherbalance 
# Sign up for https://infura.io/, and get the url to an ethereum node
infura_url = 'https://mainnet.infura.543254324532543254345'
# Create an pyetherbalance object , pass the infura_url
ethbalance = pyetherbalance.PyEtherBalance(infura_url)
# Get a dictionary with all tokens and details 
erc20tokens = ethbalance.get_erc20_tokens()
print(erc20tokens)
```




Testing:
----

Test You can test on either Ropsten, Kovan, Rinkeby or local testnets by providing the url of your corresponding ethereum node, while initializing pyetherbalance object. 

   
Copyright
---------

MTI License - See LICENSE for details.

Changelog
--------- 
## Version 0.0.1
### New
 - First Working Version  
