from dataclasses import dataclass
import os
from pathlib import Path

import openai


@dataclass
class TranscriptData:
    transcript: str
    summary: str
    key_action_items: str


def get_audio_transcript_data(file_path: Path) -> TranscriptData:
    openai.api_key = os.getenv('OPEN_AI_API_KEY')
    with open(file_path, 'rb') as audio_file:
        transcript = openai.Audio.transcribe('whisper-1', audio_file)
        transcript_text = transcript.text.strip()
    key_items = extract_action_items(transcript.text)
    summary = get_summary(transcript_text)
    return TranscriptData(
        transcript=transcript_text,
        key_action_items=key_items,
        summary=summary
    )


def extract_action_items(text: str):
    # Prompt for the model
    prompt = f"Extract the key action items from the following text:\n\n{text}"
    return _get_text_completion_result(prompt)


def get_summary(text):
    prompt = f"Summarize the following text:\n{text}"
    return _get_text_completion_result(prompt)


def _get_text_completion_result(prompt: str) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=len(prompt.split())
    )
    return response.choices[0].text.strip()
