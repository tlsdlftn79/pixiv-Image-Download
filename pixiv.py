import os
from pixivpy3 import AppPixivAPI
import sys

REFRESH_TOKEN = 'API 토큰 발급 하시고 사용'

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

    # Continuously ask for artwork IDs and download images
    while True:
        print("작품번호 입력 (끝내려면 'exit' 입력):")
        artwork_id = input()

        if artwork_id.lower() == 'exit':
            break

        # Download image
        download_image(aapi, artwork_id, './images')

if __name__ == '__main__':
    main()

