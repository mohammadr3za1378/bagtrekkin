from bagtrekkin.api.tests.auth_resource_test_case import AuthResourceTestCase


class FlightResourceTestCase(AuthResourceTestCase):
    version = 'v1'
    resource = 'flight'
    fixtures = ['users', 'companies', 'flights']
    fields = [
        'aircraft', 'airline', 'arrival_loc', 'arrival_time', 'company',
        'departure_loc', 'departure_time', 'duration', 'etickets',
        'flight_date', 'id', 'resource_uri'
    ]

    def test_get_list_unauthorized(self):
        '''Should return unauthorized response'''
        self.get_list_unauthorized()

    def test_get_list_basic_auth(self):
        '''Should return objects list based on Basic Authentication'''
        response, data = self.get_list_basic_auth()

    def test_get_list_apikey_auth(self):
        '''Should return objects list based on ApiKey Authentication'''
        response, data = self.get_list_apikey_auth()

    def test_get_schema_authorized(self):
        '''Should return appropriate schema based on Resource'''
        response, data = self.get_schema_authorized(['filtering'])

    def test_get_detail_basic_auth(self):
        '''Should return object details based on Basic Authentication'''
        response, data = self.get_detail_basic_auth()

    def test_get_detail_apikey_auth(self):
        '''Should return object details based on ApiKey Authentication'''
        response, data = self.get_detail_apikey_auth()
