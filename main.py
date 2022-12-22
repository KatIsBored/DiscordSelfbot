import discord 
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext import tasks
import time
import random
import os
import requests
from morse_code_translator.translator import translate_to_lat
from morse_code_translator.translator import translate_to_morse
from google_translate_py import Translator
import math
from os import path
from colorama import Fore, Back, Style


##devmode - dont use outside of testing
devmode=1
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

load_dotenv()

bot=commands.Bot(command_prefix="-", self_bot=True)

@bot.event
async def on_connect():
    print(r"""      _________      __   _____        __________         __   
     /   _____/ ____ |  |_/ ____\       \______   \ _____/  |_ 
     \_____  \_/ __ \|  |\   __\  ______ |    |  _//  _ \   __\
     /        \  ___/|  |_|  |   /_____/ |    |   (  <_> )  |  
    /_______  /\___  >____/__|           |______  /\____/|__|  
            \/     \/                           \/             
            
--------------------[Kat's self-bot activated]---------------------
 
 """)


@bot.command()
async def ping(ctx):
    user = ctx.message.author
    print(f'{user} >> -ping')
    await ctx.send(f"``` Pong! >> {int(bot.latency*1000)}ms ```")

@bot.command()
async def clearcmd(ctx):
    user = ctx.message.author
    print(f'{user} >> -clearcmd')
    print("Reloading...")
    time.sleep(2)
    os.system("cls")
    await ctx.send(f"``` Clearing the terminal output ```")
    time.sleep(0.5)
    print(r"""      _________      __   _____        __________         __   
     /   _____/ ____ |  |_/ ____\       \______   \ _____/  |_ 
     \_____  \_/ __ \|  |\   __\  ______ |    |  _//  _ \   __\
     /        \  ___/|  |_|  |   /_____/ |    |   (  <_> )  |  
    /_______  /\___  >____/__|           |______  /\____/|__|  
            \/     \/                           \/             
            
--------------------[Kat's self-bot activated]---------------------
 
 """)
    

@bot.command()
async def real(ctx):
    user = ctx.message.author
    print(f'{user} >> -real')
    await ctx.send("https://media.tenor.com/qoAGskeO8Y8AAAAC/spin-cat-get-real.gif")

@bot.command()
async def randomnum(ctx, num1: int, num2: int):
    user = ctx.message.author
    print(f'{user} >> -randomnum {num1} {num2}')
    num1r2=random.randint(num1,num2)
    await ctx.send("``` Random number between "+str(num1)+" and "+str(num2)+" >>  "+str(num1r2)+" ```")

@bot.command()
async def userinfo(ctx, user: discord.User):
    user = ctx.message.author
    print(f'{user} >> -userinfo {user}')
    await ctx.send("``` Username >> "+str(user.name)+"#"+str(user.discriminator)+"""
    ID >> """+str(user.id)+"""
    Account created >> """+str(user.created_at)+"""
    Bot? >> """+str(user.bot)+"```")

@bot.command()
async def google(ctx, q: str):
    user = ctx.message.author
    print(f'{user} >> -google {q}')
    qq=q.replace(" ", "+")
    await ctx.send(f"""```ini
[https://www.google.com/search?q={qq}] ```""")

@bot.command()
async def urban(ctx, q: str):
    user = ctx.message.author
    print(f'{user} >> -urban {q}')
    qq=q.replace(" ", "+")
    await ctx.send(f"""```ini
[https://www.urbandictionary.com/define.php?term={qq}] ```""")

@bot.command()
async def spam(ctx, tx: str, rep1: int, slep: int):
    user = ctx.message.author
    print(f'{user} >> -spam {tx} {rep1} {slep}')
    await ctx.message.delete()
    try:
        print(int(rep1))
        pass
    except ValueError:
        await ctx.send("``` Enter a number dumbass ```")
    for i in range(int(rep1)):
        await ctx.send(tx)
        rand=0.2+int(random.randrange(1, 7))*0.1+slep
        if devmode==1:
            print("Spam delay : "+str(float(rand)))
        else:
            pass
        time.sleep(rand)

