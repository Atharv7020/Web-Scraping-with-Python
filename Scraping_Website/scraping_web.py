from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
jobs= soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for index,job in enumerate(jobs):
    published_date = job.find('span', 'sim-posted').text
    if 'few' in published_date:
        company_name = job.find('h3',class_ = 'joblist-comp-name').text.replace('   ',' ')
        required_skill= job.find('span',class_='srp-skills').text.replace(' ','')
        more_info = job.header.h2.a['href']
        with open(f'posts/{index}.txt','w') as f:
           f.write(f"Company Name = {company_name.strip()}\n")
           f.write(f'Skills Require = {required_skill.strip()}\n')
           f.write(f"More Info = {more_info}\n")
        print(f'File Saved{index}')



