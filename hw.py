import requests

city = input('Enter your city : ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=004b8852267fb87c0f29ecc435c80b1e&units=metric'.format(city)

res = requests.get(url)

data = res.json()
try:
    temp = int(data['main']['temp'])

    print('Temperature : {} '.format(temp))

    if temp < 10 and temp > 0:
        print('Kurtka')

    elif temp < 0:
        print('Zima')

    elif temp > 10 and temp < 17:
        print('Teplo, vesna')

    elif temp > 17:
        print('Lito')
except KeyError:
    print('Nema takogo mista')
    
