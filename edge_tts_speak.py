#!/usr/bin/env python3
"""Synthesize Vietnamese speech using Microsoft Edge neural voices."""
import asyncio
import sys
from pathlib import Path
import edge_tts

async def main():
    target = Path(sys.argv[1]).resolve()
    voice = sys.argv[2]
    if voice not in ("vi-VN-HoaiMyNeural", "vi-VN-NamMinhNeural"):
        raise ValueError("Unsupported voice")
    # Bun/Node pipes UTF-8 bytes; on Windows Python may decode pipes as cp1252.
    text = sys.stdin.buffer.read().decode('utf-8', errors='strict').strip()
    if not text:
        raise ValueError("Empty text")
    target.parent.mkdir(parents=True, exist_ok=True)
    await edge_tts.Communicate(text, voice=voice).save(str(target))

if __name__ == "__main__":
    asyncio.run(main())
