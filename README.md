# Voice Assistant

A personal voice assistant in Python, from 2021. It listens on the
microphone, sends the speech to Google's speech recognizer, matches
keywords, and answers out loud.

## What it does

[`src/main.py`](src/main.py) greets you by the time of day, asks your name,
then listens in a loop. What works as written:

- **Answers set questions** from [`config/conversation.yaml`](config/conversation.yaml),
  such as "What is your name" (then it stops: see Known problems).
- **Looks things up:** a three-sentence Wikipedia summary.
- **Opens sites:** YouTube, Google and Stack Overflow.
- **Small things:** a joke, a pause for a number of seconds, and an email
  through Gmail.
- **Windows commands:** lock, log off and restart.

The time, "play", screenshots, web search, maps, shut down, hibernate and
emptying the recycle bin are written but broken: see Known problems. There
is no machine learning of its own: it matches keywords in the text Google
returns. [`src/talk.py`](src/talk.py) speaks the answers with pyttsx3.

## Repository layout

| Folder | Holds |
|---|---|
| [`src/`](src) | The assistant, [`main.py`](src/main.py), and the speech module it uses, [`talk.py`](src/talk.py) |
| [`config/`](config) | The set questions and their answers |

## Run it

In 2021 it ran with Python 3.9 on Linux; its system commands are written
for Windows:

```bash
git clone https://github.com/jewel-nath/voice-assistant.git
cd voice-assistant
pip install -r requirements.txt
python src/main.py
```

It needs a microphone and an internet connection. To send email, put a
Gmail address and an app password in `sendEmail()` in `src/main.py`.

## Known problems

- A command that matches no keyword stops the program: the last check
  uses `query`, a name that is never set. This includes the set questions,
  right after their answer, and "screenshot" itself.
- If the recognizer hears nothing or fails, `takeCommand()` stops the
  program: its bare `except` passes, then it returns `command`, which was
  never set.
- Asking the time stops the program on Windows (the format
  `"% H:% M:% S"` is invalid), and "play" calls `talk`, which doesn't exist.
- "empty recycle bin" uses `winshell`, which is never imported.
- "shutdown system", "hibernate" and "where is" build broken commands or
  addresses with stray spaces (`shutdown / p /f`, `shutdown / h`,
  `google.nl / maps / place/`); "search" opens the spoken words as if they
  were a web address.
- "restart" matches anywhere in a sentence and restarts Windows with no
  question first; "log off" and "sign out" sign out after five seconds.

## Credits

- Most of the commands, the greeting and the email function follow the
  GeeksforGeeks article
  [Voice Assistant using python](https://www.geeksforgeeks.org/python/voice-assistant-using-python/)
  by Gaurav Kumar Jha.
- The set-questions file and its loop follow
  [GassistPi](https://github.com/shivasiddharth/GassistPi) by Shivasiddharth
  (MIT).
- Thanks to [Anik Chakraborty](https://github.com/Anikcb) for the
  screenshot command and to [Prome Saha](https://github.com/Prome11809048)
  for the answer to "What is your name".

## Licence

My code is under the MIT licence: see [LICENSE](LICENSE). The parts that
follow GassistPi stay under its MIT licence, Copyright (c) 2020
Shivasiddharth. The parts that follow the GeeksforGeeks article are not
under this licence: the article states no open licence, and its site
reserves all rights.
