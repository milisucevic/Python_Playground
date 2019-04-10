from __future__ import print_function
import requests, json


class PostCodeException(Exception):
    pass


class FsPostcodes:
    def __init__(self, url):
        """
        :str url: The API url to connect to
        """
        self.URL = url

    def _do_get(self, postCode):
        """
        Performs a GET request for the specified postcode
        :str postCode: Postcode to request details of
        :return: dict containing the JSON formatted response
        """
        full_url = '%s/%s' % (self.URL, postCode)
        try:
            raw_data = requests.get(full_url, timeout=1.0)
        except requests.ConnectionError, e:
            raise PostCodeException('Unable to establish connection to %s - %s' % (full_url, e.message))

        try:
            json_data = json.loads(raw_data.content)
        except ValueError:
            raise PostCodeException('API %s returned a malformed response - %s' % (full_url, raw_data))

        if 'result' in json_data:
            return json_data
        else:
            raise PostCodeException('Invalid Postcode - %s' % postCode)

    def _parse_output(self, data):
        """
        Format Postcode data into a printable string
        :param data: The JSON data dictionary returned from the API
        :return: String containing the postcode, country and region
        """
        result = data['result']

        try:
            postcode = str(result['postcode'])
        except KeyError:
            postcode = None

        try:
            country = str(result['country'])
        except KeyError:
            country = None

        try:
            region = str(result['region'])
        except KeyError:
            region = None

        return 'Postcode: %s, Country: %s, Region: %s' % (postcode, country, region)

    def _deduplicate(self, array):
        """
        Remove duplicates from array
        :list array: Array of items to de-duplicate
        :return: A de-duplicated array of items
        """
        if type(array) != list:
            raise PostCodeException('Invalid data type - %s' % type(array))
        else:
            output = []
            for item in array:
                duplicate = False

                for dup_candidate in output:
                    if item == dup_candidate:
                        duplicate = True

                if not duplicate:
                    output += [item]
        return output

    def run(self, postcodeArray):
        """
        Run postcode requests for one or multiple postcodes
        :param postcodeArray:
        :return:
        """
        if type(postcodeArray) == str:
            data = self._do_get(postcodeArray)
            print('1) %s' % self._parse_output(data))
        else:
            counter = 1
            for postcode in self._deduplicate(postcodeArray):
                data = self._do_get(postcode)
                result = self._parse_output(data)
                print('%i) %s' % (counter, result))
                counter += 1