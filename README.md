# Table of contents
- [Web Scraping WG-Gesucht](#web-scraping-wg-gesucht)
  * [Tech Stack](#tech-stack)
  * [Description](#description)
  * [How to use](#how-to-use)
  * [Visual](#visual)
  * [Limitations](#limitations)
  * [Future improvements](#future-improvements)
    + [Message length](#message-length)
    + [Filters](#filters)
    + [Automatize](#automatize)
  * [Data Visualization](#data-visualization)
    + [Barplot](#barplot)
    + [Scatterplot 1](#scatterplot-1)
    + [Scatterplot 2](#scatterplot-2)
    + [Plotly Dashboard](#plotly-dashboard)

# Web Scraping WG-Gesucht

## Tech Stack
![Python Logo](https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg)
![MySQL Logo](https://github.com/devicons/devicon/blob/master/icons/mysql/mysql-original-wordmark.svg)
![HTML Logo](https://github.com/devicons/devicon/blob/master/icons/html5/html5-plain-wordmark.svg)
![CSS Logo](https://github.com/devicons/devicon/blob/master/icons/css3/css3-plain-wordmark.svg)
![Heroku Logo](https://github.com/devicons/devicon/blob/master/icons/heroku/heroku-plain-wordmark.svg)


## Description
Looking for a shared flat or WG-Gesucht can be a tedious and time-consuming task of constantly refreshing the page and scrolling through each post. This Telegram Bot streamlines the process by iteratively scraping each post from a given link's main page, adding it to a MySQL database, and sending a message to your Telegram Bot chat containing the new posts and their relevant information.
 
## How to use
 To use this bot, first change the variables for the database and your Telegram bot's API key in the .env file. The default URL is set for Berlin's page, but you can change it to your target city. If the CREATE_TABLE variable in main.py is set to True, a table named wg_berlin will be automatically created if it does not already exist. Then, go to your bot's chat and type \wg_berlin to get the latest posts.
 
## Visual
![Telegram Bot message](https://github.com/tiagomorato/web-scrape-wg-gesucht/blob/main/img/telebot.jpg)

## Future improvements

### Message length
If the msg variable is too long, an error may occur due to the Telegram bot's 400-character limit. To avoid this issue, future versions could implement a mechanism to split the message into smaller chunks.

### Filters
Adding filters for each category (Flatmate, Rent, m^2, District, Availability, etc.) could help users retrieve more specific posts that match their preferences.

### Automatization
In this version, users must always type \wg_berlin to check for new announcements. A better approach would be to implement a feature that periodically checks for new posts and sends them to users automatically.

## Data Visualization

### Barplot
![Barplot](https://github.com/tiagomorato/web-scrape-wg-gesucht/blob/main/img/barplot.png)

### Scatterplot 1
![Scatterplot 1](https://github.com/tiagomorato/web-scrape-wg-gesucht/blob/main/img/scatterplot.png)

### Scatterplot 2
![Scatterplot 2](https://github.com/tiagomorato/web-scrape-wg-gesucht/blob/main/img/scatterplot-per-district.png)

### Plotly Dashboard
![Plotly Dashboard](https://github.com/tiagomorato/web-scrape-wg-gesucht/blob/main/img/plotly-dashboard.jpg)
