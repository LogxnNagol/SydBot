import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
import random

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game(name="Discord"))
	print('Bot is ready!')

@client.event
async def on_member_join(member):
	print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
	print(f'{member} has left the server.')

@client.command()
async def ping(ctx):
	await ctx.send(f'Ping is {round(client.latency * 1000)}ms')

@client.command()
@commands.has_permissions(administrator=True)
async def syd(ctx, syd):
  if 
    await message.delete(message)
    
@purge.error
async def error(ctx, error):
	if isinstance(error, administrator=False):
		await ctx.send('Sorry you are not allowed to use this command.')
   
