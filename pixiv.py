import os
from pixivpy3 import AppPixivAPI
import sys

REFRESH_TOKEN = 'api 번호'

def download_image(aapi, illust_id, base_path, file_name=None):
    detail = aapi.illust_detail(illust_id)

    if not file_name:
        file_name = f"{illust_id}_image.jpg"

    download_url = detail.illust.image_urls['large']
    aapi.download(download_url, path=base_path, name=file_name)
    print(f"Image downloaded: {file_name}")

def main():
    aapi = AppPixivAPI()

    # Perform login
    aapi.auth(refresh_token=REFRESH_TOKEN)

    # Enter the artwork ID
    print("작품번호 입력:")
    artwork_id = input()

    # Download image
    download_image(aapi, artwork_id, './images')

if __name__ == '__main__':
    main()
