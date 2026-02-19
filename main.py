import requests
from bs4 import BeatifulSoup

def weather_cheсk(city):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 YaBrowser/25.12.0.0 Safari/537.36'

    }

    response= requestes.get(
        f"https://www.google.com/search?q=погода+в+{city}", 
        headers=headers)
    print(response)

    soup = BeatifulSoup(res.text, 'html.parser')

    temperature = soup.select("#wob_tm")[0].getText()
    title = soup.select("#wob_dc")[0].getText()
    humidity = soup.select("#wob_hm")[0].getText()
    time = soup.select("#wob_dts")[0].getText()
    wind = soup.select("#wob_ws")[0].getText()