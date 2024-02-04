import nextcord
import secrets
import random
from nextcord.ext import commands
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import io

TOKEN = 'MTE3ODAzOTM0NTYyMjU1MjYwNg.GcLMee.gXiO4Ql2-ykeDqMPx23LsH53G5xKr8t8sUM9pM'
bot = commands.Bot(command_prefix="!", intents=nextcord.Intents.all())
weather_api_key =  "fdaf508d1560de1ec3a73db9e31843b2"

@bot.event
async def on_ready():
    print('Бот готов')
    await bot.change_presence(activity=nextcord.Game(name='Helping Rfgfgfgfgf (his creator)'))

@bot.command()
async def on_message(message):
    if message.content == '!join_voice':
        channel = message.author.voice.channel
        voice_channel = await channel.connect()
        await message.channel.send(f'Joined voice channel: {channel.name}')

@bot.command()
async def weather(ctx, город):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={город}&appid={weather_api_key}'
    response = requests.get(url)
    weather_data = response.json()
    if response.status_code == 200:
        температура = weather_data['main']['temp']
        описание = weather_data['weather'][0]['description']
        await ctx.send(f'Текущая погода в {городе}: Температура: {температура}°C, Описание: {описание}')
    else:
        await ctx.send('Не удалось получить данные о погоде. Пожалуйста, убедитесь, что указан правильный город и ключ API.')

@bot.command(name='generate_password', help='Generates a random password')
async def generate_password(ctx):
    password = secrets.token_hex(10) 
    await ctx.send(f'Your random password: `{password}`')


@bot.command()
async def pon(ctx):
    await ctx.send('I pon that you pon.')   

@bot.command()
async def hello(ctx):
    await ctx.send('Hi! Welcome to rfgfgfgfgf server!')

@bot.command()
async def info(ctx):
    await ctx.send('I am bot helper in this server. My creator is rfgfgfgfgf & shlepa.')


@bot.command(name='create_image')
async def create_image(ctx, текст: str):
    image = Image.new('RGB', (400, 200), color='white')
    
    draw = ImageDraw.Draw(image)
    
    font = ImageFont.load_default()
    
    draw.text((10, 10), текст, fill='black', font=font)
    
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format='PNG')
    
    img_byte_array.seek(0)
    
    await ctx.send(file=nextcord.File(img_byte_array, 'image.png'))

@bot.command()
async def current_time(ctx):
    текущее_время = datetime.now().strftime('%H:%M:%S')
    await ctx.send(f'Current time: {текущее_время}')

#@bot.command()
#async def weather(ctx, город):
    #await ctx.send(f'Текущая погода в {город}: ...')


@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'Your ping is: {latency} мс')

@bot.command(name='avatar')
async def avatar(ctx, user: nextcord.Member = None):
    if user == None:
        user = ctx.author
    embed = nextcord.Embed(title = f'Аватарка {user}а', color=0xe74c3c).set_image(url = user.avatar.url)
    await ctx.send(embed=embed)

@bot.command(name='user_info')
async def user_info(ctx, пользователь: nextcord.Member = None):
    пользователь = пользователь or ctx.author
    created_at = пользователь.created_at.strftime('%Y-%m-%d %H:%M:%S')
    joined_at = пользователь.joined_at.strftime('%Y-%m-%d %H:%M:%S')
    await ctx.send(f'User information {пользователь.name}:\n'
                   f'ID: {пользователь.id}\n'
                   f'Created: {created_at}\n'
                   f'Joined: {joined_at}')
@bot.command(name="add_roles")
async def add_roles(ctx, роль: nextcord.Role = None):
    if роль == None:
        await ctx.send("You need to chose your role")
        return
    await ctx.author.add_roles(роль)
    await ctx.send(f'Роль {роль.name} успешно присвоена!')


@bot.command(name='join_voice')
async def join_voice(ctx, channel: nextcord.VoiceChannel = None):
    if channel is None:
        await ctx.send("Choose a voice channel")
        return

    if ctx.author.voice is None or ctx.author.voice.channel is None:
        await ctx.send("You are not in a voice channel.")
        return
    if ctx.voice_client is not None:
        await ctx.send("I'm already in a voice channel. Use !leave_voice to disconnect.")
        return
    voice_channel = ctx.author.voice.channel
    vc = await voice_channel.connect()

    await ctx.send(f"Joined {voice_channel.name}")

@bot.command(name="leave_voice")
async def leave_voice(ctx, channel: nextcord.channel = None):
    if channel == None:
        await ctx.send("Chose your channel")
        return
    await ctx.voice_client.disconnect()

@bot.command()
async def game(ctx):
    result = random.choice(['Орел', 'Решка'])
    await ctx.send(f'Выпало: {result}')



bot.run("PONPONPON")
