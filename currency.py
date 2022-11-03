import requests
import argparse


def convert_currency(base_currency, converted_currency):
    headers = {
        "apikey": "4JTun5eI3GRAKlv5EX9EEFsB0csmrctm"
    }
    payload = {}
    url = f'https://api.apilayer.com/exchangerates_data/convert?to={converted_currency}&from={base_currency}&amount=1'
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    return data['result']


parser = argparse.ArgumentParser(prog='converter',
                                 usage='%(prog)s [options]',
                                 description='Convert your currency into another')


parser.add_argument('b',
                    type=str,
                    help='base currency',
                    action='store')

parser.add_argument('c',
                    type=str,
                    help='converted currency',
                    action='store')


args = parser.parse_args()


arguments = vars(args)

print("{0:.2f}".format(convert_currency(arguments['b'], arguments['c'])))
