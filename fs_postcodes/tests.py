#Milica Sucevic
#Featurespace Tester Coding Task

import os
import urllib as req
import json


#Postcodes Autocomplete
def getAutoCompletePostcode(postcode):
    url = 'http://api.postcodes.io/postcodes/{}/autocomplete'.format(postcode)
    return loadJsonResponse(url)

def loadJsonResponse(url):
    return json.loads(req.urlopen(url).read())['result']

def main():

    #postcodes_string = "CB80BE, CB80BD, CB80BF"

    #Print Postcodes from a File
    """
    f_postcodes = open("/home/msucevic/Desktop/fs_postcodes/postcodes.txt", "rt")
    postcodes_string = f_postcodes.read()
    """

    #Print Auto Complete Postcode
    postcode_lst = (getAutoCompletePostcode('CB80B'))
    postcode_str_tmp = ""
    for postcode in postcode_lst:
        postcode_str_tmp = postcode_str_tmp+(str(postcode)) + ", "
    
    postcodes_string = postcode_str_tmp[:-2]
    
    #Run Python Program
    cmd_str= "python main.py "
    cmd_str = cmd_str + postcodes_string
    os.system(cmd_str)

if __name__ == '__main__':
    main()
