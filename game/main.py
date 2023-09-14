import game.config as config
from adventure import Adventure
import asyncio

async def play():
    print("Welcome to Choose-Your-Own-Adventure!")
    api_key = config.OpenAIKeyManager.get_api_key()

    adventure = Adventure(api_key)
    await adventure.start()
    while True:
        await adventure.step()
    

if __name__ == '__main__':
    asyncio.run(play())