@bot.command()
async def realspam(ctx, rep1: int):
    user = ctx.message.author
    print(f'{user} >> -realspam {rep1}')
    await ctx.message.delete()
    try:
        print(int(rep1))
        pass
    except ValueError:
        await ctx.send("``` Enter a number dumbass ```")
    for i in range(int(rep1)):
        await ctx.send("https://media.tenor.com/qoAGskeO8Y8AAAAC/spin-cat-get-real.gif")
        rand=0.3+int(random.randrange(1, 9))*0.1
        if devmode==1:
            print("Real-spam delay : "+str(float(rand)))
        else:
            pass
        time.sleep(rand)

@bot.command()
async def nerdspam(ctx, repn: int, nloop: int):
    user = ctx.message.author
    print(f'{user} >> -nerdspam {repn} {nloop}')
    await ctx.message.delete()
    for i in range(nloop):
        if(nloop>1):
            await ctx.send(":nerd:"*repn)
            nsleep=0.1+int(random.randrange(2, 7)*0.1)
            print("Nerd-spam delay : "+str(nsleep)+"s")
            time.sleep(nsleep)
        if nloop==1:
            await ctx.send(":nerd:"*repn)

@bot.command()
async def nerdgifspam(ctx, repngif: int):
    user = ctx.message.author
    print(f'{user} >> -nerdgifspam {repngif}')
    await ctx.message.delete()
    for i in range(repngif):
        await ctx.send("https://tenor.com/view/nerd-nerd-emoji-nerd-emoji-meme-accttually-nerd-emoji-gif-26120328")
        nsleep=0.2+random.randint(1, 6)*0.1
        time.sleep(nsleep)
        print("Nerdspam delay : "+str(nsleep)+"s")

@bot.command()
async def textwall(ctx):
    user = ctx.message.author
    print(f'{user} >> -textwall')
    await ctx.message.delete()
    await ctx.send("."+"""
    
    """*160+".")

@bot.command()
async def everyonespam(ctx, rep1: int):
    user = ctx.message.author
    print(f'{user} >> -everyonespam {rep1}')
    await ctx.message.delete()
    try:
        print(int(rep1))
        pass
    except ValueError:
        await ctx.send("``` Enter a number dumbass ```")
    for i in range(int(rep1)):
        await ctx.send("@everyone")
        rand=0.3+int(random.randrange(1, 9))*0.1
        if devmode==1:
            print("Everyone-spam delay : "+str(float(rand)))
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

@bot.command()
async def safefarm(ctx, rep1: int, slep: int):
    user = ctx.message.author
    print(f'{user} >> -safefarm {rep1} {slep}')
    await ctx.message.delete()
    try:
        print(int(rep1))
        pass
    except ValueError:
        await ctx.send("``` Enter a number dumbass ```")
    for i in range(int(rep1)):
        yes=str(random.randrange(0, 9999999))
        await ctx.send(yes)
        rand=0.2+int(random.randrange(1, 7))*0.1+slep
        if devmode==1:
            print("Safe-Farm-spam delay : "+str(float(rand))+"  ("+yes+")")
        else:
            pass
        time.sleep(rand)

@bot.command()
async def whattime(ctx):
    user = ctx.message.author
    print(f'{user} >> -whattime')
    await ctx.message.delete()
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S   %D", t)
    await ctx.send(f"""```fix
  🕑 {str(current_time)} ```""")

@bot.command()
async def dick(ctx, user: discord.User):
    user = ctx.message.author
    print(f'{user} >> -dick {user}')
    leng=random.randint(1,40)
    await ctx.send("``` "+str(user.name)+"#"+str(user.discriminator)+"""`s dick
    8"""+"="*leng+"ᴅ ```")

