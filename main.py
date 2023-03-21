import os

# import missing libraries
try:
    import discord 
    from discord.ext import commands
    from dotenv import load_dotenv
    from discord.ext import tasks
    import time
    import random
    import requests
    from morse_code_translator.translator import translate_to_lat
    from morse_code_translator.translator import translate_to_morse
    from google_translate_py import Translator
    import math
    from os import path
    import colorama
    from textwrap import wrap
    import base64
    import numpy as np
    import subprocess
    import sys
    import openai
except ImportError:
    os.system('pip install discord.py-self python-dotenv google-translate-py colorama openai')
    import discord 
    from discord.ext import commands
    from dotenv import load_dotenv
    from discord.ext import tasks
    import time
    import random
    import requests
    from morse_code_translator.translator import translate_to_lat
    from morse_code_translator.translator import translate_to_morse
    from google_translate_py import Translator
    import math
    from os import path
    import colorama
    from textwrap import wrap
    import base64
    import numpy as np
    import subprocess
    import sys
    import openai

##devmode - dont use outside of testing
devmode=1
##public commands - experimental
publix=0
##auto response - use rarely as is easily triggered and detected (may result in a ban)
ares=0
if ares==0:
    areson="Inactive"
if ares==1:
    areson="Active"
##sniper for nitro - could get you in trouble (may result in a ban)
nitrosnipe=1
##modules/commands that are quite risky to have (if used incorrectly can brick entire pc)
risky=1
if risky==0:
    riskyon="Inactive"
if risky==1:
    riskyon="Active"




if getattr(sys, 'frozen', False):
        # we are running in a bundle
        bundle_dir = os.path.dirname(sys.executable)
else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))


txtwall="""
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
  
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
  
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
 ㅤ
  ㅤ
 """
clr = "\033[38;2;159;0;245m"
cmdcoun=0

cmdcount=cmdcoun
os.system('title Loading...')

load_dotenv()

bot=commands.Bot(command_prefix="-", self_bot=True)
@bot.event
async def on_connect():
    global cmdcoun
    os.system('title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = '+str(cmdcoun)+'')
    ascii_art = [
        "                       ___           ___                   ___                       ___     ",
        "                      /\\  \\         /\\__\\      ___        |\\__\\          ___        /\\  \\    ",
        "                     /::\\  \\       /:/  /     /\\  \\       |:|  |        /\\  \\      /::\\  \\   ",
        "                    /:/\\:\\  \\     /:/  /      \\:\\  \\      |:|  |        \\:\\  \\    /:/\\:\\  \\  ",
        "                   /::\\~\\:\\  \\   /:/  /       /::\\__\\     |:|__|__      /::\\__\\  /::\\~\\:\\  \\ ",
        "                  /:/\\:\\ \\:\\__\\ /:/__/     __/:/\\/__/ ____/::::\\__\\  __/:/\\/__/ /:/\\:\\ \\:\\__\\",
        "                  \\:\~\\ \\ \\/__/ \\:\\  \\    \\/\\:/  /    \\::::/~~/~    \\/\\:/  /    \\\\_|::\\/:/  /",
        "                   \\:\\ \\ \\__\\    \\:\\  \\   \\::/__/      ~~|:|~~|     \\::/__/        |:|::/  / ",
        "                    \\:\\ \\/__/     \\:\\  \\   \\:\\__\\        |:|  |      \\:\\__\\        |:|\\/__/  ",
        "                     \\:\\__\\        \\:\\__\\   \\:__/         \\|__|       \\:__/        \\|__|   ",
    ]

    start_color = (89, 5, 245) # #5905f5
    end_color = (213, 5, 245) # #d
    for line in ascii_art:
            pos = np.linspace(0, 1, len(line))
            for j, char in enumerate(line):
                color_ratio = pos[j]
                color = tuple(map(lambda x: int(np.interp(color_ratio, [0, 1], x)), zip(start_color, end_color)))
                ansi_color = f"\033[38;2;{color[0]};{color[1]};{color[2]}m"
                print(ansi_color + char, end="")
            print("\033[0m\n", end="")
    print("""
    
    """)
    start_color, end_color = end_color, start_color
    text = "--------------------------------------------------[Elixir Self-Bot started]--------------------------------------------------"
    pos = np.linspace(0, 1, len(text))
    for j, char in enumerate(text):
        color_ratio = pos[j]
        color = tuple(map(lambda x: int(np.interp(color_ratio, [0, 1], x)), zip(start_color, end_color)))
        ansi_color = f"\033[38;2;{color[0]};{color[1]};{color[2]}m"
        print(ansi_color + char, end="")
    print("\033[0m")
    clor = f"\033[38;2;159;0;245m"
    text = "                    "
    print(clor + text )


