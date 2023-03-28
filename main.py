import random
import requests
from dotenv import load_dotenv
import os
from urllib.parse import urlparse
from pathlib import Path

from pprint import pprint


def download_random_comics():
    """Скачивает случайный комикс с сайта https"//xkcd.com"""
    last_comics_url = 'https://xkcd.com/info.0.json'
    last_comics_response = requests.get(last_comics_url)
    last_comics = last_comics_response.json()['num']
    accidental_comics = random.randint(1, last_comics)
    url = f'https://xkcd.com/{accidental_comics}/info.0.json'
    response = requests.get(url)
    comic_ingredients = response.json()
    img_url = comic_ingredients['img']
    img_path = urlparse(img_url).path
    img_filename = Path(img_path).name
    img_response = requests.get(img_url)
    img_response.raise_for_status()
    img = img_response.content
    comment = comic_ingredients['alt']
    with open(img_filename, "wb") as file_img:
        file_img.write(img)
    return img_filename, comment


def get_upload_url(vk_token, group_id):
    """Получаем ссылку для загрузки картинки на сервер vk"""
    method = 'photos.getWallUploadServer'
    url = f'https://api.vk.com/method/{method}/'
    params = {
        'group_id': group_id,
        'access_token': vk_token,
        'v': 5.131,
    }
    response = requests.get(url, params=params).json()

    return response['response']['upload_url']


def upload_photo_to_server(upload_url, img_filename):

    with open(img_filename, 'rb') as file:
        vk_file = {
            'photo': file,
            }
        response = requests.post(upload_url, files=vk_file)
    response_params = response.json()
    photo = response_params["photo"]
    server = response_params["server"]
    vk_hash = response_params["hash"]
    return photo, server, vk_hash


def save_wall_photo(vk_token, group_id, vk_hash, server):
    method = 'photos.saveWallPhoto'
    url = f'https://api.vk.com/method/{method}'
    params = {
        'group_id': group_id,
        'access_token': vk_token,
        'hash': vk_hash,
        'photo': photo,
        'server': server,
        'v': 5.131
    }
    savewall_response = requests.post(url, params=params).json()
    owner_id = savewall_response['response'][0]['owner_id']
    media_id = savewall_response['response'][0]['id']
    return owner_id, media_id


def publish_comic_to_vk(vk_token, group_id, owner_id, media_id, comment):
    method = 'wall.post'
    url = f'https://api.vk.com/method/{method}'
    params = {
        'token': vk_token,
        'owner_id':f'-{group_id}',
        'from_group': 1,
        'message': comment,
        'attachments': f'photo{owner_id}_{media_id}',
        'v': 5.131
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == '__main__':
    load_dotenv()
    group_id = os.environ['VK_CLIENT_ID']
    vk_token = os.environ['VK_ACCESS_TOKEN']
    img_filename, comment = download_random_comics()
    try:
        upload_url = get_upload_url(vk_token, group_id)
        photo, server, vk_hash = upload_photo_to_server(upload_url, img_filename)
        owner_id, media_id = save_wall_photo(vk_token, group_id,
                                             vk_hash, server)
        post_id = publish_comic_to_vk(vk_token, group_id, owner_id, media_id, comment)
        pprint (post_id)
    finally:
        if os.path.isfile(img_filename):
            os.remove(img_filename)



