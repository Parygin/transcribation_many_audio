# Transcribing a list of files using Yandex SpeechKit


# Requirements
For the script to work, you must have a [Yandex Cloud account](https://console.cloud.yandex.ru/) with a positive balance.


# Installation
+ Clone the repository and go to the application folder:
``` python
git clone https://github.com/Parygin/transcribation_many_audio.git
cd transcribation_many_audio/
```
+ Install and activate the Python virtual environment:
``` python
python3 -m venv venv
source venv/bin/activate
```
+ Install all the dependencies are gathered in requirements.txt:
``` python
pip3 install -r requirements.txt
```
+ Write your settings in the .env file (after removing the "example"from its name).
+ Rename the file "links_list.txt-example" and enter a list of audio files to be processed.
+ Launch the app.
``` python
python3 transcribation_many_audio.py
```


### Basic settings


# Information
- [Yandex Cloud: Распознавание длинных аудио](https://cloud.yandex.ru/docs/speechkit/stt/transcribation)
- [Yandex Cloud: Создание API-ключа](https://cloud.yandex.ru/docs/iam/operations/api-key/create)
- [Yandex Cloud: Концепции](https://cloud.yandex.ru/docs/storage/concepts/)