@bot.command()
async def ping(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -ping')
    await ctx.send(f"``` Pong! >> {int(bot.latency*1000)}ms ```")

@bot.command()
async def test(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -test')
    await ctx.send(f"/beg")

@bot.command()
async def restart(ctx):
    global cmdcoun
    cmdcoun = cmdcoun + 1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -restart')
    await ctx.send(f"``` Restarting...```")
    os.system("cls")
    
    # Get the name of the current script
    current_script = os.path.basename(sys.argv[0])
    
    if getattr(sys, 'frozen', False):
        # We are running as a frozen executable
        if current_script.endswith('.exe'):
            # Restart the frozen executable
            subprocess.Popen([sys.executable, os.path.abspath(sys.argv[0])])
        else:
            # We don't know how to restart a non-executable frozen script
            await ctx.send(f"``` Unable to restart a non-executable frozen script```")
    else:
        # We are running as a Python script
        if current_script.endswith('.py'):
            # Restart the Python script
            subprocess.Popen([sys.executable, os.path.abspath(sys.argv[0])])
        else:
            # We don't know how to restart a non-Python script
            await ctx.send(f"``` Unable to restart a non-Python script```")

@bot.command()
async def ares(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -ares')
    global ares
    if ares==1:
        ares=0
        await ctx.send("``` Auto-respond is now disabled ```")
    else:
        ares=1
        await ctx.send("``` Auto-respond is now enabled ```")

@bot.command()
async def publix(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -publix')
    global publix
    if publix==1:
        publix=0
        await ctx.send("``` Public commands are now disabled ```")
    else:
        publix=1
        await ctx.send("``` Public commands are now enabled ```")

@bot.command()
async def clearcmd(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -clearcmd')
    print("Reloading...")
    time.sleep(2)
    os.system("cls")
    await ctx.send(f"``` Clearing the terminal output ```")
    time.sleep(0.5)
    ascii_art = [
        "                       ___           ___                   ___                       ___     ",
        "                      /\\  \\         /\\__\\      ___        |\\__\\          ___        /\\  \\    ",
        "                     /::\\  \\       /:/  /     /\\  \\       |:|  |        /\\  \\      /::\\  \\   ",
        "                    /:/\\:\\  \\     /:/  /      \\:\\  \\      |:|  |        \\:\\  \\    /:/\\:\\  \\  ",
        "                   /::\\~\\:\\  \\   /:/  /       /::\\__\\     |:|__|__      /::\\__\\  /::\\~\\:\\  \\ ",
        "                  /:/\\:\\ \\:\\__\\ /:/__/     __/:/\\/__/ ____/::::\\__\\  __/:/\\/__/ /:/\\:\\ \\:\\__\\",
        "                  \\:\~\\ \\ \\/__/ \\:\\  \\    \\/\\:/  /    \\::::/~~/~    \\/\\:/  /    \\\\_|::\\/:/  /",
        "                   \\:\\ \\ \\__\\    \\:\\  \\   \\::/__/      ~~|:|~~|     \\::/__/        |:|::/  / ",
        "                    \\:\\ \\/__/     \\:\\  \\   \\:\\__\\        |:|  |      \\:\\__\\        |:|\\/__/  ",
        "                     \\:\\__\\        \\:\\__\\   \\:__/         \\|__|       \\:__/        \\|__|   ",
    ]

    start_color = (89, 5, 245) # #5905f5
    end_color = (213, 5, 245) # #d
    for line in ascii_art:
            pos = np.linspace(0, 1, len(line))
            for j, char in enumerate(line):
                color_ratio = pos[j]
                color = tuple(map(lambda x: int(np.interp(color_ratio, [0, 1], x)), zip(start_color, end_color)))
                ansi_color = f"\033[38;2;{color[0]};{color[1]};{color[2]}m"
                print(ansi_color + char, end="")
            print("\033[0m\n", end="")
    print("""
    
    """)
    start_color, end_color = end_color, start_color
    text = "--------------------------------------------------[Elixir Self-Bot started]--------------------------------------------------"
    pos = np.linspace(0, 1, len(text))
    for j, char in enumerate(text):
        color_ratio = pos[j]
        color = tuple(map(lambda x: int(np.interp(color_ratio, [0, 1], x)), zip(start_color, end_color)))
        ansi_color = f"\033[38;2;{color[0]};{color[1]};{color[2]}m"
        print(ansi_color + char, end="")
    print("\033[0m")
    clor = f"\033[38;2;159;0;245m"
    text = "                    "
    print(clor + text )
    

@bot.command()
async def real(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -real')
    await ctx.send("https://media.tenor.com/qoAGskeO8Y8AAAAC/spin-cat-get-real.gif")

@bot.command()
async def gpt(ctx, question: str):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -gpt {question}')
    openai.api_key = os.getenv('CHAT_KEY')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.4,
    )

    message = response.choices[0].text.strip()

    await ctx.send("```"+message+"```")

@bot.command()  # changes everyones nickanme
@commands.has_permissions(manage_nicknames=True)
async def nickall(ctx, arg):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=arg)
        except:
            pass

@bot.command(aliases=['floodaudit'])  # audit flood
async def auditflood(ctx, arg):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -auditflood {arg}')
    await ctx.message.delete()

    amount = int(arg)
    for _ in range(amount):
        await ctx.message.channel.create_invite(max_age=0, max_uses=0)

@bot.command()
async def raid(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -raid')
    await ctx.message.delete()
    await ctx.send("https://tenor.com/view/raid-shadow-legends-raid-gif-20940490")
    members = ''
    guild = ctx.message.guild

    for member in guild.members:
        members += f'{member.mention}'

    ping = members[0:1990]

    for _ in range(5):
        for channel in ctx.message.guild.text_channels:
            await channel.send(txtwall)
            rekt = await channel.send(f'{ping} @everyone')

@bot.command()  # Purge messages command
async def purge(ctx, arg):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    await ctx.message.delete()
    user = ctx.message.author
    print(f'        {user} >> -purge {arg}')

    async for msg in ctx.message.channel.history(limit=int(arg)):
        if msg.author.id == bot.user.id:
            time.sleep(0.1)
            try:
                await msg.delete()
            except:
                continue

@bot.command(aliases=['makechannels'])  # Make channels command
@commands.has_permissions(manage_channels=True)
async def mk_channels(ctx, arg1, arg2):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    await ctx.message.delete()
    user = ctx.message.author
    print(f'        {user} >> -mk_channels {arg1} {arg2}')
    guild = ctx.message.guild
    amount = int(arg1)
    for x in range(amount):
        if arg2 == 'random':
            name = random.randint(1, 100)
            await guild.create_text_channel(name)
        else:
            await guild.create_text_channel(arg2)

@bot.command(aliases=['delchannels'])  # Delete channels command
@commands.has_permissions(manage_channels=True)
async def del_channels(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    await ctx.message.delete()
    user = ctx.message.author
    print(f'        {user} >> -del_channels')
    for c in ctx.guild.channels:
        await c.delete()

@bot.command()  # Nuke command
@commands.has_permissions(manage_guild=True)
async def nuke(ctx, arg1, arg2, arg3):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    await ctx.message.delete()
    user = ctx.message.author
    print(f'        {user} >> -nuke {arg1} {arg2} {arg3}')
    for c in ctx.guild.channels:
        await c.delete()

    guild = ctx.message.guild
    amount = int(arg1)
    for x in range(amount):
        channel = await guild.create_text_channel(arg2)
        await channel.send('@everyone')

    await ctx.guild.edit(name=arg3)

@bot.command()  # Activity command
async def play(ctx, arg):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    await ctx.message.delete()
    user = ctx.message.author
    print(f'        {user} >> -play {arg}')
    await bot.change_presence(activity=discord.Game(name=arg))
    await ctx.send("``` Play activity changed to \""+arg+"\" ```")

@bot.command(aliases=['react_messages'])  # React to messages
@commands.has_permissions(add_reactions=True)
async def react(ctx, arg, times: int):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    await ctx.message.delete()
    user = ctx.message.author
    print(f'        {user} >> -react {arg} {times}')
    messages = await ctx.message.channel.history(limit=times).flatten()
    for message in messages:
        await message.add_reaction(arg)

@bot.command(aliases=['react_text'])  # React to messages with cool little text shits
@commands.has_permissions(add_reactions=True)
async def txtreact(ctx, arg, times: int):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    await ctx.message.delete()
    user = ctx.message.author
    print(f'        {user} >> -react {arg} {times}')
    reaction="e"
    messages = await ctx.message.channel.history(limit=times).flatten()
    for message in messages:
        await message.add_reaction(arg)

@bot.command(aliases=['save_account'])  # backup friends and guilds
async def backup(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    await ctx.message.delete()
    user = ctx.message.author
    print(f'        {user} >> -backup')
    f = open('./backup/guilds.txt', 'w', encoding='utf-8')
    for guild in bot.guilds:
        f.write(f'{guild.id} - {guild.name}\n')
    f.close()

    f = open('./backup/friends.txt', 'w', encoding='utf-8')
    for friend in bot.user.friends:
        f.write(f'{friend.id} - {friend.name}#{friend.discriminator}\n')
    f.close()

@bot.command(aliases=['deleteserver', 'server_delete', 'delete_server'])  # delete server
@commands.has_permissions(manage_guild=True)
async def delserver(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    await ctx.message.delete()
    user = ctx.message.author
    print(f'        {user} >> -delserver')
    await ctx.message.guild.delete()

@bot.command()  # Clones server
async def cloneserver(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    await ctx.message.delete()
    user = ctx.message.author
    print(f'        {user} >> -cloneserver')
    server = ctx.message.guild
    roles = server.roles

    guild = await bot.create_guild(ctx.message.guild.name)

    for cg in server.categories:
        for c in ctx.guild.channels:
            await c.delete()
        category = await guild.create_category(cg.name)

        for channel in cg.channels:
            if isinstance(channel, discord.VoiceChannel):
                vc = await category.create_voice_channel(channel.name)
                overwrites = channel.overwrites
                await vc.edit(overwrites=overwrites)

            if isinstance(channel, discord.TextChannel):
                cha = await category.create_text_channel(channel.name)
                overwrites = channel.overwrites
                await cha.edit(overwrites=overwrites)

    for role in roles:
        role = await guild.create_role(name=role.name,
                                       permissions=discord.Permissions(permissions=role.permissions.value))

    try:
        await guild.edit(icon=ctx.message.guild.icon)
    except:
        pass

@bot.command()  # Ping server memberos
async def massm(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    guild = ctx.message.guild
    await ctx.message.delete()
    user = ctx.message.author
    print(f'        {user} >> -massm')
    members = ''

    for member in guild.members:
        members = f'{members}<@{member.id}>'

    n = 2000

    pings = wrap(members, 2000)

    for ping in pings:
        await ctx.send(ping)

@bot.command()
async def randomnum(ctx, num1: int, num2: int):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -randomnum {num1} {num2}')
    num1r2=random.randint(num1,num2)
    await ctx.send("``` Random number between "+str(num1)+" and "+str(num2)+" >>  "+str(num1r2)+" ```")

@bot.command()
async def base64e(ctx, inp: str):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    await ctx.message.delete()
    print(f'        {user} >> -base64e {inp}')
    encoded_message = base64.b64encode(inp.encode())
    await ctx.send("```"+str(encoded_message.decode())+"```")

@bot.command()
async def base64de(ctx, inp: str):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    await ctx.message.delete()
    print(f'        {user} >> -base64e {inp}')
    decoded_message = base64.b64decode(inp).decode()
    await ctx.send("```"+str(decoded_message)+"```")

@bot.command()
async def userinfo(ctx, inuser: discord.User):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -userinfo {user}')
    await ctx.send("``` Username >> "+str(inuser.name)+"#"+str(inuser.discriminator)+"""
    ID >> """+str(inuser.id)+"""
    Account created >> """+str(inuser.created_at)+"""
    Bot? >> """+str(inuser.bot)+"```")

@bot.command()
async def crime(ctx, user: discord.User):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -crime {user}')
    await ctx.send("``` "+str(user.name)+"#"+str(user.discriminator)+" has commited :""""
    ID >> """+str(user.id)+"""
    Account created >> """+str(user.created_at)+"""
    Bot? >> """+str(user.bot)+"```")


@bot.command()
async def google(ctx, q: str):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -google {q}')
    qq=q.replace(" ", "+")
    await ctx.send(f"""```ini
[https://www.google.com/search?q={qq}] ```""")

@bot.command()
async def urban(ctx, q: str):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -urban {q}')
    qq=q.replace(" ", "+")
    await ctx.send(f"""```ini
[https://www.urbandictionary.com/define.php?term={qq}] ```""")

@bot.command()
async def spam(ctx, tx: str, rep1: int, slep: int):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -spam {tx} {rep1} {slep}')
    await ctx.message.delete()
    try:
        pass
    except ValueError:
        await ctx.send("``` Enter a number dumbass ```")
    for i in range(int(rep1)):
        await ctx.send(tx)
        rand=0.2+int(random.randrange(1, 7))*0.1+slep
        if devmode==1:
            print("         Spam delay : "+str(float(rand)))
        else:
            pass
        time.sleep(rand)

@bot.command()
async def realspam(ctx, rep1: int):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -realspam {rep1}')
    await ctx.message.delete()
    try:
        pass
    except ValueError:
        await ctx.send("``` Enter a number dumbass ```")
    for i in range(int(rep1)):
        await ctx.send("https://media.tenor.com/qoAGskeO8Y8AAAAC/spin-cat-get-real.gif")
        rand=0.3+int(random.randrange(1, 9))*0.1
        if devmode==1:
            print("         Real-spam delay : "+str(float(rand)))
        else:
            pass
        time.sleep(rand)

@bot.command()
async def nerdspam(ctx, repn: int, nloop: int):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -nerdspam {repn} {nloop}')
    await ctx.message.delete()
    for i in range(nloop):
        if(nloop>1):
            await ctx.send(":nerd:"*repn)
            nsleep=0.1+int(random.randrange(2, 7)*0.1)
            print("         Nerd-spam delay : "+str(nsleep)+"s")
            time.sleep(nsleep)
        if nloop==1:
            await ctx.send(":nerd:"*repn)

@bot.command()
async def nerdgifspam(ctx, repngif: int):
    global cmdcoun
    cmdcoun=cmdcoun+1
    user = ctx.message.author
    print(f'        {user} >> -nerdgifspam {repngif}')
    await ctx.message.delete()
    for i in range(repngif):
        await ctx.send("https://tenor.com/view/nerd-nerd-emoji-nerd-emoji-meme-accttually-nerd-emoji-gif-26120328")
        nsleep=0.2+random.randint(1, 6)*0.1
        time.sleep(nsleep)
        print("         Nerdgifspam delay : "+str(nsleep)+"s")

@bot.command()
async def textwall(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -textwall')
    await ctx.message.delete()
    await ctx.send("."+"""
    
    """*160+".")

@bot.command()
async def everyonespam(ctx, rep1: int):
    global cmdcoun
    cmdcoun=cmdcoun+1
    user = ctx.message.author
    print(f'        {user} >> -everyonespam {rep1}')
    await ctx.message.delete()
    try:
        pass
    except ValueError:
        await ctx.send("``` Enter a number dumbass ```")
    for i in range(int(rep1)):
        await ctx.send("@everyone")
        rand=0.3+int(random.randrange(1, 9))*0.1
        if devmode==1:
            print("         Everyone-spam delay : "+str(float(rand)))
        else:
            pass
        time.sleep(rand)

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if nitrosnipe==1:
        if "https://discord.gift/" in message.content.lower():
            print("Nitro link found!")

    if ares==1:
          if message.author == bot.user:
                  return
          elif message.content.lower() == "hi" or message.content.lower() == "hello":
              await message.channel.send(f"Hello {message.author.mention}")
          elif message.content.lower() == "ok":
              await message.channel.send(f"ok")
    
    if publix==1:
          if message.author == bot.user:
                  return
          elif message.content.lower() == "+help" or message.content.lower() == "+info":
              await message.channel.send(f"""``` You have ran the info command for Kat's bot
by running to any command that isnt +help or +tos you are accepting the tos you can view by running +tos
to view a list of commands run +cmd ```""")
          if message.content.lower() == "+test":
              await message.channel.send(f"Hello {message.author.mention}")
          if message.content.lower() == "+tos":
              await message.channel.send("""``` ---[TOS]---
By running any command on the bot you are agreeing to these rules
    Any attempt at running malicious code with the bot will result in a suspension
    The bot will never ask you for your login details or such
    Thr bot will not save any data from your chats
    You will not report the account housing the bot ```""")
          if message.content.lower() == "+real":
              await message.channel.send(f"https://media.tenor.com/qoAGskeO8Y8AAAAC/spin-cat-get-real.gif")
          if message.content.lower() == "+cmd":
              await message.channel.send("""``` Heres a list of commands
              +real (cool cat)
              +test (test)
              +help (+info)
              +tos
              +gpt <text> - (gets you an answer from chatGPT, product of OpenAI at chat.openai.com) ```""")
          if message.content.lower().startswith("+gpt"):
            content = message.content[len("+gpt"):].strip()
            openai.api_key = os.getenv('CHAT_KEY')
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=content,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.4,
            )

            answ = response.choices[0].text.strip()

            await message.channel.send("```ChatGPT >> "+answ+"```")


@bot.command()
async def safefarm(ctx, rep1: int, slep: int):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -safefarm {rep1} {slep}')
    await ctx.message.delete()
    try:
        pass
    except ValueError:
        await ctx.send("``` Enter a number dumbass ```")
    for i in range(int(rep1)):
        yes=str(random.randrange(0, 9999999))
        await ctx.send(yes)
        rand=0.2+int(random.randrange(1, 7))*0.1+slep
        if devmode==1:
            print("         Safe-Farm-spam delay : "+str(float(rand))+"  ("+yes+")")
        else:
            pass
        time.sleep(rand)

@bot.command()
async def whattime(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -whattime')
    await ctx.message.delete()
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S   %D", t)
    await ctx.send(f"""```fix
  🕑 {str(current_time)} ```""")

@bot.command()
async def dick(ctx, duser: discord.User):
    user = ctx.message.author
    print(f'        {user} >> -dick {duser}')
    leng=random.randint(1,40)
    if duser.name=="KatIsBored":
        await ctx.send("``` "+str(duser.name)+"#"+str(duser.discriminator)+"""`s dick
    8"""+"========================="+"="*leng+"ᴅ ```")
    else:
        await ctx.send("``` "+str(duser.name)+"#"+str(duser.discriminator)+"""`s dick
    8"""+"="*leng+"ᴅ ```")

@bot.command()
async def coinflip(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -coinflip')
    await ctx.message.delete()
    result=random.randint(1,2)
    if result==1:
        await ctx.send("``` The coin has landed on heads ```")
    if result==2:
        await ctx.send("``` The coin has landed on tails ```")

@bot.command()
async def m8ball(ctx, ques: str):
    global cmdcoun
    cmdcoun=cmdcoun+1
    user = ctx.message.author
    print(f'        {user} >> -m8ball {ques}')
    answers=["It is certain", "Reply hazy, try again", "Don`t count on it", "It is decidedly so", "Ask again later", "My reply is no", "Better not tell you now", "Without a doubt", "Yes definitely", "Cannot predict now", "Outlook not so good", "Very doubtful", "You may rely on it", "Concentrate and ask again"]
    answer=answers[int(random.randint(0,14))]
    await ctx.send(f"""``` Oh magic 8ball, {ques}?
     8ball >>  """+answer+" ```")

@bot.command()
async def morse(ctx, bef: str):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -morse \"{bef}\"')
    await ctx.message.delete()
    final=translate_to_morse(bef)
    await ctx.send("```"+str(final.replace("  ", " / "))+"```")

@bot.command()
async def demorse(ctx, bef: str):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -demorse \"{bef}\"')
    await ctx.message.delete()
    final=translate_to_lat(bef)
    await ctx.send("```"+str(final.replace("/ ", " "))+"```")

@bot.command()
async def terminal(ctx, cmdi: str):
    global cmdcoun
    cmdcoun = cmdcoun + 1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -terminal {cmdi}')

    if risky == 1:
        cmdii = str(f"{str(cmdi)}_{str(random.randint(0, 10000000))}.txt")
        cmdii = cmdii.replace(" ", "_")
        
        script_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        print(script_dir)
        
        isExist = os.path.exists(os.path.join(script_dir, "Terminal_output"))
        if not isExist:
            os.makedirs(os.path.join(script_dir, "Terminal_output"))
            print("          [INFO] Terminal_output has been created")
        
        cmdiii = os.path.join(script_dir, "Terminal_output", cmdii)
        filee = os.path.join("Terminal_output", cmdii)
        open(filee, "x").close()
        
        if getattr(sys, 'frozen', False):
            subprocess.run([sys.executable, __file__, cmdi, ">>", cmdiii], cwd=script_dir)
        else:
            os.system(str(cmdi + " >> " + cmdiii))
        
        with open(filee, "r") as fil:
            out = fil.read()
        
        await ctx.send("""```css
[⌨ """+cmdi+""" ⌨] ```""")
        await ctx.send(f"""```ansi
[2;36m{out}[0m[2;40m[0m```""")

@bot.command()
async def morsetable(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -morsetable')
    await ctx.send("""```css
[Morse code table]```""")
    await ctx.send("""```A	. _	 	    |     1   . _ _ _ _	 
B	_ . . .	     |     2   . . _ _ _	 
C	_ . _ .	     |     3   . . . _ _	 
D	_ . .	       |     4   . . . . _	 
E	.	 	      |     5   . . . . .	 
F	. . _ .	     |     6   _ . . . .
G	_ _ .	       |     7   _ _ . . .
H   . . . .	      |     8   _ _ _ . .
I	. .	 	    |     9   _ _ _ _ .
J	. _ _ _	     |     0   _ _ _ _ _
K	_ . _	 	  |   
L	. _ . .	 	|  
M	_ _	 	    |     ,   _ _ . . _ _
N	_ .	         |     .   . _ . _ . _
O	_ _ _	       |     ?   . . _ _ . .
P	. _ _ .	     |     -   _ . . . . _
Q	_ _ . _	     |     (   _ . _ _ .
R	. _ .	       |     )   _ . _ _ . _
S	. . .	       |     =   _ . . . _
T	_	           |     +   . _ . _ .
U	. . _           |     :   _ _ _ . . .
V	. . . _	 	|     ;   _ . _ . _ .
W	. _ _	       |     '   . _ _ _ _ .
X	_ . . _	     |     "   . _ . . _ .
Y	_ . _ _	     |     ×   _ . . _
Z	_ _ . .         |     T̲   . . _ _ . _ ```""")

@bot.command()
async def edit(ctx, rep1, con1):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -edit {rep1} {con1}')
    await ctx.message.delete()
    async for msg in ctx.message.channel.history(limit=int(rep1)):
        if msg.author.id == bot.user.id:
            time.sleep(0.5)
            await msg.edit(content=con1)

@bot.command()
async def delete(ctx, rep1: int):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -delete {rep1}')
    await ctx.message.delete()
    async for msg in ctx.message.channel.history(limit=rep1):
        if msg.author.id == bot.user.id:
            time.sleep(0.5)
            await msg.delete()

@bot.command()
async def sqroot(ctx, num1: int):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -sqroot {num1}')
    if num1==6413607225:
        await ctx.send("``` Square root of "+str(num1)+" >>  BOOBS ```")
    else:
        num2=math.sqrt(num1)
        await ctx.send("``` Square root of "+str(num1)+" >>  "+str(num2)+" ```")

@bot.command()
async def power(ctx, num1: float, num2: float):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -power {num1} {num2}')
    num3=math.pow(num1, num2)
    num2p=num2
    if num2p==int(num2p):
        num2=int(num2)
    else:
        pass
    if num1==int(num1):
        num1=int(num1)
    else:
        pass
    num2=str(num2)
    num20=str(num2.replace("0", "⁰"))
    num21=num20.replace("1", "¹")
    num22=num21.replace("2", "²")
    num22=num22.replace("3", "³")
    num22=num22.replace("4", "⁴")
    num22=num22.replace("5", "⁵")
    num22=num22.replace("6", "⁶")
    num22=num22.replace("7", "⁷")
    num22=num22.replace("8", "⁸")
    num22=num22.replace(".", "·")
    num23=num22.replace("9", "⁹")
    if num3==80085:
        await ctx.send("```"+str(num1)+num23+" >>  BOOBS ```")
    else:
        if num2p+num1==int(num2p+num1):
            await ctx.send("```"+str(num1)+num23+" >>  "+str(int(num3))+" ```")
        else:
                await ctx.send("```"+str(num1)+str(num23)+" >>  "+str(num3)+" ```")

@bot.command()
async def v7wpa(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -v7wpa')
    await ctx.message.delete()
    await ctx.send("""```Data from the vault 7 of wikileaks.org
"The increasing sophistication of surveillance techniques has drawn comparisons with George Orwell's 1984, but "Weeping Angel", developed by the CIA's Embedded Devices Branch (EDB), which infests smart TVs, transforming them into covert microphones, is surely its most emblematic realization."```""")

@bot.command()
async def v7olc(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -v7olc')
    await ctx.message.delete()
    await ctx.send("""```Data from the vault 7 of wikileaks.org
The OutlawCountry project of the CIA that targets computers running the Linux operating system. OutlawCountry allows for the redirection of all outbound network traffic on the target computer to CIA controlled machines for ex- and infiltration purposes.```""")

@bot.command()
async def v7elsa(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -v7elsa')
    await ctx.message.delete()
    await ctx.send("""```Data from the vault 7 of wikileaks.org
ELSA is a geo-location malware for WiFi-enabled devices like laptops running the Micorosoft Windows operating system. Once persistently installed on a target machine using separate CIA exploits, the malware scans visible WiFi access points and records the ESS identifier, MAC address and signal strength at regular intervals. To perform the data collection the target machine does not have to be online or connected to an access point; it only needs to be running with an enabled WiFi device. If it is connected to the internet, the malware automatically tries to use public geo-location databases from Google or Microsoft to resolve the position of the device and stores the longitude and latitude data along with the timestamp.```""")

@bot.command()
async def v7chb(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -v7chb')
    await ctx.message.delete()
    await ctx.send("""```Data from the vault 7 of wikileaks.org
CherryBlossom provides a means of monitoring the Internet activity of and performing software exploits on Targets of interest. In particular, CherryBlossom is focused on compromising wireless networking devices```""")

@bot.command()
async def pi(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -pi')
    await ctx.message.delete()
    await ctx.send("```𝜋 >> 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954```")

@bot.command()
async def translate(ctx, txt: str, lan1: str, lan2: str):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    print(f'        {user} >> -translate \"{txt}\" {lan1} {lan2}')
    if txt=="help":
        await ctx.send(f"""```diff
        +Translator help+  ```""")
        await ctx.send(""""```
```""")
    else:
        await ctx.send("``` "+Translator().translate(txt, lan1, lan2)+" ```")

@bot.command()
async def bsod(ctx):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    await ctx.message.delete()
    user = ctx.message.author
    print(f'        {user} >> -bsod')
    await ctx.send(r"<ms-cxh-full://0>")

@bot.command()
async def bc(ctx, arg2, arg1):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    await ctx.message.delete()
    user = ctx.message.author
    print(f"        {user} >> -bc "+arg2+" "+arg1+"")
    times = int(arg1)
    for _ in range(times):
        for channel in ctx.message.guild.text_channels:
            slep=random.randint(0, 10)//10
            slep=slep+1
            time.sleep(slep)
            try:
                await channel.send(arg2)
            except:
                continue

@bot.command()
async def cmd(ctx, cata: str=None):
    global cmdcoun
    cmdcoun=cmdcoun+1
    os.system(f'title Elixir Self-Bot ┋ Prefix = "-" ┋ Commands ran = {cmdcoun}')
    user = ctx.message.author
    if cata is None:
        print(f'        {user} >> -cmd')
    else:
        print(f'        {user} >> -cmd '+cata)
    await ctx.message.delete()
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S   %D", t)
    if cata is None:
        await ctx.send(f"""``` ☸ [ Elixir help ] Prefix is (-) ☸
 | Catagories :
 |   [ useful ]
 |   [ fun ]
 |   [ malicious ]
 |   [ other ]
 ╰----------------------------------------------------------------------------------------------``````fix
  ▣ {str(current_time)} ```""")
    elif cata=="useful" or cata=="[useful]" or cata=="[ useful ]" or cata=="use" or cata=="u":
        await ctx.send(f"""``` ☸ [ Useful ] ☸
 | ping - (pong)
 | restart - (restarts the bot - stops current task)
 | ares - (toggles auto respond)
 | publix - (toggles public commands WIP)
 | gpt <text> - (gets an answer from chatGPT-3 to your text)
 | purge <num> - (deletes a set amount of messages)
 | edit <num> <text> - (edits messages to the text)
 | delete <num> - (deletes a set amount of messages from anyone)
 | base64e <text> - ("encrypts" your text in base64)
 | base64de <text> - ("decrypts" the text using base64)
 | userinfo <@> - (gives somewhat useful info about a user)
 | google <text> - (makes a google link with the text)
 | urban <text> - (makes an urban dictionary link with the text)
 | whattime - (tells you the time - totally useless)
 | morse <text> - (turns your text into morse code)
 | demorse <text> - (turns the morse code into text)
 | morsetable - (gives a table of morse characters)
 | terminal <text> - (runs the text as a command in terminal)
 | sqroot <num> - (gives the square root of the number)
 | pi - (gives the value of pi)
 | power <num> <num> - (gives the answer to X^x)
 | backup - (saves your friend list and your servers)
 ╰----------------------------------------------------------------------------------------------``````fix
  ▣ {str(current_time)} ```""")
    elif cata=="fun" or cata=="[fun]" or cata=="[ fun ]" or cata=="f" or cata=="funny":
        await ctx.send(f"""``` ☸ [ Fun ] ☸
 | real - (coolass cat)
 | react <text> <num> - (reacts to messages with an emoji a set number of times)
 | play <txt> - (sets your play activity to X)
 | realspam <num> - (sends multiple coolass cats)
 | nerdspam <num> <num> - (sends X amount of nerd amojies X amount of times)
 | nerdgifspam <num> - (sends an X amount of nerd gifs)
 | dick <@> - (sends the persons supposed dick length)
 | coinflip - (flips a coin)
 | m8ball <text> - (the magic 8 ball says...)
 | v7olc - (CIA dont raid me UwU)
 | v7elsa - (CIA dont raid me UwU)
 | v7wpa - (CIA dont raid me UwU)
 | v7chb - (CIA dont raid me UwU)
 ╰----------------------------------------------------------------------------------------------``````fix
   ▣ {str(current_time)} ```""")
    elif cata=="malicious" or cata=="[Malicious]" or cata=="[ malicious ]" or cata=="m" or cata=="mal":
        await ctx.send(f"""``` ☸ [ Malicious ] ☸
 | auditflood <num> - (floods the audit logs)
 | nickall <text> - (changes everyones nickname)
 | raid - (shadow legends)
 | mk_channels <num> <text> - (makes channels)
 | del_channels - (deletes channels - you're a dumbass)
 | nuke <num> <text> <text> - (slightly not nice command)
 | delserver - (deletes a server without verification)
 | cloneserver - (clones the server)
 | massm - (mentions a bunch of users)
 | spam <text> <num> <num> - (self explanitory)
 | bsod - (click the link)
 | everyonespam - (mentions a bunch of users aswell)
 ╰----------------------------------------------------------------------------------------------``````fix
   ▣ {str(current_time)} ```""")
    elif cata=="other" or cata=="[other]" or cata=="[ other ]" or cata=="o" or cata=="otter":
        await ctx.send(f"""``` ☸ [ Other ] ☸
 | textwall - (sends a bunch of text to block out previous messages)
 | clearcmd - (clears the command prompt for better user experience)
 | safefarm <num> <num> - (farms server xp in a way thats not detectable via bot)
 | bc <text> <num> - (sends the message in all channels X amount of times)
 ╰----------------------------------------------------------------------------------------------``````fix
   ▣ {str(current_time)} ```""")
grouplock_group=os.getenv("GROUP")
TOKEN=os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
