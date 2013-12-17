import json
from requests import get
from requests.compat import urlencode

class Dnz():
    def __init__(self,api_key=None):
        if api_key:
            self.api_key = api_key
        else:
            raise ValueError('DigitalNZ API requires an api key.')

    def search(self, q=None, **kwargs):
        # Builds and performs an item search.
        if not q and not kwargs:
            raise ValueError("You must specify search criteria.")
        if q:
            kwargs['query'] = q

        kwargs['key'] = self.api_key
        request = Request(**kwargs)
        return Results(get(request.url).json(), request)

class Request():
    def __init__(self, query=None, fields=None, facets=None, sort=None, direction=None, 
                 per_page=None, page=None, facets_per_page=None,
                 _and=None, _or=None, _without=None,
                 key='', wild=None):
        ''' 
        Build individual url fragments for different search criteria
        TODO - write help text.
        '''
        url_parts = []
        self.base_url = "http://api.digitalnz.org/v3/records.json"
        self.api_key =  key
        if query:
            url_parts.append(self._singleValueFormatter('text',query))
        if fields:
            url_parts.append(self._multiValueFormatter('fields',fields))
        if facets:
            url_parts.append(self._multiValueFormatter('facets',facets))
        if sort:
            url_parts.append(self._singleValueFormatter('sort', sort))
        if direction:
            url_parts.append(self._singleValueFormatter('direction', direction))
        if per_page or per_page==0:
            url_parts.append(self._singleValueFormatter('per_page',per_page))
        if facets_per_page or facets_per_page==0:
            url_parts.append(self._singleValueFormatter('facets_per_page',facets_per_page))
        if page:
            url_parts.append(self._singleValueFormatter('page',page))
        if _and:
            url_parts.append(self._multiDictFormatter('and',_and))
        if _or:
            url_parts.append(self._multiDictFormatter('or',_or))
        if _without:
            url_parts.append(self._multiDictFormatter('without',_without))
        if wild:
            url_parts.append(wild)
        # Now combine all the chunks together
        self.url = self._buildUrl(url_parts)
        print 'Requesting:', self.url


    def _buildUrl(self, url_parts=None):
        url = [
            self.base_url,
            "?",
            "&".join(url_parts),
            "&api_key=",
            self.api_key
        ]
        return ''.join(url)

    def _singleValueFormatter(self, param_name, value):
        # Creates an encoded URL fragment for parameters that contain only a single value
        return urlencode({param_name: value})

    def _multiValueFormatter(self, param_name, values):
        # Creates an encoded URL fragment for parameters that may contain multiple values.
        if isinstance(values, basestring):
            raise ValueError("Multi-value parameters should not be strings.")
        return urlencode({param_name: ','.join(values)})

    def _multiDictFormatter(self, param_name, values):
        # Creates an encoded URL fragment for parameters that are dictionaries.
        url_parts = []
        for k in values.keys():
            param_scoped_name = '%s[%s][]' % (param_name, k)
            #check the dict values are not strings
            if isinstance(values[k], basestring):
                raise ValueError("Multi-value parameters should not be strings.")
            for value in values[k]:
                url_parts.append( urlencode(({param_scoped_name: value})) )
        return '&'.join(url_parts)

    def _searchFieldsFormatter(self, searchFields):
        # Creates an encoded URL fragment for searching for a value within a specific field.
        # If multiple fields are specified, a single string is returned
        sf = [urlencode({k:v}) for k,v in searchFields.records() if k in settings.searchable_fields]
        return '&'.join(sf)

class Results():
    def __init__(self, response, request):
        self.request = request
        self.result_count = response['search']['result_count']
        self.records= [result for result in response['search']['results']]
        self.facets=[{k:v} for k,v in  response['search']['facets'].iteritems()]
