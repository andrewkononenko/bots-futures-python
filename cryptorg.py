import requests
import json
import time
import hashlib
import base64
import hmac

class Api():

	""" This is API for Cryptorg.net """

	apiKey = ''
	apiSecret = ''
	apiUrl = 'https://api2.cryptorg.net'

	""" Cryptorg api constructor """
	def __init__(self, apiKey, apiSecret):
		self.apiKey = apiKey
		self.apiSecret = apiSecret

	""" Get list of user's bots """
	def botList(self):
		return self.sendRequest('GET', '/bot-futures/all', 'exchange=CRYPTORG_FUTURES')

	""" Update bot settings """
	def updateBot(self, params, attributes):

		try:
			query = "pairTitle=" + params['pairTitle'] + "&botId=" + str(params['botId'])
			pass

		except Exception as e:
			return {'status': 'ok', 'result': 'false', 'message': e}

		else:
			a = self.sendRequest('POST', '/bot-futures/update', query, attributes)
			return a

	""" Send request to api.cryptorg.net """
	def sendRequest(self, method, url, query = '', params = ''):

		nonce = str(int(time.time()))

		authStr = url + '/' + nonce + '/' + query
		strForSign = base64.b64encode(authStr.encode('utf-8'))

		hash = hmac.new(self.apiSecret.encode('utf-8'), strForSign, hashlib.sha256).hexdigest()

		headers = {

			"CTG-API-SIGNATURE": str(hash),
			"CTG-API-KEY": str(self.apiKey),
			"CTG-API-NONCE": nonce
		}

		signUrl = self.apiUrl + url + '?' + query

		if (method == 'GET'):
			response = requests.get(url = signUrl, headers = headers).text

		if (method == 'POST'):
			response = requests.post(url = signUrl, headers = headers, json=params).text

		return json.dumps(json.loads(response), indent=4, sort_keys=True)
		