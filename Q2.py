# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import json


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def Login():

    url = 'https://api.qa.foureyesinsight.uk/portal/access/login'
    x = '{"email": "Test.User+1@foureyesinsight.com","Password": "#InterVIEW123!"}'

    headers = {'content-type': 'application/json'}
    x = requests.post(url, data=x, headers=headers)
    print(x.status_code)
    print(x.text)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('start')
    Login()
    print('end')
