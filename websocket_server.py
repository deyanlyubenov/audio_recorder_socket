import asyncio
import os
import uuid
import datetime
from io import BytesIO

from pydub import AudioSegment
import websockets

RECORDINGS_DIR = "recordings"

async def handle_connection(websocket, path):
    os.makedirs(RECORDINGS_DIR, exist_ok=True)

    buffer = bytearray()
    last_received = asyncio.get_event_loop().time()

    print("Client connected. Waiting for audio frames...")

    while True:
        try:
            message = await asyncio.wait_for(websocket.recv(), timeout=2.0)
        except asyncio.TimeoutError:
            if buffer:
                await _flush_buffer(buffer)
            continue
        except websockets.exceptions.ConnectionClosed:
            break

        if isinstance(message, bytes):
            buffer.extend(message)
            last_received = asyncio.get_event_loop().time()
        # Ignore text messages

    if buffer:
        await _flush_buffer(buffer)
    print("Client disconnected")

async def _flush_buffer(buffer: bytearray):
    """Encode the collected WAV data to MP3 and save to a file."""
    filename = f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex}.mp3"
    filepath = os.path.join(RECORDINGS_DIR, filename)
    print(f"Saving recording to {filepath}")

    audio = AudioSegment.from_file(BytesIO(buffer), format="wav")
    audio.export(filepath, format="mp3")
    buffer.clear()

async def main():
    async with websockets.serve(handle_connection, "0.0.0.0", 8000):
        print("WebSocket server listening on ws://0.0.0.0:8000")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
