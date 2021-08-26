import os
import asyncio
import websockets
import crc16

connected = set()

async def echo(websocket, path):
    # Register.
    username = 'user' + str(crc16.crc16xmodem(websocket.remote_address[0].encode('utf-8')))
    connected.add(websocket)
    try:
        async for message in websocket:
            await asyncio.wait([ws.send(username + ': ' + str(message)) for ws in connected])
            #await asyncio.sleep(10)
    finally:
        # Unregister.
        connected.remove(websocket)

start_server = websockets.serve(echo, "0.0.0.0", os.environ.get("PORT", 17995))

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
