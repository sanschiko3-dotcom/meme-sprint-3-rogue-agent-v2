import hashlib
import os
import struct
from pathlib import Path

def main():
    data = (Path(__file__).resolve().parent / 'assets/entry.png').read_bytes()
    if data[:8] != b'\x89PNG\r\n\x1a\n' or data[12:16] != b'IHDR':
        raise ValueError('Invalid PNG')
    if len(data) >= 1048576 or struct.unpack('>II', data[16:24]) != (1024, 1024):
        raise ValueError('Invalid size or dimensions')
    out = Path(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output'))
    out.mkdir(parents=True, exist_ok=True)
    path = out / 'entry.png'
    path.write_bytes(data)
    if path.read_bytes() != data:
        raise RuntimeError('Copy verification failed')
    print(f'{path} {len(data)} bytes sha256={hashlib.sha256(data).hexdigest()}')

if __name__ == '__main__':
    main()
