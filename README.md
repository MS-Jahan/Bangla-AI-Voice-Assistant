# Bangla-AI-Voice-Assistant
Taking Bangla voice as input and giving Bangla voice as output is what it does.

This project involves using Google Speech-To-Text, OpenAI’s Whisper Model, Google Bard API (Reverse Engineered), Google Text-To-Speech, BanglaTTS (PyTorch, Aksharamukha, Silero Models).
It also uses undetected_chromedriver (a special selenium wrapper).

It's just a baby project for my university (out-of-syllabus) presentation done in less than 2 hours! As I was busy with other things, I couldn't make something big.
I don't take pride in the project; it's merely a childish endeavor.

## Installation
Last tested on Python 3.11
1. Firstly, clone this repo:
`git clone https://github.com/MS-Jahan/Bangla-AI-Voice-Assistant`
2. Install required modules:
`pip install -r requirements`
3. Copy [mpv](https://mpv.io/installation/) binary in mpv folder. It should have `mpv.com` binary. See the code for more insight. MPV is used here for audio playing. You can use `playaudio` or `pygame` if you want.

## How To Run
After the installation, run the `main.py` file.
`python3 main.py`

On first run, you'll be prompted to log into your Google account. Don't close the browser window, it should close automatically.
When it says "Say Something" in the terminal, say something to the mic in Bangla.

## Links
Source: https://github.com/MS-Jahan/Bangla-AI-Voice-Assistant

Presentation: https://docs.google.com/presentation/d/15BHxU8sqFw_1tB1tRCsm7UuAyvFNEolYuCUg12-P3XI/

Video Demo: https://youtu.be/3VHht3nIheU
