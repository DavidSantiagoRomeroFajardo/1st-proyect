import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def en_lines():
    print(f'Tu bot {bot.user} esta en linea')
    
@bot.command()
async def saludar(ctx,*,mensaje:str):
    
    mensaje = mensaje.lower().strip()
    
    if mensaje == 'hola':
        await ctx.send('Hola, ¿cómo estás?')
        
    elif mensaje == 'klk':
        
        await ctx.send('Klk, ¿todo bien?')
        
    elif mensaje == 'buenas':
            
        await ctx.send('Buenas, ¿qué tal?')
    
    else:
        
        await ctx.send('SALUDA BIEN!!!')

@bot.command()
async def despedir(ctx,*,mensaje:str):
    
    mensaje = mensaje.lower().strip()
    
    if mensaje == 'adios':
        await ctx.send('Adios, que te vaya bien')
        
    elif mensaje == 'hasta luego':
        
        await ctx.send('Hasta luego, nos vemos pronto')
        
    elif mensaje == 'chao':
            
        await ctx.send('Chao, gracias por la charla')
    
    else:
        
        await ctx.send('Eso es una despedida o... Lo tomare como despedida')
        
@bot.command()
async def test(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')

token = ''
        
bot.run(token)