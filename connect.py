from sys import path

path.append('..')


from client import Client
from library import convertpe , convertep






bot_token = 'w17xsFMZdYdGSGgZy9-AJ2HK5bzXb8qf2-7ln4ClwAgAdTF9itwtzeFCqDsqfviyVTlgI9OUKApUcSqkFtcgvKUKIgti0WJG_so_y0cyRTKqQIVEpvvmurDnNfMZP0OdUMF6uJ5cYB3EqSv7'

bot1 = Client(bot_token)
bot1.RETRY_DELAY = 1

def massages ():

   try:
      messages = bot1.get_messages()
      for msg in messages:

         msg ['body'] = convertpe (msg ['body'])


         yield (msg)

   except Exception as e:
      print(e.args[0])



def send_message (data):
   data ['body'] = convertep( data ['body'] )
   bot1.send_message ( data )














#url = "https://bot.sapp.ir/XayO8FeO8PDjV1Xq0unWmLxsUf6MjFMnG5DFk7EVwRTsSD4PVc8lMX-d3AlBqu6e4zbLWIioqyMb_nwr1vmVMeUy3c3x_ZWZBoBjKQF6H3QcHUdkKfe2LDUTwcvl8ZDBI8NYkOGD8dTUdBqm/getMessage"
