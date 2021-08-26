import os
import asyncio
import websockets
import binascii

async def echo(websocket, path):
    async for message in websocket:
        username = await 'user' + str(binascii.crc32(websocket.remote_address[0].encode('utf-8')))
        await websocket.send(username + ': ' + str(message))

start_server = websockets.serve(echo, "localhost", os.environ.get("PORT", 17995))

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
