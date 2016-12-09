import config # local file for storing the ACCESS_TOKEN
import json
import requests

url = "http://www.searchupc.com/handlers/upcsearch.ashx?request_type=3&access_token=B4EDA630-C081-496C-B70C-2E7A44CAFCBA&upc="

def getProductJSON(barcode):
	searchUrl = url + barcode
	response = requests.get(searchUrl)
	return json.loads(response.text)["0"]

def getProductName(product):
	return product["productname"]
