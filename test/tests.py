from dnz.api import *

def test_api_key_passed_as_parameter():
	'''
	Validates the API constructor.
	'''
	key = "abcde"
	dnz = Dnz(key)
	assert key == dnz.api_key, "Invalid API key found"

def test_api_missing_key():
	key = None
	dnz = None
	try:
		dnz = Dnz(key)
	except:
		pass
	assert dnz == None, "API must throw error on invalid API key"

def test_results_with_errors():
	errors = 'Invalid API Key'
	results = Results(response={'errors': errors}, request=None)
	assert results.errors == errors, 'Invalid Results errors value'

def test_results():
	response = {
		'search': {
			'result_count': 15,
			'results': ['dvcor', 'dvco'],
			'facets': {}
		}
	}
	results = Results(response=response, request='Request')

	assert 'Request' == results.request, 'Wrong request value'
	assert 15 == results.result_count, 'Result count does not match'