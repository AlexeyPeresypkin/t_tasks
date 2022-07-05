"""
В нашей школе мы не можем разглашать персональные данные пользователей, но чтобы преподаватель и ученик смогли объяснить нашей поддержке, кого они имеют в виду (у преподавателей, например, часто учится несколько Саш), мы генерируем пользователям уникальные и легко произносимые имена. Имя у нас состоит из прилагательного, имени животного и двузначной цифры. В итоге получается, например, "Перламутровый лосось 77". Для генерации таких имен мы и решали следующую задачу:
Получить с русской википедии список всех животных (https://inlnk.ru/jElywR) и вывести количество животных на каждую букву алфавита. Результат должен получиться в следующем виде:
А: 642
Б: 412
В:....
"""

from bs4 import BeautifulSoup
import requests


def get_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    div = soup.find('div', {'id': 'mw-pages'})
    data = tuple(i.text[0].lower() for i in div.find_all('li'))
    link = soup.find('a', text='Следующая страница')
    if not link:
        next_link = None
    else:
        next_link = 'https://ru.wikipedia.org/' + link['href']
    return data, next_link


if __name__ == '__main__':
    abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    url = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
    result = tuple()
    data, next_url = get_data(url)
    result += data

    while next_url:
        data, next_url = get_data(next_url)
        result += data

    for char in abc:
        print(f'{char.upper()}: {result.count(char)}')
