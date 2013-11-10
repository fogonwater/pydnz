#pyDnz - A Python client for the v3 DigitalNZ API
##### under active development...

[DigitalNZ](http://digitalnz.org/) aims to make New Zealand digital content more useful. DigitalNZ provides an API to help developerrs people find digital material from libraries, museums, government departments, publicly funded organisations, the private sector, and community groups. This python library is a wrapper around that API, making it easier to interact with.

pyDNZ is based on [DPyLA](https://github.com/bibliotechy/DPyLA) - A Python client for the [The DPLA](http://dp.la) (Digital Public Library of America).

Tested and working with Python 2.7. See the [DigitalNZ API v3 docs](http://digitalnz.org/developers/api-docs-v3/search-records-api-v3) for more information about the API.

### Dependencies
Depends on the [Requests package](http://www.python-requests.org/en/latest/).

####Getting started

There is no installer for this script yet. In the meantime, simply drop the pyDnz.py script into a directory with your project. 

Then start a python interpreter and type:

`>>> from pydnz import Dnz`

Then create the dnz object with your [DigitalNZ API key](http://digitalnz.org/api_keys).

`>>> dnz = Dnz('YOUR_API_KEY')` 

Now, create your first search

`>>> result = dnz.search('kiwi tui')`

Matching rcords returned are in _result.records_ as a dictionary of values. Let's take a look. First import the standard pretty printer.

`>>> import pprint.pprint as pp`

And now pretty print the record results.

`>>> pp(result.records)`

You can also find out how many records were found matching that criteria with _result.result_count_.
```
>>> print result.result_count
6323
```

Sometimes you only want to see certain fields in your result. Feed a list of fields as an array or tuple.

```
>>> result = dnz.search('kiwi tui', fields=['id', title', 'collection', 'content_partner'])
>>> pp(result.records)
```

#### Pagination
You can also so more or fewer results using the _per_page_ parameter (maximum value of 100) and paginate through with the _page_ paramater.

```
>>> result = dnz.search('kiwi tui', fields=['id', 'title', 'collection', 'content_partner'], per_page=50, page=10)
>>> pp(result.records)
```

#### Facets
Get back a list of the most common terms within a field for this set of results as _result.facets_. See the [DigitalNZ API v3 docs](http://digitalnz.org/developers/api-docs-v3/search-records-api-v3) for more info.

```
>>> result = dnz.search('kiwi tui', per_page=0, facets=['year', 'collection'])
>>> pp(result.facets)
```

You can also increase the number of facets returned (up to a maximum of 150) with the _facets_per_page_ parameter.

```
>>> result = dnz.search('kiwi tui', per_page=0, facets=['year', 'collection'], facets_per_page=30)
>>> pp(result.facets)
```

#### Sort
Pass a sortable field along with the _sort_ field and a _direction_ to order the result set. Sortable fields are 'category', 'content_partner', 'date', 'syndication_date', 'title'. Directions can be 'asc' or 'desc'.

```
result = dnz.search('penguin', sort='date', direction='desc', fields=['title', 'date'])
pp(result.records)
```

## Limitations
Early days. Still a fair few rough edges.
* No test coverage.
* Does not support _and[field]_, _or[field]_, _without[field]_ searches... yet.
* Geographic search.
* Oh, you know... all that other stuff.

##License

GPLV2. 
See [license.txt](license.txt)