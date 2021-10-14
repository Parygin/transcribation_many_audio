# Transcribing a list of files using Yandex SpeechKit


# Requirements
+ For the script to work, you must have a [Yandex Cloud account](https://console.cloud.yandex.ru/) with a positive balance.
+ Audio files must be loaded into an open [Bucket](https://cloud.yandex.ru/docs/storage/concepts/bucket), this is necessary for generating links *(this requirement may be removed in the future)*.
+ It is worth paying attention to the [supported audio formats](https://cloud.yandex.ru/docs/speechkit/stt/formats).
I prefer ffmpeg:
``` bash
mkdir new
for i in *.wav; do name=`echo $i | cut -d'.' -f1`; ffmpeg -i $i -c:a libopus -b:a 48k new/$name.opus; done
```

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
+ The script was conceived as a tool for transcribing really long audio (from 10 minutes and more). If you work with shorter files, you can try changing the interval for checking the result:
``` python
TIME_SLEEP = 30
```
+ The default file paths are set as follows:
``` python
# A file with a list of audio files:
FILE = 'links_list.txt'
# Folder for transcription results:
FOLDER = 'results'
```

# Information
- [Yandex Cloud: Распознавание длинных аудио](https://cloud.yandex.ru/docs/speechkit/stt/transcribation)
- [Yandex Cloud: Создание API-ключа](https://cloud.yandex.ru/docs/iam/operations/api-key/create)
- [Yandex Cloud: Концепции](https://cloud.yandex.ru/docs/storage/concepts/)

# Information from the community
- [habr: Yandex SpeechKit из командной строки bash/shell](https://habr.com/ru/post/583230/)