@bot.command()
async def coinflip(ctx):
    user = ctx.message.author
    print(f'{user} >> -coinflip')
    await ctx.message.delete()
    result=random.randint(1,2)
    if result==1:
        await ctx.send("``` The coin has landed on heads ```")
    if result==2:
        await ctx.send("``` The coin has landed on tails ```")

@bot.command()
async def m8ball(ctx, ques: str):
    user = ctx.message.author
    print(f'{user} >> -m8ball {ques}')
    answers=["It is certain", "Reply hazy, try again", "Don`t count on it", "It is decidedly so", "Ask again later", "My reply is no", "Better not tell you now", "Without a doubt", "Yes definitely", "Cannot predict now", "Outlook not so good", "Very doubtful", "You may rely on it", "Concentrate and ask again"]
    answer=answers[int(random.randint(0,14))]
    await ctx.send(f"""``` Oh magic 8ball, {ques}?
     8ball >>  """+answer+" ```")

@bot.command()
async def morse(ctx, bef: str):
    user = ctx.message.author
    print(f'{user} >> -morse \"{bef}\"')
    await ctx.message.delete()
    final=translate_to_morse(bef)
    await ctx.send("```"+str(final.replace("  ", " / "))+"```")

@bot.command()
async def demorse(ctx, bef: str):
    user = ctx.message.author
    print(f'{user} >> -demorse \"{bef}\"')
    await ctx.message.delete()
    final=translate_to_lat(bef)
    await ctx.send("```"+str(final.replace("/ ", " "))+"```")

@bot.command()
async def terminal(ctx, cmdi: str):
    user = ctx.message.author
    print(f'{user} >> -terminal {cmdi}')
    if risky==1:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S   %D", t)
        cmdii=str(f"{str(cmdi)}_{str(random.randint(0, 10000000))}.txt")
        cmdii=cmdii.replace(" ", "_")
        cmdiii=str(r"C:\Users\Kat\Desktop\Self.Bot\Terminal_output\\"+str(cmdii))
        filee=str(f"Terminal_output\{cmdii}")
        fileee=open(str(filee), "x")
        fileee.close()
        os.system(str(cmdi+" >> "+cmdiii))
        fil=open(str(filee), "r")
        out=fil.read()
        await ctx.send("""```css
[⌨ """+cmdi+""" ⌨] ```""")
        await ctx.send(f"""``` {out} ```""")
        fileee.close()
    

@bot.command()
async def morsetable(ctx):
    user = ctx.message.author
    print(f'{user} >> -morsetable')
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
    user = ctx.message.author
    print(f'{user} >> -edit {rep1} {con1}')
    await ctx.message.delete()
    async for msg in ctx.message.channel.history(limit=int(rep1)):
        if msg.author.id == bot.user.id:
            time.sleep(0.5)
            await msg.edit(content=con1)

@bot.command()
async def delete(ctx, rep1: int):
    user = ctx.message.author
    print(f'{user} >> -delete {rep1}')
    await ctx.message.delete()
    async for msg in ctx.message.channel.history(limit=rep1):
        if msg.author.id == bot.user.id:
            time.sleep(0.5)
            await ctx.message.delete()

@bot.command()
async def sqroot(ctx, num1: int):
    user = ctx.message.author
    print(f'{user} >> -sqroot {num1}')
    if num1==6413607225:
        await ctx.send("``` Square root of "+str(num1)+" >>  BOOBS ```")
    else:
        num2=math.sqrt(num1)
        await ctx.send("``` Square root of "+str(num1)+" >>  "+str(num2)+" ```")

@bot.command()
async def power(ctx, num1: float, num2: float):
    user = ctx.message.author
    print(f'{user} >> -power {num1} {num2}')
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
async def pi(ctx):
    user = ctx.message.author
    print(f'{user} >> -pi')
    await ctx.message.delete()
    await ctx.send("```𝜋 >> 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954```")

@bot.command()
async def translate(ctx, txt: str, lan1: str, lan2: str):
    user = ctx.message.author
    print(f'{user} >> -translate \"{txt}\" {lan1} {lan2}')
    if txt=="help":
        await ctx.send(f"""```diff
        +Translator help+  ```""")
        await ctx.send(""""```
```""")
    else:
        await ctx.send("``` "+Translator().translate(txt, lan1, lan2)+" ```")

