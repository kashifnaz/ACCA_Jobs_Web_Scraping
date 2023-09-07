import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract(city, page):
  '''Extracting information for jobs city-wise'''
  headers = {
      'User-Agent':
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'
  }
  url = f'https://jobs.accaglobal.com/jobs/{city}/{page}'
  r = requests.get(url, headers)
  soup = BeautifulSoup(r.content, 'html.parser')
  return soup


def transform(soup):
  '''Extracting relevant information from the soup object'''
  divs = soup.find_all('div', class_="lister__details cf js-clickable")
  for block in divs:
    title = block.find_all('span')[0].text
    location = block.find_all(
        class_="lister__meta-item lister__meta-item--location")[0].text
    salary = block.find_all(
        class_="lister__meta-item lister__meta-item--salary")[0].text
    recuriter = block.find_all(
        class_="lister__meta-item lister__meta-item--recruiter")[0].text
    a = [
        x['href'].strip()
        for x in block.find_all(class_='js-clickable-area-link', href=True)
    ]
    url = 'https://jobs.accaglobal.com' + str(a).replace("['", '').replace(
        "']", '')
    job = {
        'Title': title,
        'Location': location,
        'Salary': salary,
        'Recuriter': recuriter,
        'Link': url
    }
    joblist.append(job)


# Create and empty job list
joblist = []

# Creating a writer object for writing data in multiple sheets
writer = pd.ExcelWriter('ACCA_jobs.xlsx', engine='xlsxwriter')
for city in ['karachi', 'lahore', 'islamabad']:
  for i in range(0, 10):
    print(f'Getting {city.capitalize()} jobs at page, {i}')
    c = extract(city, i)
    transform(c)
df = pd.DataFrame(joblist).drop_duplicates()
df.to_excel(writer, sheet_name='ACCA_Jobs', index=False)
writer.close()
