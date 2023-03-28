# Comics-publishing

Скрипт создан для скачивания комиксов с сайта [xkcd](https://xkcd.com/) и их публикации в вашей группе ВКонтакте.

## Запуск

`Python3` должен быть уже установлен.
Для работы со скриптом вам нужно получить API-токен VK. Вот [инструкция](https://www.pandoge.com/socialnye-seti-i-messendzhery/poluchenie-klyucha-dostupa-access_token-dlya-api-vkontakte) как это сделать.
1. Скачайте репозиторий.
2. В рабочей директории репозитория создайте файл `.env`с таким наполнением:
   ```
   VK_ACCESS_TOKEN=<ваш access token>  
   VK_CLIENT_ID=<id вашего приложения>
   ```
   
3. Установите зависимости командой 

   `pip3 install -r -requirements.txt` 
3. Запустите скрипт командой 
   
   `python main.py`
