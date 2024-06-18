from typing import Any
import discord
from discord.interactions import Interaction
from discord.ui import View, Select
import asyncio

from discord.ui.item import Item

class MainEmbed(discord.Embed):
    def __init__(self, type, icon_url):
        self.type = type
        super().__init__(
               title="Chose your map", 
               description=f"That's the *first step* in wich you will select the \nmap that you want to get the **{type}** from!\n\nThe BOT will return the *TOP 5* **{type}** by default, \nbut you can chage it using **/config**.", 
               color=0x2a2a2a
            )
        super().set_thumbnail(url="https://s2-techtudo.glbimg.com/Hg6dmbUbRhch_7Ke-BOA3Qlpamg=/0x0:1200x603/1000x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2019/i/b/ETfVe9TSWL7BL6NLQZYQ/1535723475188-fb-image.png")
        super().set_footer(text="Papis Interprise")
        super().set_image(url=icon_url)
                 
class Menu_1(Select):
    async def callback(self, interaction: discord.Interaction):
            print("CLICKOU!")
            await interaction.response.response_message(content=F"Smokes do mapa {self.values[0]}...")

    def __init__(self):
        super().__init__(options=[
            discord.SelectOption(label="Mirage", emoji="<:mirage1:1130930676737253396>"),
            discord.SelectOption(label="Inferno", emoji="<:inferno:1130930869822042222>"),
            discord.SelectOption(label="Overpass", emoji="<:overpass:1130931063523389470>"),
            discord.SelectOption(label="Ancient", emoji="<:ancient:1130931154418159626>"),
            discord.SelectOption(label="Nuke", emoji="<:nuke:1130931301235572897>"),
            discord.SelectOption(label="Vertigo", emoji="<:vertigo:1130931432160763925>"),
            discord.SelectOption(label="Anubis", emoji="<:anubis:1130931509814112347>"),
        ],
        placeholder="Active Duty",)
    
class Menu_2(Select):
    async def callback(self, interaction: discord.Interaction):
            print("CLICKOU!")
            await interaction.response.send_message(content="Jirombola")

    def __init__(self):
        super().__init__(options=[
            discord.SelectOption(label="Dust2", emoji="<:dust2:1130931587584892980>"),
            discord.SelectOption(label="Tuscan", emoji="<:tuscan:1130931663094951997>"),
            discord.SelectOption(label="Train", emoji="<:train:1130938211686940794>"),
            discord.SelectOption(label="Cache", emoji="<:cache:1130931730887479329>"),
            discord.SelectOption(label="Cobblestone", emoji="<:cobblestone:1130931813318152312>"),
        ],
        placeholder="Reserve")

class MyView(View):
    label = ""
    def __init__(self, label, menus):
        super().__init__()
        self.label = label
        for x in menus:
             super().add_item(x)