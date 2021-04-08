import discord
import commands
import messages
import constants
import time

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

    elif message.content.startswith("-!yoda"):
        sentence = message.content.replace("-!yoda ", "")
        yoda_sentence = commands.get_yoda_speak(sentence)
        await message.channel.send(yoda_sentence)

    elif message.content.startswith("-!joke"):
        joke = commands.get_joke()
        await message.channel.send(joke.setup)
        time.sleep(2)
        await message.channel.send(joke.punchline)

    elif message.content.startswith("-!"):
        await message.channel.send(messages.response_text)

    # All these are checking for NSFW content
    if message.content.__contains__(".gif") \
            or message.content.__contains__(".jpg") or message.content.__contains__(".png"):

        is_NSFW = commands.check_nsfw_image(message.content)

        if is_NSFW:
            await message.channel.send(messages.nsfw_content_message(message.author.display_name))
            await message.delete()

    if message.content.__contains__(".mov") \
            or message.content.__contains__(".mp4") or message.content.__contains__(".avi"):

        is_NSFW = commands.check_nsfw_video(message.content)

        if is_NSFW:
            await message.channel.send(messages.nsfw_content_message(message.author.display_name))
            await message.delete()

    if message.attachments:
        for attachment in message.attachments:
            if attachment.url.__contains__(".jpg") \
                    or attachment.url.__contains__(".png") or attachment.url.__contains__(".gif"):

                is_NSFW = commands.check_nsfw_image(attachment.url)

                if is_NSFW:
                    await message.channel.send(messages.nsfw_content_message(message.author.display_name))
                    await message.delete()

            if attachment.url.__contains__(".mov") \
                    or attachment.url.__contains__(".mp4") or attachment.url.__contains__(".avi"):

                is_NSFW = commands.check_nsfw_video(attachment.url)

                if is_NSFW:
                    await message.channel.send(messages.nsfw_content_message(message.author.display_name))
                    await message.delete()

    if message.content.__contains__("827972357368053830"):
        await message.channel.send(messages.mention_message)

    if message.embeds:
        for embed in message.embeds:
            if embed.image:
                is_NSFW = commands.check_nsfw_image(embed.image.url)

                if is_NSFW:
                    await message.channel.send(messages.nsfw_content_message(message.author.display_name))
                    await message.delete()

            if embed.video:
                is_NSFW = commands.check_nsfw_video(embed.video.url)

                if is_NSFW:
                    await message.channel.send(messages.nsfw_content_message(message.author.display_name))
                    await message.delete()


client.run(constants.discord_token)
