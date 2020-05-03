# program to display currency rates by using web scrapping
import datetime
from os import system

import requests
from bs4 import BeautifulSoup

print("Welcome TO the curency converter")
while True:
    print("What do you want to convert?\n 1)Pounds\n", "2)Australian-Dollars\n", "4)Dirhams\n", "3)Canadian-Dollars\n",
          "5)Dollars\n", "6)Euros\n", "7)Lira\n", "8)New-Zealand-Dollars\n"
          , "9)Rupees\n", "10)South-African-Rands\n", "11)Swiss-Francs-currency\n", "13)Yen\n", "type 'quit' to exit")
    choice = input()
    if choice == 'quit':
        exit("thank you for using currency converter")
    currency = ["Pounds", "Australian-Dollars", "Canadian-Dollars", "Dirhams", "Dollars", "Euros", "Lira",
                "New-Zealand-Dollars",
                "Rupees", "South-African-Rands", "Swiss-Francs-currency", "Yen"]
    cto = currency[int(choice) - 1]

    print("What do you want from convert?\n 1)Pounds\n", "2)Australian-Dollars\n", "4)Dirhams\n",
          "3)Canadian-Dollars\n",
          "5)Dollars\n", "6)Euros\n", "7)Lira\n", "8)New-Zealand-Dollars\n"
          , "9)Rupees\n", "10)South-African-Rands\n", "11)Swiss-Francs-currency\n", "13)Yen\n", "type 'quit' to exit")
    choice = input()
    if choice == 'quit':
        exit("thank you for using currency converter")

    cfrom = currency[int(choice) - 1]

    page = requests.get("https://www.exchangerates.org.uk/" + cfrom + "-to-" + cto + "-currency-conversion-page.html")

    soup = BeautifulSoup(page.content, "html.parser")

    conversion_rates = soup.find(id="conversion-chart-today")

    conversion_data = conversion_rates.find(class_="convtop").get_text()

    print("Current Exchange Rates\n" + conversion_data + "\nat " + str(datetime.datetime.now()))
    c = conversion_data.split("=")
    c = c[1].split(" ")
    amount = input("how much do you want to convert")
    converted = float(amount) * float(c[1])
    print("after conversion amount is", converted, c[2])
    input("press any key to continue")
    system("clear")
