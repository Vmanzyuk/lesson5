import requests
import settings



def get_weather(url,PROXY):
    result = requests.get(url,proxies=PROXY)
    if result.status_code==200:
        return result.json()
    else:
        print('Govno')


if __name__=="__main__":
    data=get_weather('http://api.openweathermap.org/data/2.5/weather?id=524901&APPID={}&units=metric'.format(settings.API_key),settings.PROXY)
    print(data)

