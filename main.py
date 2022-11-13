import os
import discord
from replit import db

intents = discord.Intents.all()
'''this is required for message access'''
client = discord.Client(intents=intents)
token = os.environ['TOKEN']

def ifExist(id):
  if id in db:
    return True
  else:
    return False

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  print(str(message.author.id) + ": "+ message.content)
  if message.author==client.user:
    return
  if message.content.startswith('!tokat'):
    if ifExist(str(message.author.id)):
      db[str(message.author.id)]=db[str(message.author.id)]+1
      print('incremented '+str(message.author.id)+' slap count by 1')
      print(db[str(message.author.id)])
    else:
      db[str(message.author.id)]=0
      print('New user entry to the database')
    await message.channel.send('Yine bir gun,yine bir bela...')
  if message.content.startswith('!toplam'):
    await message.channel.send('Lanetli gun sayisi '+ str(db[str(message.author.id)]))

client.run(token)