# A Discord bot developed by PhantomAlcor with contributions from MrGeneralissimo

#Setup
import discord
import asyncio
import datetime
import random
import time
import json

from discord.ext import commands

client = commands.Bot(command_prefix = '%')
# Removes the default help menu
#client.remove_command("help")

# Bot Status
@client.event
async def on_ready():
    print("The", client.user.name,"bot is online")
    print("Bot ID:", client.user.id)
    print("The current command prefix is: %")
    print("~~~~~~~~~~~~~~")
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("%help for commands!"))

# Brand new help command
@client.command(aliases = ["Help"])
@commands.has_permissions(manage_messages = True)
async def help(ctx):
    await ctx.send('''```
Current Commands:
%about    
%ban      
%clear    
%help     
%kick     
%latency  
%unban    
%veb_data

Type %help command for more info on a command.
```''')

#About the bot
@client.command(aliases = ["About"])
@commands.has_permissions(manage_messages = True)
async def about(ctx):
    await ctx.send('''```
Bot and logo developed and created by:
PhantomAlcor, with contributions from MrGeneralissimo

*Expect frequent shutdowns 
                   ```''')

########## Utility ##########

# Bot will print it's latency
@client.command(category = "Utility", aliases = ["Latency"], description = "Bot will check it's latency; Measured in miliseconds; Must have manage_messages permission")
@commands.has_permissions(manage_messages = True)
async def latency(ctx):
    await ctx.send(f'```Bot Latency: ~{round(client.latency * 1000)}ms```')

# Bot will clear a certain amount of messages
@client.command(aliases = ["Clear"], description = "Bot will clear a specified amount of messages excluding the context; Defaults to three messages; Must have manage_messages permission")
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount = 3):
    if amount >= 151:
        await ctx.send('You cannot delete that many!')
        return
    await ctx.channel.purge(limit = amount + 1)

# Kicks a specified member
@client.command(aliases = ["Kick"], description = "Bot will kick a specified member; Must have kick permission")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await ctx.send("See ya later, nerd")
    await member.kick(reason = reason)

# Bans a specified member
@client.command(aliases = ["Ban"], description = "Bot will ban a specified member; Must have ban permission")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'You just got the ban hammer!')

# Unbans a specified member
@client.command(aliases = ['Unban'], description = 'Bot will unban a specified member; Command format: "unban user_name#0000; Must have unban permission"')
@commands.has_permissions(ban_members = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

# DMs' a message to someone who joins
@client.event
async def on_member_join(ctx):
    await ctx.send(f'Welcome to {ctx.guild.name}; Make sure to read the rules!')
# Insert sends a message when someone leaves command:

######### Random Bullcrap #########

@client.command(aliases = ["VEB_data", "vef_data", "VEF_data"], description = "Bot will display the value of the Venizuelan Bolivar in United States Dollars")
@commands.has_permissions(manage_messages = True)
async def veb_data(ctx):
    # TODO: Debug load_currency_data; Specifically, the error message says that it was never awaited; Line 113
    def load_currency_data():
        with open('currency_data.json') as raw_currency_data:
            currency_data = json.load(raw_currency_data)

        for data in currency_data["main"]:
            venezuelan_bolivar = data["venezuela_bolivar"]

        return venezuelan_bolivar
        
    await ctx.send(load_currency_data())

########## Bot will run it's token ##########
client.run("Njc4NjY1MjQ5ODE3MTAwMzE5.XkmIhw.D2dBzjUXzpUSkgvxYZXBt9sK_IE")
# invite authorization link: https://discordapp.com/oauth2/authorize?client_id=678665249817100319&scope=bot
