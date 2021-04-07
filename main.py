import discord
import commands
import messages

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


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

    elif message.content.startswith("-!verifyAll"):
        names = message.channel.members
        list_of_names = []

        for name in names:
            list_of_names.append(name.display_name)

        responses = commands.get_batch_verification(list_of_names)

        for response in responses:
            await message.channel.send(response)

    elif message.content.startswith("-!verify"):
        name = message.content.replace("-!verify ", "")
        response = commands.get_verification(name)
        await message.channel.send(response)

    elif message.content.startswith("-!names"):
        names = message.channel.members
        list_of_names = []

        for name in names:
            list_of_names.append(str(name.display_name))

        await message.channel.send(list_of_names)

    elif message.content.__contains__("827972357368053830"):
        await message.channel.send(messages.mention_message)

    elif message.content.startswith("-!"):
        await message.channel.send(messages.response_text)

    elif message.content.__contains__("gif") \
            or message.content.__contains__("jpg") or message.content.__contains__("png"):
        file_path = "nsfw_image.jpg"
        commands.get_image(message.content, file_path)
        is_NSFW = commands.check_nsfw_image(file_path)

        if is_NSFW:
            await message.channel.send(f"@Admin @Moderator , {message.author.display_name} sent an inappropriate image.")
            await message.delete()


client.run('ODI3OTcyMzU3MzY4MDUzODMw.YGizWA.08HUC_slOmNj65veuKenyt4oA40')
