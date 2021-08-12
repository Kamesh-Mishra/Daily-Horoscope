import requests
from bs4 import BeautifulSoup

def horoscope(zodiac_sign, day):
    url = ("https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{}.aspx?sign={}".format(day, zodiac_sign))
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup.find("div", class_="main-horoscope").p.text
    
print("Daily Horoscope: \n")
print("enter your Zodiac sign number:\n",
        "1. Aries\n",
        "2. Taurus\n",
        "3. Gemini\n",
        "4. Cancer\n",
        "5. Leo\n",
        "6. Virgo\n",
        "7. Libra\n",
        "8. Scorpio\n",
        "9. Sagittarius\n",
        "10. Capricorn\n",
        "11. Aquarius\n",
        "12. Pisces"
    )
zodiac_sign = int(input("Input number> "))
print("\nchoose day:\n", "yesterday\n", "today\n", "tomorrow")
day = input("enter the day> ")
horoscope_text = horoscope(zodiac_sign, day)
print("\n",horoscope_text)