import discord
import discord.utils
from discord import app_commands
from classes import MyView, Menu_1, Menu_2, MainEmbed

import requests
MY_GUILD = discord.Object(id=1110977633992327269)  #Servidor

class MyClient(discord.Client):
    def __init__(self, intents:discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self) #Criando a Tree

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

    async def on_member_join(self, member):
        pass
    
    async def on_message(self, message):
        mapas = ["ANUBIS", "ANCIENT","INFERNO","MIRAGE","NUKE","OVERPASS","VERTIGO"]
        if message.author.bot:
            return
        content = message.content
        for x in mapas:
            if x in content.upper():
                await message.reply("Percebi que você mencionou um mapa de CS:GO, use meus comandos para aprender mais sobre o uso dos utilitarios.")
#INTENTS
client = MyClient(intents=discord.Intents.all())

@client.event
async def on_ready():
        print(f'Logged in as {client.user} (ID: {client.user.id})')
        print('------')
        #myLoop.start()

def check_role(interaction: discord.Interaction):
    return interaction.user.Member.get_role()

#############################################
@client.tree.command(name="smokes")
async def smokes(interaction: discord.Interaction):
    embed = MainEmbed(type="smokes", icon_url="https://static.wikia.nocookie.net/cswikia/images/7/76/Smokegrenadehud_csgo.png/revision/latest?cb=20211113165620")
    view = MyView(label="Smokes", menus=[Menu_1(),Menu_2()])
    await interaction.response.send_message(view=view, embed=embed)

@client.tree.command(name="molotovs")
async def molotovs(interaction: discord.Interaction):
    mapa = ""
    embed = MainEmbed(type="molotovs", icon_url="https://static.wikia.nocookie.net/cswikia/images/5/56/Molotovhud.png/revision/latest?cb=20211113171930")
    view = MyView(label="Smokes", menus=[Menu_1(),Menu_2()])
    await interaction.response.send_message(view=view, embed=embed)


@client.tree.command(name="flashs")
async def flashs(interaction: discord.Interaction):
    mapa = ""
    embed = MainEmbed(type="flashs", icon_url="https://static.wikia.nocookie.net/cswikia/images/f/f3/Flashbanghud_csgo.png/revision/latest?cb=20211113165814")
    view = MyView(label="Smokes", menus=[Menu_1(),Menu_2()])
    await interaction.response.send_message(view=view, embed=embed)

@client.tree.command(name='hegrenades')
async def hegrenades(interaction: discord.Interaction):
    mapa = ""
    embed = MainEmbed(type="hegrenades", icon_url="https://static.wikia.nocookie.net/cswikia/images/c/ce/Hegrenadehud_csgo.png/revision/latest?cb=20211113165930")
    view = MyView(label="Smokes", menus=[Menu_1(),Menu_2()])
    await interaction.response.send_message(view=view, embed=embed)


client.run("MTEyNzI2OTM0NjcyOTc5MTUzOQ.GE03MT.5EP3gdv-nMUUE7U3EzJS92XwoXT_F7YypGiKfA")