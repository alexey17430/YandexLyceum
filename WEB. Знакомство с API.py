import requests
from pprint import pprint

for elem in ['Хабаровск', 'Уфа', 'Нижний Новгород', 'Калининград']:
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-" \
                       f"98533de7710b&geocode={elem}" \
                       f"&format=json&results=1"
    response = requests.get(geocoder_request)

    if response:
        ans = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject'][
            'metaDataProperty']['GeocoderMetaData']['Address']['Components'][1]['name']
        pprint(ans)
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
