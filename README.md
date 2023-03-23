- [Web Scraping WG-Gesucht](#web-scraping-wg-gesucht)
  * [Description](#description)
  * [How to use](#how-to-use)
  * [Limitations](#limitations)
  * [Future improvements](#future-improvements)
    + [Message length](#message-length)
    + [Filters](#filters)
    + [Automatize](#automatize)

# Web Scraping WG-Gesucht

## Description
Looking for a shared flat or WG-Gesucht can be a tedious and time-consuming task of constantly refreshing the page and scrolling through each post. This Telegram Bot streamlines the process by iteratively scraping each post from a given link's main page, adding it to a MySQL database, and sending a message to your Telegram Bot chat containing the new posts and their relevant information.
 
## How to use
 To use this bot, first change the variables for the database and your Telegram bot's API key in the .env file. The default URL is set for Berlin's page, but you can change it to your target city. If the CREATE_TABLE variable in main.py is set to True, a table named wg_berlin will be automatically created if it does not already exist. Then, go to your bot's chat and type \wg_berlin to get the latest posts.
 
## Visuals
![Telegram Bot message](https://github.com/tiagomorato/web-scrape-wg-gesucht/blob/main/img/img-telebot1.jpg)

## Future improvements

### Message length
If the msg variable is too long, an error may occur due to the Telegram bot's 400-character limit. To avoid this issue, future versions could implement a mechanism to split the message into smaller chunks.

### Filters
Adding filters for each category (Flatmate, Rent, m^2, District, Availability, etc.) could help users retrieve more specific posts that match their preferences.

### Automatization
In this version, users must always type \wg_berlin to check for new announcements. A better approach would be to implement a feature that periodically checks for new posts and sends them to users automatically.
