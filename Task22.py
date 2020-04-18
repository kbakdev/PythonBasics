import pip._vendor.requests as requests
city = input('Podaj miasto: ')
api_address = 'http://openweathermap.org/data/2.5/weather?q='+city+'&appid=439d4b804bc8187953eb36d2a8c26a02'
json_data = requests.get(api_address).json()
print('Temperatura: ',json_data['main']['temp'],'C','\nNiebo: ',json_data['weather'][0]['description'],)