import json
import asyncio
import websockets

from SDClient import SDClient
#from SDBattle import pokemon_battle

from environs import Env

async def cynthia():

    env = Env()
    env.read_env()
    uri = env("SD_URI", "wss://sim2.psim.us/showdown/websocket")
    username = env("SD_USERNAME")
    password = env("SD_PASSWORD", "")
    ladder = env("SD_LADDER", "gen7randombattle")

    team = 'null'

    sd_client = await SDClient.create(username, password, uri)
    await sd_client.login()

    while True:
        await sd_client.find_game(ladder, team)

#        winner = pokemon_battle(sd_client, ladder)
#        break


asyncio.get_event_loop().run_until_complete(cynthia())
