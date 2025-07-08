# audio_recorder_socket

This repository provides a simple WebSocket server that receives binary WAV audio frames over WebSocket and encodes them to `.mp3` files.

## Requirements

- Python 3.12+
- [`websockets`](https://pypi.org/project/websockets/)
- [`pydub`](https://pypi.org/project/pydub/) (requires `ffmpeg`)

Install dependencies using pip (make sure `ffmpeg` is installed on your system):

```bash
pip install -r requirements.txt
```

## Running the server

Run the server with Python:

```bash
python websocket_server.py
```

The server listens on `ws://0.0.0.0:8000`. When a client sends binary WAV data,
the server buffers the incoming frames and, after a short period with no new
data, encodes the buffer to MP3. The resulting files are stored under the
`recordings/` directory with timestamped names.

