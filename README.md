# Comics-publishing

Скрипт создан для скачивания комиксов с сайта [xkcd](https://xkcd.com/) и их публикации в вашей группе ВКонтакте.

## Environment

`Python3` должен быть уже установлен. Скачайте репозиторий. Установите зависимости командой:

`pip3 install -r -requirements.txt`

### Перемеменные окружения

В рабочей директории репозитория рядом с файлом `main.py` создайте файл `.env`с таким наполнением:
   ```
   VK_ACCESS_TOKEN=<ваш access token>  
   VK_GROUP_ID=<id группы, куда нужно публиковать комиксы>
   ```
### Как получить данные для переменных окружения:
Для работы со скриптом вам нужно получить API-токен VK. Вот [инструкция](https://www.pandoge.com/socialnye-seti-i-messendzhery/poluchenie-klyucha-dostupa-access_token-dlya-api-vkontakte) как это сделать. 
ID группы можно найти в ссылке вашей группы после слова public `https://vk.com/public<219612138>`

# Запуск
Запустите скрипт командой 
 
   `python main.py`
