from bs4 import BeautifulSoup
with open("index.html","r") as html_file:
    content = html_file.read()
    soup=BeautifulSoup(content,'lxml')
    cards=soup.find_all('div',class_='card')

    for card in cards:
        course_names=card.h5.text
        course_prices= card.a.text.split()[-1]

        print(f"{course_names} costs {course_prices}")