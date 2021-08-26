import os
import asyncio
import websockets
import crc16

async def echo(websocket, path):
    async for message in websocket:
        username = 'user' + str(crc16.crc16xmodem(websocket.remote_address[0].encode('utf-8')))
        await websocket.send(username + ': ' + str(message))

start_server = websockets.serve(echo, "0.0.0.0", os.environ.get("PORT", 17995))

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
