import logging
import os

# import requests
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv('KEY')
FILE = 'links_list.txt'
FOLDER = 'results'
URL = 'https://transcribe.api.cloud.yandex.net/speech/stt/{VERSION}/{METHOD}'
VERSION = 'v2'
METHOD = 'longRunningRecognize'

logging.basicConfig(
    level=logging.DEBUG,
    filename='main.log',
    format='%(asctime)s, %(levelname)s, %(name)s, %(message)s'
)


def main():
    logging.debug('Приложение запущенно')
    print('\nСкрипт транскрибации аудио, Yandex SpeechKit.\n'
          '---------------------------------------------\n\n'
          'Исходные данные — файл links_list.txt, ожидаемый формат строки:\n'
          'audio_title.opus\n'
          '(без заголовков, одним столбцом, с расширением файла).\n'
          'На выходе — все транскрипты в папке results, '
          'txt-файлы, именованные по названию аудио-файлов.\n\n'
          'Перед запуском убедитесь, '
          'что настройки в файле .env заполненны корректно.\n\n'
          'Всё готово? Начинаем? [y/n]')
    start = input()
    if start == 'y':
        processing_lines_of_the_file()
        logging.debug('Запуск скриптовой части подтверждён')
    else:
        logging.debug('Выполнение скриптовой части отклоненно пользователем')


def processing_lines_of_the_file():
    logging.debug('Попытка открыть файл со списком аудиофайлов')
    try:
        with open(FILE) as register:
            for one_audio in register:
                logging.debug(f'{one_audio} получен в обработку')
                title = f'{FOLDER}/{one_audio.split(".")[0]}.txt'

                logging.debug(f'{one_audio} полностью обработан')
    except Exception as e:
        message = f'Неразрешимая ошибка: {e}'
        logging_and_print_error_message(message)


def logging_and_print_error_message(message):
    logging.error(message)
    print(message)


if __name__ == '__main__':
    main()
