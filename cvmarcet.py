from bs4 import BeautifulSoup
import requests
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)

data = []

for i in range(1, 200, 30):
    url = f'https://www.cvmarket.lt/darbo-skelbimai?op=search&search%5bjob_salary%5d=3&search%5bcategories%5d%5b0%5d=8&search%5bkeyword%5d=&ga_track={i}'

    response = requests.get(url)
    # print(response)

    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup.prettify())

    jobs = soup.find_all('article', {'data-component-id': True}) #tikrina, ar yra reikšmė data-component-id
    # print(jobs)

    for job in jobs:
        title = job.find('h2', class_='xl:text-xl font-bold mt-2 hover:underline').text.strip()
        company = job.find('span', class_='job-company mr-5').text.strip()
        salary_range = job.find('div', class_='inline-block mt-2.5 lg:mt-0 salary-block mr-5').text.strip()
        salary_min = job.find('div', {'data-salary-from': True})['data-salary-from']
        salary_max = job.find('div', {'data-salary-to': True})['data-salary-to']
        if salary_min and salary_max:
            salary_min = salary_min
            salary_max = salary_max
        else:
            salary_min = 'N/A'
            salary_max = 'N/A'
        salary_type = job.find('span', class_='text-slate-200 visited-group:text-gray-300 text-sm font-bold mt-0.5 salary-type').text.strip()
        city = job.find('span', class_='bg-blue-50 text-slate-500 py-1.5 px-3 font-bold text-sm rounded-full flex w-fit h-fit justify-center items-center space-x-1.5 cursor-defaults leading-4 location').text.strip()
        job_posted = job.find('div', class_='whitespace-nowrap').text.strip()
        data.append({'Title': title,
                     'Company': company,
                     'Min Salary': salary_min,
                     'Max Salary': salary_max,
                     'Salary Type': salary_type,
                     'City': city,
                     'Job Posted': job_posted
                     })

df = pd.DataFrame(data)
print(df)
