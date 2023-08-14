# Video Caption Generator

## Project Overview
This project is a Python web app that allows users to upload videos and generate overlaid captions.
After the user uploads their media, OpenAI Whisper transcribes and timestamps the audio. Finally, using
FFmpeg the subtitle file is burned onto the original file and displayed onto the screen. The website uses Flask
and Bootstrap for styling.

## Technologies Used

- **Backend**: Python, Flask, FFmpeg
- **Frontend**: Bootstrap
- **Machine Learning**: Pre-trained models from OpenAI 
- **Database**: SQLAlchemy

## Project Setup
For transcription, I used an older version of OpenAI Whisper as I found it easier to work with for
writing .SRT subtitle files. Here is my installation:

    pip install openai-whisper==20230117

Whisper has its own requirements namely FFmpeg, which can be found here:

    ['Whisper'](https://github.com/openai/whisper)





