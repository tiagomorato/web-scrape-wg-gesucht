import logging
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import telebot
from db_functions import db_query, db_create_table


load_dotenv()
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
bot = telebot.TeleBot(os.environ.get('API_KEY'))

CREATE_TABLE = True


@bot.message_handler(commands=['wg'])
def greet(message):
    url = "https://www.wg-gesucht.de/wg-zimmer-in-Berlin.8.0.1.0.html"

    # Initialize message to be sent
    msg = ''

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find_all('div', {'class': 'wgg_card offer_list_item'})

    # To later only insert posts that are not in the database
    existing_data_id = db_query('SELECT data_id FROM wg_berlin')
    existing_data_id = set(item for t in existing_data_id for item in t)

    for post in posts:
        data_id = post.get('data-id')

        if int(data_id) not in existing_data_id:
            title = post.find('h3', {'class': 'truncate_title noprint'}).text.strip()
            size = post.find('div', {'class': 'col-xs-3 text-right'}).text.strip()
            price = post.find('div', {'class': 'col-xs-3'}).text.strip()
            flatmate = post.find('span', {'class': 'noprint'}).attrs.get('title', '').strip()
            available = post.find('div', {'class': 'col-xs-5 text-center'}).text.strip()
            available = ' '.join(available.split())

            # Get link
            h3 = post.find('h3', {'class': 'truncate_title noprint'})
            a_tag = h3.find('a')
            href = a_tag.get('href')
            link = "https://www.wg-gesucht.de" + href

            # Get address
            div = post.find('div', {'class': 'col-xs-11'})
            address = div.find('span').text.strip()

            # Remove unnecessary spaces
            address = ' '.join(address.split())[9:].strip()
            author = post.find('span', {'class': 'ml5'}).text.strip()
            online = post.find('span', attrs={'style': 'color: #218700;'}).text
            online = online[8:]

            try:
                data = [data_id, title, address, price, size, flatmate, available, online, author, link]
                query = 'INSERT INTO wg_berlin(data_id, title, address, price, size, flatmate, available, on_since, author, link) ' \
                        'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                res = db_query(query, data)

                if res:
                    msg += "Title: {}\n" \
                           "Address: {}\n" \
                           "Price: {}\n" \
                           "Size: {}\n" \
                           "Flatmate: {}\n" \
                           "Availability: {}\n" \
                           "Online: {}\n" \
                           "Author: {}\n" \
                           "Link: {}\n\n".format(*data[1:])
            except Exception as e:
                print("Error:", e)

    if msg:
        # Send message via telebot
        bot.reply_to(message, msg)
    else:
        no_wg = "~empty~"
        bot.reply_to(message, no_wg)


if __name__ == '__main__':
    if CREATE_TABLE:
        db_create_table()

    bot.polling(non_stop=True)


