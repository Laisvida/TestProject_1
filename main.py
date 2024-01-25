bs4 import BeautifulSoup
import requests
# import pandas as pd

# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 500)
# data = []

# for i in range(1, 200, 30):
    url = 'https://www.cvmarket.lt/darbo-skelbimai?op=search&search%5Bjob_salary%5D=3&ga_track=homepage&search%5Bcategories%5D%5B%5D=8&search%5Bkeyword%5D='



    response = requests.get(url)
    print(response)

    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup.prettify())
    #
    # jobs = soup.find_all('article', {'data-component-id': True}) #tikrina, ar yra reikšmė data-component-id
    # # print(jobs)
    #
    # for job in jobs:
    #     title = job.find('h2', class_='xl:text-xl font-bold mt-2 hover:underline').text.strip()
    #     company = job.find('span', class_='job-company mr-5').text.strip()
    #     salary_range = job.find('div', class_='inline-block mt-2.5 lg:mt-0 salary-block mr-5').text.strip()
    #     salary_min = job.find('div', {'data-salary-from': True})['data-salary-from']
    #     salary_max = job.find('div', {'data-salary-to': True})['data-salary-to']
    #     if salary_min and salary_max:
    #         salary_min = salary_min
    #         salary_max = salary_max
    #     else:
    #         salary_min = 'N/A'