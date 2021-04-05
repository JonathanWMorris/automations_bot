import discord
import requests
import base64
import random

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-!hello'):
        await message.channel.send('Hello!')

    elif message.content.startswith('-!cat'):
        result = requests.get('https://api.thecatapi.com/v1/images/search')
        result_json = result.json()
        image = result_json[0]
        image_url = image["url"]
        await message.channel.send(image_url)

    elif message.content.startswith('-!speak'):
        text = message.content
        text = text.replace("-!speak", "")
        result = requests.post(
            "https://api.deepai.org/api/text-generator",
            data={
                'text': text,
            },
            headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
        )
        json_result = result.json()
        await message.channel.send(json_result["output"])

    elif message.content.startswith("-!private"):
        await message.delete(delay=2)

    elif message.content.startswith("-!fact"):
        dogFacts = "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1"
        trivia = "https://opentdb.com/api.php?amount=1&category=9&difficulty=easy&type=boolean&encode=base64"

        response = requests.get(trivia)

        trivia_object = response.json()

        results_object = trivia_object["results"]

        fact = results_object[0]["question"]
        fact = base64.b64decode(fact)
        fact = fact.decode('utf-8')
        fact = fact[:-1]

        accuracy = results_object[0]["correct_answer"]
        accuracy = base64.b64decode(accuracy).lower()
        accuracy = accuracy.decode('utf-8')

        if accuracy == "true":
            fact = f"Did you know that {fact}?"
        elif accuracy == "false":
            fact = f"Did you know that '{fact}' is not true?"

        await message.channel.send(fact)

    elif message.content.startswith("-!animals"):
        animals = ["cat", "dog", "wolf", "otter", "panda"]
        command = f"a!{random.choice(animals)}"
        await message.channel.send(command)

    elif message.content.startswith("-!help"):
        help_message = "Currently the commands that we have are are: \n 1) hello \n 2) cat \n 3) private \n 4) fact " \
                       "\n 5) animals "
        await message.channel.send(help_message)

    elif message.content.startswith("-!"):
        response_text = "Looks like you are having some troubles, that is not a valid command. Try again! I believe " \
                        "in you! "
        await message.channel.send(response_text)


client.run('ODI3OTcyMzU3MzY4MDUzODMw.YGizWA.08HUC_slOmNj65veuKenyt4oA40')
