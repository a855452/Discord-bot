#載入Discord 模組
import discord
from discord.ext import commands
import json,asyncio,datetime

#載入json模組
import json
#載入ranom(隨機)模組
import random

#載入setting.json檔案
#請於同格資料夾內新增setting.json
#建立資料
#{
#    "TOKEN":"your token",
#   "pic": ["圖片位置"],
#    "txt": ["泡麵","牛排","便當","小七","水餃","不要吃"]
#}
with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

#前綴
bot = commands.Bot(command_prefix=">")

#bot上線顯示
@bot.event
async def on_ready():
    print(">>bot is online")

#help
@bot.command()
async def 指令(ctx):
 await ctx.send("可用指令")
 #await ctx.send("抽-抽一張圖片")
 await ctx.send("抽晚餐-決定晚餐吃什麼")
 await ctx.send("我愛你-打就對了廢話那麼多幹嘛")
 await ctx.send("抽現金-看你運氣囉")

#抽圖片
#圖片位置放置於 setting pic類別
#@bot.command()
#async def 抽(ctx):
#    random_pic = random.choice(jdata['pic'])
#    pic = discord.File(random_pic)
#    await ctx.send(file=pic)

#抽隨機字串
#隨機字串放置於 setting txt類別
@bot.command()   
async def 抽晚餐(ctx):
    random_txt = random.choice(jdata['txt'])
    #pic = discord.File(random_pic)
    await ctx.send(random_txt)
@bot.command()
async def 我愛你(ctx):
    random_txt = random.choice(jdata['txt2'])
    #pic = discord.File(random_pic)
    await ctx.send(random_txt)
@bot.command()
async def 早安(ctx):
  await ctx.send("主人早安 昨天的主人好厲害")
@bot.command()
async def 晚安(ctx):
  await ctx.send("主人晚安 晚在床上等~妳~喔~")

#定時訊息
#async def interval():
# await bot.wait_until_ready()
# channel= bot.get_channel(609001766113247233)
# while not bot.is_closed():
#     await channel.send("123")
#     await asyncio.sleep(3600)
#bg_task = bot.loop.create_task(interval())

#隨機數字
@bot.command()   
async def 抽現金(ctx):
   await ctx.send("恭喜抽到") 
   await ctx.send(random.randint(1,200000))
   
#@bot.command()
#async def join(ctx):
#    channel = ctx.author.voice.channel(609001766113247233)
#    await channel.connect()
bot.run(jdata['TOKEN'])
