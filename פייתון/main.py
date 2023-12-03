import urllib.request
num_car=input("enter num of car")
if len(num_car)!=7:
    print("the size of num car dont right")
else:
    url = f'https://data.gov.il/api/3/action/datastore_search?resource_id=053cea08-09bc-40ec-8f7a-156f0677aff3&limit=5&q=:{num_car}'
    fileobj = urllib.request.urlopen(url)
    print(fileobj.read().decode())