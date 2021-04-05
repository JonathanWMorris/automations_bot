import discord
import commands
import messages

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-!hello'):
        await message.channel.send(messages.welcome_message)

    elif message.content.startswith('-!cat'):
        image_url = commands.get_cat_image_url()
        await message.channel.send(image_url)

    elif message.content.startswith("-!private"):
        await message.delete(delay=2)

    elif message.content.startswith("-!fact"):
        fact = commands.get_fact()
        await message.channel.send(fact)

    elif message.content.startswith("-!animals"):
        command = commands.get_animal_command()
        await message.channel.send(command)

    elif message.content.startswith("-!help"):
        await message.channel.send(messages.help_message)

    elif message.content.startswith("-!"):
        await message.channel.send(messages.response_text)


client.run('ODI3OTcyMzU3MzY4MDUzODMw.YGizWA.08HUC_slOmNj65veuKenyt4oA40')
