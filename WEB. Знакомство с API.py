import requests

geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-" \
                   "98533de7710b&geocode=Исторический+музей+города+Москва,Красная+площадь,1" \
                   "&format=json&results=1"

response = requests.get(geocoder_request)
if response:
    ans1 = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject'][
        'Point']['pos']
    ans2 = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject'][
        'metaDataProperty']['GeocoderMetaData']['AddressDetails']['Country']['AddressLine']
    ans3 = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject'][
        'metaDataProperty']['GeocoderMetaData']['AddressDetails']['Country']['AdministrativeArea'][
        'Locality']['Thoroughfare']['Premise']['PostalCode']['PostalCodeNumber']
    print(ans1, ans3 + ' ' + ans2, sep='\n')
else:
    print("Ошибка выполнения запроса:")
    print(geocoder_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
