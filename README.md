# audio_recognition
Telegram chat bot receives audio files and write messages with transcript, summary and key actions.

To install all requirements you need to run `pip install -r requirements.txt` in the project directory.

To start the Telegram bot you need to run `python main.py` script with following environment variables:
```
BOT_TOKEN=6711054509:AAG_LMYvq7s2t0Pov4yT2SR3khvy2KmD1lY
OPEN_AI_API_KEY=<YOUR OPEN AI API KEY>
ONE_NOTE_CLIENT_ID=<YOUR CLIENT ID>
ONE_NOTE_CLIENT_SECRET=<YOUR CLIENT SECRET>
ONE_NOTE_TENANT_ID=<YOUR TENANT ID>
```

Find in Telegram [MaxartAudioRecognitionBot](https://t.me/MaxartAudioRecognitionBot), 
press `/start` and send to it an audio file you want to analyze.

After few seconds you will receive audio transcription as following:
```
transcript:
 This is an OpenAI test number one. Tomorrow I will have a Romanian lesson. On Friday I will work. On Saturday I will go to airport.

summary:
 I will have a Romanian lesson tomorrow and then work on Friday. On Saturday, I will be heading to the airport.

key_action_items:
 1. Have a Romanian lesson tomorrow
2. Work on Friday
3. Go to airport on Saturday

OneNote page is not created
```

OneNote page should be created with filename as page name and summary as content. Currently, this functionality doesn't work now.
