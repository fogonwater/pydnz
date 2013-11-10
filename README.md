#pyDNZ - A Python client for the DigitalNZ API
#### under active development! 

[DigitalNZ](http://digitalnz.org/) aims to make New Zealand digital content more useful. DigitalNZ provides an API to help developerrs people find digital material from libraries, museums, government departments, publicly funded organisations, the private sector, and community groups. This python library is a wrapper around that API, making it easier to interact with.

pyDNZ is based on [DPyLA](https://github.com/bibliotechy/DPyLA) - A Python client for the [The DPLA](http://dp.la) (Digital Public Library of America).

Tested and working with Python 2.7

### Dependencies
Depends on the [Requests package](http://www.python-requests.org/en/latest/)

####Getting started

There is no installer for this script yet. In the meantime, simply drop the pyDnz.py script into a directory your 

Then fire up your fave python interpreter and:

`>>> from pydnz import Dnz`

Then create the dnz object with your [DigitalNZ API key](http://digitalnz.org/api_keys).

`>>> dnz = Dnz('YOUR_API_KEY')` 

Now, create create your first search

`>>> result = dnz.search('kiwi')`

Records returned are in result.records. Let's take a look.

`>>> import pprint.pprint as pp
>>> pp(result.records)
`