"""Validate the bundled bounty artwork and publish an exact copy."""

import hashlib
import os
from pathlib import Path
import struct


PNG_SIGNATURE = b'\x89PNG\r\n\x1a\n'
EXPECTED_DIMENSIONS = (1024, 1024)
BYTE_LIMIT = 1024 * 1024
ENTRY_NAME = 'entry.png'


def load_artwork() -> bytes:
    source = Path(__file__).resolve().parent / 'assets' / ENTRY_NAME
    payload = source.read_bytes()
    validate_artwork(payload)
    return payload


def validate_artwork(payload: bytes) -> None:
    if len(payload) >= BYTE_LIMIT:
        raise ValueError('Artwork must be smaller than 1 MiB')
    if payload[:8] != PNG_SIGNATURE:
        raise ValueError('Artwork has an invalid PNG signature')
    if len(payload) < 33 or payload[12:16] != b'IHDR':
        raise ValueError('Artwork must begin with a complete IHDR chunk')
    if struct.unpack('>I', payload[8:12])[0] != 13:
        raise ValueError('PNG IHDR chunk length must be 13 bytes')
    dimensions = struct.unpack('>II', payload[16:24])
    if dimensions != EXPECTED_DIMENSIONS:
        raise ValueError('Artwork dimensions must be exactly 1024x1024')


def publish_artwork(payload: bytes) -> Path:
    directory = Path(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output'))
    directory.mkdir(parents=True, exist_ok=True)
    destination = directory / ENTRY_NAME
    destination.write_bytes(payload)
    if destination.read_bytes() != payload:
        raise RuntimeError('Published artwork differs from the source bytes')
    return destination


def run_entrypoint() -> None:
    artwork = load_artwork()
    published = publish_artwork(artwork)
    digest = hashlib.sha256(artwork).hexdigest()
    print(f'{published} {len(artwork)} bytes sha256={digest}')


if __name__ == '__main__':
    run_entrypoint()
