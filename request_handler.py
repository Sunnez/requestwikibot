import requests
from bs4 import BeautifulSoup


def get_info(req):
    url = f'https://ru.wikipedia.org/wiki/{req.title()}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    info = {
        'text': get_text(soup),
        'img': get_img(soup),
        'url': str(url)
    }

    return info


def get_text(soup):
    try:
        content_text = soup.find_all('div', class_='mw-parser-output')
        for content in content_text:
            main_text = content.find_all('p')
        text = str(main_text[0].text) + str(main_text[1].text)
        return text
    except:
        content_text = soup.find_all('div', class_='mw-parser-output')
        second_text = content.find_all('ul')
        return str(second_text[0].text)


def get_img(soup):
    try:
        content_img = soup.find_all('a', class_='image')
        link_img = content_img[0].find('img')
        return str(link_img.get('src'))
    except:
        return '-No images-'
