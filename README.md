# audio_recorder_socket

This repository provides a simple WebSocket server that records incoming binary audio frames and saves them as `.mp3` files.

## Requirements

- Python 3.12+
- [`websockets`](https://pypi.org/project/websockets/)

Install dependencies using pip:

```bash
pip install -r requirements.txt
```

## Running the server

Run the server with Python:

```bash
python websocket_server.py
```

The server listens on `ws://0.0.0.0:8000`. When a client connects and sends binary audio data, the server writes the frames to a new file under the `recordings/` directory. Each connection creates a unique file with a timestamp and random identifier.

