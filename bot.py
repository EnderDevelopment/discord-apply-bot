import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def applypanel(ctx):
    embed = discord.Embed(title="Bewerbung", description="Klicken Sie auf den Knopf, um die Bewerbung zu starten", color=discord.Color.blue())
    view = discord.ui.View()
    button = discord.ui.Button(label="Bewerben", style=discord.ButtonStyle.primary)
    view.add_item(button)

    async def button_callback(interaction):
        await interaction.response.send_message("Bitte beantworten Sie die folgenden Fragen:", ephemeral=True)
        await interaction.user.send("Frage 1: Warum möchten Sie sich bewerben?")

        def check(m):
            return m.author == interaction.user and isinstance(m.channel, discord.DMChannel)

        try:
            msg1 = await bot.wait_for('message', check=check, timeout=60.0)
            await interaction.user.send("Frage 2: Welche Erfahrungen haben Sie?")
            msg2 = await bot.wait_for('message', check=check, timeout=60.0)

            application = f"Bewerbung von {interaction.user.mention}:
Frage 1: {msg1.content}
Frage 2: {msg2.content}"
            channel = bot.get_channel(int(os.getenv('APPLICATION_CHANNEL_ID')))
            if channel:
                await channel.send(application)
                await interaction.user.send("Ihre Bewerbung wurde gesendet!")
            else:
                await interaction.user.send("Fehler: Bewerbungs-Channel nicht gefunden.")
        except asyncio.TimeoutError:
            await interaction.user.send("Die Bewerbung wurde abgebrochen.")

    button.callback = button_callback
    await ctx.send(embed=embed, view=view)

@bot.command()
async def cancel(ctx):
    await ctx.send("Ihre Bewerbung wurde abgebrochen.")

bot.run(TOKEN)