@bot.command()
async def cmd(ctx):
    user = ctx.message.author
    print(f'{user} >> -cmd')
    await ctx.message.delete()
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S   %D", t)
    await ctx.send(f"""``` ☸ [Kat's bot help] Prefix is (-) ☸
 | cmd - (shows this)
 | cmds - (shows a safe version of cmd)
 | ping - (pong)
 | real - (sends a coolass cat)
 | realspam <num> - (sends a set amount of coolass cats)
 | randomnum <num> <num> - (selects a random number between the 2)
 | userinfo <@> - (gives basic info about the user)
 | textwall - (creates a large wall of text making the chat look new)
 | everyonespam <num> - (spams @everyone a set amount of times)
 | nerdspam <num> <num> - (spams the nerd emoji a set amount of times in sets)
 | nerdgifspam <num> - (spams the nerd gif a set amout of times)
 | safefarm <num> <num> - (sends a set amount of random messages for farming server xp)
 | coinflip - (flips a coin)
 | m8ball <Question> - (answers questions - use "#" for the question)
 | morsetable - (shows a morse table)
 | morse <txt> - (turns the text into morse code)
 | demorse <txt> - (turns the morse code into text)
 | whattime - (shows you the time and date)
 | google <txt> - (google anything)
 | urban <txt> - (check urban dictionary for the term)
 | dick <@> - (shows how long someones dick is)
 | sqroot <num> - (calculates the square root of the number)
 | pi - (shows the value of pi)
 | power <num> <num> - (calculates the value of num1 to the power of num2)
 | terminal <txt> - (runs the text you sent as a terminal command)
 | spam <txt> <num> <num> - (spam anything however much youd like)
 | edit <num> <txt> - (edits a specified amount of messages to cerain text)
 | clearcmd - (clears the terminal - just for a better view experience)
 ╰----------------------------------------------------------------------------------------------``````fix
  ▣ {str(current_time)} ```""")

@bot.command()
async def cmds(ctx):
    user = ctx.message.author
    print(f'{user} >> -cmds')
    await ctx.message.delete()
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S   %D", t)
    await ctx.send(f"""``` ☸ [help] Prefix is (-) ☸
 | cmds - (shows this)
 | ping - (pong)
 | real - (sends a coolass cat)
 | realspam <num> - (sends a set amount of coolass cats)
 | randomnum <num> <num> - (selects a random number between the 2)
 | userinfo <@> - (gives basic info about the user)
 | textwall - (creates a large wall of text making the chat look new)
 | everyonespam <num> - (spams @everyone a set amount of times)
 | nerdspam <num> <num> - (spams the nerd emoji a set amount of times in sets)
 | nerdgifspam <num> - (spams the nerd gif a set amout of times)
 | safefarm <num> <num> - (sends a set amount of random messages for farming server xp)
 | coinflip - (flips a coin)
 | m8ball <Question> - (answers questions - use "#" for the question)
 | morsetable - (shows a morse table)
 | morse <txt> - (turns the text into morse code)
 | demorse <txt> - (turns the morse code into text)
 | whattime - (shows you the time and date)
 | google <txt> - (google anything - use 1 word only)
 | urban <txt> - (check urban dictionary for the term)
 | sqroot <num> - (calculates the square root of the number)
 | pi - (shows the value of pi)
 | power <num> <num> - (calculates the value of num1 to the power of num2)
 | terminal <txt> - (runs the text you sent as a terminal command)
 | spam <txt> <num> <num> - (spam anything however much youd like)
 | edit <num> <txt> - (edits a specified amount of messages to cerain text)
 | clearcmd - (clears the terminal - just for a better view experience)
 ╰----------------------------------------------------------------------------------------------``````fix
  ▣ {str(current_time)} ```""")

TOKEN=os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
