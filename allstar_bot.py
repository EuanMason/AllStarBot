import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message.content = message.content.casefold()
    if message.content.startswith('hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NDg0MzQxMjQ5MDM4MzUyMzg0.Dmgt-A.0VYP4DWBM3x0hrRURS7TonMFpYU')
