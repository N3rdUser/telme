import asyncio
from pyrogram import Client

# send audio file
# get message with filter soundcloud url
# after send remove mp3 file

api_id = 12345
api_hash = "0123456789abcdef0123456789abcdef"

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")


asyncio.run(main())