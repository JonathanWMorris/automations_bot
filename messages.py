
help_message = "Currently the commands that we have are are: \n 1) -!hello \n 2) -!cat \n 3) -!private \n 4) -!fact " \
               "\n 5) -!animals "

response_text = "Looks like you are having some troubles, that is not a valid command. Try again! I believe " \
                "in you! "

welcome_message = "Hello! I'm a bot, did you know that i can do botty things that bots do? I'm a bot, i'm a bot, " \
                  "i'm a bot "

mention_message = "Did someone say my name? Strange... I hope they know they only need to type -!help for the help " \
                  "message. \n They probably aren't good with technology..."


def nsfw_content_message(author):
    return f"<@!822960923475968051> <@!822961195031199764> , {author} sent an inappropriate image."