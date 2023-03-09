import requests, telepot, os
from dotenv import load_dotenv

load_dotenv()
id_telegram = os.getenv('ID_TELEGRAM')
token = os.getenv('TOKEN')
bot = telepot.Bot(token)
# '```\n' +  https://wttr.in/Jakarta+Selatan?2Fnq  + '```'
text = requests.get('https://v2.wttr.in/Jakarta%20Selatan?format=%l :+\n%T+\n%c+%t / %f+\n%C').text
bot.sendMessage(id_telegram, text, 'Markdown')