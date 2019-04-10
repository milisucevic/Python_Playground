from __future__ import print_function
import sys
from lib import fs_postcodes


def handle_args(args_array):
    base_url = 'http://api.postcodes.io/'
    api = 'postcodes/'
    args = args_array[1:]
    if '-n' in args:
        api = 'postcodes/nearest/'
        args.remove('-n')
    elif  '-nearest' in args:
        api = 'postcodes/nearest/'
        args.remove('-nearest')

    postcode_array = [x.strip() for x in ' '.join(args).split(',')]

    return '%s%s' %(base_url, api), postcode_array


def main(api_url, postcodes):
    postcode_handler = fs_postcodes.FsPostcodes(api_url)
    postcode_handler.run(postcodes)


if __name__ == '__main__':
    url, postcodes = handle_args(sys.argv)
    try:
        main(url, postcodes)
    except fs_postcodes.PostCodeException, e:
        print('An exception occurred: %s' % e.message)
