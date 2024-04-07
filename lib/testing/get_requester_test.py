from GetRequester import GetRequester

class TestGetRequester:
    '''Class {Classname} in {modulename}.py'''
    URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
    EXPECTED_DATA = [
        {'name': 'Daniel', 'occupation': 'LG Fridge Salesman'},
        {'name': 'Joe', 'occupation': 'WiFi Fixer'},
        {'name': 'Avi', 'occupation': 'DJ'},
        {'name': 'Howard', 'occupation': 'Mountain Legend'}
    ]

    def test_get_response(self):
        '''get_response_body function returns response.'''
        requester = GetRequester(self.URL)
        assert requester.get_response_body() != ''

    def test_load_json(self):
        '''load_json function returns response.'''
        requester = GetRequester(self.URL)
        assert requester.load_json() == self.EXPECTED_DATA