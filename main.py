import asyncio
import os
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from one_note import create_one_note_page
from transcription import get_audio_transcript_data

dp = Dispatcher()
bot = Bot(os.getenv('BOT_TOKEN'), parse_mode=ParseMode.HTML)
TMP_DIR = Path('/tmp')
Path.mkdir(TMP_DIR, exist_ok=True)


@dp.message()
async def echo_handler(message):
    if not message.audio:
        return
    _file = await bot.get_file(message.audio.file_id)
    file_path = TMP_DIR / message.audio.file_name
    await bot.download(file=_file, destination=file_path)
    data = get_audio_transcript_data(file_path)
    chat_id = message.from_user.id
    for section, text in data.__dict__.items():
        await bot.send_message(chat_id=chat_id, text=f'{section}:\n {text}')

    page_name = f'{Path(message.audio.file_name).stem} summary'
    one_note_is_created = await create_one_note_page(page_name=page_name, content=data.summary)
    one_note_message = f'OneNote page {page_name} is created' if one_note_is_created else 'OneNote page is not created'
    await bot.send_message(chat_id=chat_id, text=one_note_message)

    #  TODO: send emails


async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

