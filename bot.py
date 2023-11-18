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
bot = commands.Bot(command_prefix=',', intents=intents)
    
# HRH The Chores Bot

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return

# The chores list

	kitchen = [
		'Today, you should clean out the fridge.', 
		'Today, you should take out recycling.', 
		'Today, you should wash recycling trashcans and the shelf.', 
		'Today, you should wash the dishes.', 
		'Today, you should vacuum the floor.', 
		'Today, you should clean the countertops.', 
		'Today, you should clean the oven.', 
		'Today, you should change the dishes pad.', 
		'Today, you should declutter the spice rack.', 
		'Today, you should declutter the tea rack.', 
		'Today, you should wipe down the outer elements.',
		'Today, you should wipe down the inner elements.', 
		'Today, you should declutter the entrance shelf.', 
		'Today, you should declutter the lazy susan cabinet.', 
		'Today, you should wipe down and declutter the upper cabinets.', 
		'Today, you should wash the floors.', 
		'Today, you should declutter shoes.', 
		'Today, you should declutter the side cabinet.', 
		'Today, you should declutter the wall board.', 
		'Today, you should declutter the hallway corner.']

	bathroom = [
		'Today, you should wipe down the mirror.', 
		'Today, you should declutter the sink.', 
		'Today, you should wipe down the sink.', 
		'Today, you should change the towels.', 
		'Today, you should declutter the storage.', 
		'Today, you should wipe down the storage.',
		'Today, you should change the trashbag.', 
		'Today, you should wipe down the trash.', 
		'Today, you should wash the shower.', 
		'Today, you should unplug the shower.', 
		'Today, you should vacuum the floors.', 
		'Today, you should change the shower mat.', 
		'Today, you should wash the floors.']

	toilet = [
		'Today, you should wipe down the mirror.', 
		'Today, you should wipe down the sink.', 
		'Today, you should wipe down the TP shelf.', 
		'Today, you should change the towel.', 
		'Today, you should wipe down the accessories.', 
		'Today, you should disinfect the switches/knobs.',
		'Today, you should clean the toilet.', 
		'Today, you should put on a toilet earring.', 
		'Today, you should vacuum the floor.', 
		'Today, you should mop the floor.']

	dining = [
		'Today, you should dust.', 
		'Today, you should wipe down the chairs.', 
		'Today, you should declutter the upper shelf.', 
		'Today, you should wipe down the upper shelf.', 
		'Today, you should declutter the table.', 
		'Today, you should change the tablecloths.', 
		'Today, you should wipe down the table.', 
		'Today, you should clean cat dishes.', 
		'Today, you should clean the cat tray.', 
		'Today, you should clean the floor where the cat eats.', 
		'Today, you should vacuum the floor.', 
		'Today, you should wash the floors.']

	bedroom = [
		'Today, you should declutter the bedsides.', 
		'Today, you should declutter the bed storage.', 
		'Today, you should declutter the laundry room.', 
		'Today, you should declutter the low small wardrobe surface.',
		'Today, you should declutter the lower wardrobe.', 
		'Today, you should declutter the low small wardrobe cabinets.', 
		'Today, you should wipe and clear the desk and upper desk area.', 
		'Today, you should vaccuum the mattress.',
		'Today, you should wipe the baseboard.', 
		'Today, you should change the sheets.', 
		'Today, you should wash the bedding.', 
		'Today, you should wash the towels.', 
		'Today, you should hang up the wet clothes.', 
		'Today, you should fold the laundry.', 
		'Today, you should put away the laundry.', 
		'Today, you should dust.',
		'Today, you should disinfect light switches/knobs/handles.', 
		'Today, you should vacuum the floors.', 
		'Today, you should wash the floors.']

	living = [
		'Today, you should dust.', 
		'Today, you should vacuum the floors and the rug.', 
		'Today, you should put away remotes and controllers.',
		'Today, you should dust the windowsills.', 
		'Today, you should declutter the cat toy shed.',
		'Today, you should declutter and dust the TV stand.', 
		'Today, you should wipe down the TV.', 
		'Today, you should arrange the couch.', 
		'Today, you should wipe down the coffee stand.', 
		'Today, you should declutter the desk stand.',
		'Today, you should declutter the desk.', 
		'Today, you should clean the kitty litter.', 
		'Today, you should clean the kitty area.', 
		'Today, you should order the board.', 
		'Today, you should wash the floors.', 
		'Today, you should order and wipe the bookshelves.']

# Outputs

	if message.content == 'kitchen':
		response = "\n".join(random.choices(kitchen, k=3))
		await message.channel.send(response)
	await bot.process_commands(message)

	if message.content == 'bathroom':
		response = "\n".join(random.choices(bathroom, k=3))
		await message.channel.send(response)
	await bot.process_commands(message)

	if message.content == 'toilet':
		response = "\n".join(random.choices(toilet, k=3))
		await message.channel.send(response)
	await bot.process_commands(message)

	if message.content == 'dining room':
		response = "\n".join(random.choices(dining, k=3))
		await message.channel.send(response)
	await bot.process_commands(message)

	if message.content == 'bedroom':
		response = "\n".join(random.choices(bedroom, k=3))
		await message.channel.send(response)
	await bot.process_commands(message)

	if message.content == 'living room':
		response = "\n".join(random.choices(living, k=3))
		await message.channel.send(response)
	await bot.process_commands(message)

bot.run(TOKEN)
