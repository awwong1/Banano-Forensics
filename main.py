import requests
import json
from collections import defaultdict

#myaddress = "ban_1tc93no6sebhpbh69b877wy3hhhxriqoj5cneq3qbfg9skw63o9wbezrjmka"


host = 'http://167.99.212.163:2454'

#Run me after entering an address and then run other bits
#print(txt.value)
address = input("Enter a Banano address begginning with ban_\n")
if address == "":
    address = "ban_1tc93no6sebhpbh69b877wy3hhhxriqoj5cneq3qbfg9skw63o9wbezrjmka"
#Test Payload of block count
payload = {'action': 'block_count'}
r = requests.post(host, json=payload)
print(r.text)

payload = {"action": "account_balance", "account": address}
r = requests.post(host, json=payload)
resp_json = r.json() #Storing the JSON response in a dictionary
print(resp_json['balance']) #Accessing the balance key in RAW format

payload = {"action": "ban_from_raw", "amount": resp_json['balance']} #Converts raw format to Banano Format
r = requests.post(host, json=payload)

print(r.text)

bal_json = r.json()
print(address + " has " + str(bal_json['amount']) + " Banano")


payload = {"action": "account_key", "account" : address} # Turns an address into a public key
r = requests.post(host, json=payload)
#print(r.text)

payload = {"action": "account_key", "account" : "ban_1tc93no6sebhpbh69b877wy3hhhxriqoj5cneq3qbfg9skw63o9wbezrjmka"} # Turns an address into a public key
r = requests.post(host, json=payload)
print(r.text)

payload = {"action": "account_key", "account" : "ban_1mj43j4y4n6a7ppr7989ty94fi7zkc3s55un81ntrjnud4ncmsbk9we9dxcf"} # Turns an address into a public key
r = requests.post(host, json=payload)
print(r.text)

noTrans = input("How many transactions should be retrieved: ")
if noTrans == "":
    noTrans = 1

payload = {"action": "account_history", "account": address,"count": noTrans}
r = requests.post(host, json=payload)
resp_json = r.json()
print(resp_json)

nodes = defaultdict(list)




count = 0
for i in resp_json['history']:
    count = count+1
    #for j in resp_json['history'][i]:
        #print(j)
    #print(i['type'])
    payload = {"action": "ban_from_raw", "amount": i['amount']} #Converts raw format to Banano Format
    r = requests.post(host, json=payload)
    bal_json = r.json()
    amount = bal_json['amount']
    
    print("boo")
    
    if i['type'] == "receive":
        
        print(address + " has received " + str(amount) + "Ban from " + i['account'] + " with transaction hash: " + i['hash'] + "\n")
    elif i['type'] == "send": 
        print(address + " has sent " + str(amount) + "Ban to " + i['account'] + " with transaction hash: " + i['hash'] + "\n")
       
    nodes[address].append(i['account'])
    
print(nodes)

print(address + " has made " + str(count) + " transactions")