from bs4 import BeautifulSoup
with open("home.html","r") as html_file:
    content=html_file.read()
    tags = BeautifulSoup(content,'lxml')
    print(tags.find('h5'))
    print(tags.find_all('h5'))

    tag_names_only=tags.find_all('h5')
    for name in tag_names_only:
        print(name.text)
