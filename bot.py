# imports

import os
import discord
import random

from discord.ext.commands import Bot
from discord.ext import commands
from dotenv import load_dotenv

# environment variables

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# intents

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)
    
# HRH The Chores Bot

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return

# The chores list

	kitchen = [
		' clean out the fridge',
		' take out recycling',
		' wash recycling trashcans and the shelf',
		' wash the dishes',
		' vacuum the floor',
		' clean the counter tops',
		' clean the oven',
		' change the dishes pad',
		' declutter the spice rack',
		' declutter the tea rack',
		' wipe down the outer elements',
		' wipe down the inner elements',
		' declutter the entrance shelf',
		' declutter the lazy susan cabinet',
		' wipe down and declutter the upper cabinets',
		' declutter the misc middle and top shelves'
		' wash the floors',
		' declutter shoes',
		' declutter the side cabinet',
		' declutter the wall board',
		' declutter the hallway corner']

	bathroom = [
		' wipe down the mirror',
		' declutter the sink',
		' wipe down the sink',
		' change the towels',
		' declutter the storage',
		' wipe down the storage',
		' change the trash bag',
		' wipe down the trash',
		' wash the shower',
		' unplug the shower',
		' vacuum the floors',
		' change the shower mat',
		' wash the floors']

	toilet = [
		' wipe down the mirror',
		' wipe down the sink',
		' wipe down the TP shelf',
		' change the towel',
		' wipe down the accessories',
		' disinfect the switches/knobs',
		' clean the toilet',
		' put on a toilet earring',
		' vacuum the floor',
		' mop the floor']

	dining = [
		' dust',
		' wipe down the chairs',
		' declutter the upper shelf',
		' wipe down the upper shelf',
		' declutter the table',
		' change the tablecloths',
		' wipe down the table',
		' clean cat dishes',
		' clean the cat tray',
		' clean the floor where the cat eats',
		' vacuum the floor',
		' wash the floors']

	bedroom = [
		' declutter the bedsides',
		' declutter the bed storage',
		' declutter the laundry room',
		' declutter the low small wardrobe surface',
		' declutter the lower wardrobe',
		' declutter the low small wardrobe cabinets',
		' wipe and clear the desk and upper desk area',
		' vacuum the mattress',
		' wipe the baseboard',
		' change the sheets',
		' wash the bedding',
		' wash the towels',
		' hang up the wet clothes',
		' fold the laundry',
		' put away the laundry',
		' dust',
		' disinfect light switches/knobs/handles',
		' vacuum the floors',
		' wash the floors']

	living = [
		' dust the living room area',
		' vacuum the floors and the rug',
		' put away remotes and controllers',
		' dust the windowsills',
		' declutter the cat toy shed',
		' declutter and dust the TV stand',
		' wipe down the TV',
		' arrange the couch',
		' wipe down the coffee stand',
		' declutter the desk stand',
		' declutter the desk',
		' clean the kitty litter',
		' clean the kitty area',
		' order the board',
		' wash the floors',
		' order and wipe the bookshelves']

# Outputs

	if message.content == 'kitchen':
		response = ",".join(random.sample(kitchen, k=3))
		await message.channel.send(f'Today in the kitchen, you should: {response}.')
	await bot.process_commands(message)

	if message.content == 'bathroom':
		response = ",".join(random.sample(bathroom, k=3))
		await message.channel.send(f'Today in the bathroom, you should: {response}.')
	await bot.process_commands(message)

	if message.content == 'toilet':
		response = ",".join(random.sample(toilet, k=3))
		await message.channel.send(f'Today in the toilet, you should: {response}.')
	await bot.process_commands(message)

	if message.content == 'dining room':
		response = ",".join(random.sample(dining, k=3))
		await message.channel.send(f'Today in the dining room, you should: {response}.')
	await bot.process_commands(message)

	if message.content == 'bedroom':
		response = ",".join(random.sample(bedroom, k=3))
		await message.channel.send(f'Today in the bedroom room, you should: {response}.')
	await bot.process_commands(message)

	if message.content == 'living room':
		response = ",".join(random.sample(living, k=3))
		await message.channel.send(f'Today in the living room room, you should: {response}.')
	await bot.process_commands(message)

bot.run(TOKEN)
