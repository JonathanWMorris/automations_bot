# Automation Bot
This is a general purpose bot in Leland Class of 2021. This bot is intended to make things easier for all users.

## Commands

### -!Hello
This gives a welcome message.

### -!cat
This gives you one cat picture.

### -!private
Messages with this at the front will disappear after 2 seconds

### -!fact
This command sends out a random fact in the channel the command was used in

### -!animals
This command creates and sends a message/ command for the Animal Bot by attaching "-a" to a random string from this list: ["cat", "dog", "wolf", "otter", "panda"]. This will send a random animal image essentially.

### -!help
Sends a help message in the channel it was requested.

### -!verifyAll
Verifys if all the members in that chanell are seniors by checking in the official roster, if they are potentially not seniors, it will send a message that "{name} is not a senior".

### -!verify {name}
This will verify if the name you provided are in the official roster. It will ensure that only seniors are in the server. This will say either "{name} is a senior" or "{name} is not a senior".

### -!names
This will list the names of everyone who is in the channel. This is mainly there for testing purposes.

### -!
This is meant to be as a catch all so that it will respond with an error message.

## Auto NSFW detection
This bot automatically looks at links, embeds, and attachments to see if the content is NSFW or not. The accuracy is around 80% - 90%.
