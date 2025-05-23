import discord
from discord.ext import commands
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def en_lines():
    print(f'Tu bot {bot.user} esta en linea')

@bot.command()
async def contaminacion(ctx,*,mensaje:str):
    
    mensaje = mensaje.lower().strip()

    if mensaje == "que es":
        await ctx.send("La contaminacion es la presencia de elementos nocivos en el aire y en la atmosfera")
        nombre_imagen = random.choice(os.listdir('contamination'))   
        with open(f'contamination/{nombre_imagen}', 'rb') as f:
        
            picture = discord.File(f)
        
        await ctx.send(file=picture) 

    elif mensaje == "que causa":
        await ctx.send("La contaminacion debilita la atmosfera dejando entar mas rayos del sol. Ademas contamina el aire llenandolo de dioxido de carbono(CO2)")
        nombre_imagen = random.choice(os.listdir('contamination'))   
        with open(f'contamination/{nombre_imagen}', 'rb') as f:
        
            picture = discord.File(f)
        
        await ctx.send(file=picture)
    
    elif mensaje == "como prevenirla":
        await ctx.send("Puedes prevenir la contaminacion sembrando arboles, usando transporte publico o electrico, reduciendo el uso de plasticos, reciclando, ETC")
        nombre_imagen = random.choice(os.listdir('contamination'))   
        with open(f'contamination/{nombre_imagen}', 'rb') as f:
        
            picture = discord.File(f)
        
        await ctx.send(file=picture)

token = ""

bot.run(token)
