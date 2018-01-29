import requests
from SorgBot import SorgBot
resp_json = requests.get('https://api.telegram.org/bot525519947:AAG2k1H8wZb_G01YEv-cIh0Tq0DCnQQYBKY/getUpdates', {'offset':None, 'timeout':30})
resp_py = resp_json.json()
results = resp_py['result']
print(results)


def get_updates_test():
    resp1 = requests.get('https://api.telegram.org/bot525519947:AAG2k1H8wZb_G01YEv-cIh0Tq0DCnQQYBKY/getUpdates', {'offset' :None, 'timeout': 30})
    resp2 = resp1.json()['result']
    return resp2


print(get_updates_test())

test_bot = SorgBot('525519947:AAG2k1H8wZb_G01YEv-cIh0Tq0DCnQQYBKY')

print(test_bot.get_updates())
