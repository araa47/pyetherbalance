import decimal
import requests
import json
from .erc20tokens  import tokens 


class PyEtherBalance(object):
	def __init__(self, node_url, erc20_tokens_json=None):
		# Ethereum node::string 
		self.node_url = node_url
		# json erc20 tokens :: dict 
		## sample 
		#{"OMG":{'symbol': 'OMG', 'address': '0xd26114cd6EE289AccF82350c8d8487fedB8A0C07', 'decimals': 18, 'name': 'OmiseGO'},
		#"ZRX": {'symbol': 'ZRX', 'address': '0xE41d2489571d322189246DaFA5ebDe1F4699F498', 'decimals': 18, 'name': '0x Project'}}
		# If not passed use custom json
		if erc20_tokens_json is None:
			self.erc20_tokens = tokens
		# if passed use the json object passed 
		else:
			self.erc20_tokens = erc20_tokens_json
	
	# function to add custom token to tokens 
	def add_token(self, token, details):
		# If fields in details, update internal tokens
		if all (item in details for item in ("name", "address", "decimals", "symbol")):
			self.erc20_tokens[token] = details
			return self.erc20_tokens
		else:
			errormsg = "Error! details must include the following keys, name, address, decimals and symbol"
			return errormsg
		
	# This function posts JSON RPC requests to the ethereum node  
	def json_rpc_post(self,method, params, id):
		url = self.node_url
		headers = {'content-type': 'application/json'}
		payload = {
			"method": method,
			"params": params,
			"jsonrpc": "2.0",
			"id": id,
		}
		try:
			response = requests.post(url, data=json.dumps(payload), headers=headers)
			if response.status_code == 200:
				response = response.json()
				return response
		except Exception as e:
			return(e)
	
	# Get all internal tokens and details 
	def get_erc20_tokens(self):
		return self.erc20_tokens
	
	# Get ethereum balance	
	def get_eth_balance(self, address):
		response = self.json_rpc_post('eth_getBalance', [address,'latest'], 1)
		final_result = None 
		try:
			balance = response.get('result', None)
			balance = decimal.Decimal(float.fromhex(balance))
			balance = balance / decimal.Decimal(1000000000000000000)
			final_result = {'status':'ok', 'name': 'Ethereum', 'balance': float(str(balance)), 'symbol': 'ETH'}
		except Exception as e:
			final_result = {'status': 'error', 'description':(str(e))}
		return final_result
	
	# Get token balance 
	def get_token_balance(self, symbol, address):
		# get contract address from interally saved tokens
		contract_address = (self.erc20_tokens.get(symbol, {})).get('address', None)
		if contract_address is None:
			# not supported
			return {'status': 'unsupported token'}
		# get name
		name = self.erc20_tokens.get(symbol).get('name')
		# get precision (10^decimals)
		precision = 10 ** self.erc20_tokens.get(symbol).get('decimals')
		# build abi 
		abi = '0x70a08231000000000000000000000000' + address[2:]
		params = [{"to": contract_address, "data":abi}, "latest"]
		response = self.json_rpc_post('eth_call', params, 1)
		final_result = None 
		try:
			balance = response.get('result', None)
			balance = decimal.Decimal(float.fromhex(balance))
			balance = balance / decimal.Decimal(precision)
			final_result = {'status':'ok', 'name': name, 'balance': float(str(balance)), 'symbol': symbol}
		except Exception as e:
			final_result = {'status': 'error', 'description':(str(e))}
		return final_result

