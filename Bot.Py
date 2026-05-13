# from modelo import *
import pyttsx3
from googletrans import Translator
import requests
import discord
from discord.ext import commands
import random
import requests
import random
import bot_logic


intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)
token=None
import os

ruta = os.path.join(os.path.dirname(__file__), "botToken.txt")

with open(ruta, "r") as file:
    token = file.read()
print(token)
datos_interesantes = [
    "Los pulpos tienen tres corazones 🐙",
    "La miel nunca se descompone 🍯",
    "Los tiburones existen desde antes que los árboles 🦈",
    "El cerebro humano usa alrededor del 20% de la energía del cuerpo 🧠",
    "Las vacas tienen mejores amigas 🐄",
    "Un día en Venus es más largo que un año en Venus 🪐",
    "Los plátanos son radiactivos 🍌",
    "Los delfines tienen nombres entre ellos 🐬",
    "El agua caliente se congela más rápido que la fría (efecto Mpemba) ❄️",
    "Las hormigas no duermen 🐜",
    "El corazón de una ballena azul puede pesar más que un coche 🐋",
    "Los gatos pueden hacer más de 100 sonidos diferentes 🐱",
    "Los humanos comparten el 60% de su ADN con los plátanos 🍌",
    "Un rayo es 5 veces más caliente que la superficie del sol ⚡",
    "Los canguros no pueden caminar hacia atrás 🦘",
    "El espacio no tiene sonido 🌌",
    "Los koalas duermen hasta 22 horas al día 🐨",
    "El ojo de un avestruz es más grande que su cerebro 🐦",
    "Las estrellas de mar pueden regenerar sus brazos ⭐",
    "El monte Everest crece unos milímetros cada año 🏔️"
]

prefix="$"
help_textS =f"""
Comandos:

!genpass → Genera contraseña
!duck → Imagen de pato
!randomN → Número aleatorio
!randomfacts → Dato curioso
"""
# -----------------------
# COMANDO: genpass
# -----------------------
def get_fact():
    url="https://uselessfacts.jsph.pl/random.json"
    res=requests.get(url)
    if res.status_code==200:
        data=res.json()
        return data.get("text")
    else:
        return "not founded"
def speak(text):
    engine1=pyttsx3.init()
    engine1.say(text)
    engine1.runAndWait()
@bot.command()
async def SOS(ctx):
    await ctx.send(help_textS)
@bot.command()
async def fact(ctx):
    dato=get_fact()
    trans=Translator()
    trad=trans.translate(dato,dest="es")
    await ctx.send(trad.text)
    await ctx.send(dato)

@bot.command()
async def flip(ctx):
    chosed=bot_logic.flip_coin()
    await ctx.send(chosed)
@bot.command()
async def emoji(ctx):
    chosed=bot_logic.gen_emodji()
    await ctx.send(chosed) 
@bot.command()
async def genpass(ctx, long: int = 8):
    chars = "+-/*!&$#?=@<>"
    password = "".join(random.choice(chars) for _ in range(long))
    await ctx.send(password)

# -----------------------
# COMANDO: duck
# -----------------------
def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    return res.json()['url']

@bot.command()
async def duck(ctx):
    await ctx.send(get_duck_image_url())
    
@bot.command()
async def randomN(ctx):
    number=random.randint(1,100)
    await ctx.send(number)
@bot.command()
async def randomfacts(ctx):
    choised=random.choice(datos_interesantes)
    await ctx.send(choised)
# -----------------------
# EVENTO READY
# -----------------------
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


def Get_wheater(City):
    url=f"https://wttr.in/{City}?format=%C+%t"
    res=requests.get(url)
    if res.status_code==200: 
        return res.text.strip()
    else:
        return "No se ha podido acceder."

@bot.command()
async def Wheather(ctx,city:str):
    info=Get_wheater(city)
    await ctx.send(info)
    speak(info)
def speak(info):
    engine=pyttsx3.init()
    engine.say(info)
    engine.runAndWait()



# -----------------------
# INICIAR BOT
# -----------------------
bot.run(token)

