import asyncio
import os
import uuid
import datetime
import websockets

RECORDINGS_DIR = "recordings"

async def handle_connection(websocket, path):
    os.makedirs(RECORDINGS_DIR, exist_ok=True)
    filename = f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex}.mp3"
    filepath = os.path.join(RECORDINGS_DIR, filename)
    print(f"Recording incoming connection to {filepath}")
    with open(filepath, 'wb') as f:
        async for message in websocket:
            if isinstance(message, bytes):
                f.write(message)
            else:
                # Ignore text messages
                pass
    print(f"Saved recording to {filepath}")

async def main():
    async with websockets.serve(handle_connection, "0.0.0.0", 8000):
        print("WebSocket server listening on ws://0.0.0.0:8000")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
