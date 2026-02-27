# Telegram Lead Bot

Simple Telegram bot for collecting client requests.

## Features
- Welcome message on /start
- Button for submitting a request
- Sends client messages directly to admin in Telegram
- Easy to customize for any business

## Technologies
- Python
- pyTelegramBotAPI (TeleBot)

## Setup Instructions

1. Clone the repository:
git clone https://github.com/zit-w/telegram-lead-bot.git

2. Go to the project folder:
cd telegram-lead-bot

3. Install dependencies:
pip install -r requirements.txt

4. Edit the configuration:
Open bot.py and replace:
- YOUR_BOT_TOKEN — token from BotFather
- YOUR_USER_ID — your Telegram ID (get it from @userinfobot)

5. Run the bot:
python bot.py

## How it works
1. User starts the bot
2. Clicks "Оставить заявку"
3. Writes a message
4. Admin receives the request instantly

## Use cases
- Collect client requests
- Small business automation
- Lead generation
- Customer support

## Contact
Telegram: https://t.me/zit_w
