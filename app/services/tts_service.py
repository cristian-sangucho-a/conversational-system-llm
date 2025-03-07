from gtts import gTTS
import asyncio
import tempfile
from pathlib import Path

async def text_to_speech(text: str, filename: str = "response.mp3") -> str:
    try:
        temp_dir = Path("temp")
        temp_dir.mkdir(exist_ok=True)
        filepath = temp_dir / filename

        tts = await asyncio.to_thread(
            gTTS, 
            text=text, 
            lang='es', 
            slow=False
        )
        
        await asyncio.to_thread(tts.save, str(filepath))
        return str(filepath)
    except Exception as e:
        raise Exception(f"Error generating audio: {str(e)}")