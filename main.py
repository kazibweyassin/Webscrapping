import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

python_jobs = [job for job in job_elements if "python" in job.find("h2", class_="title").text.lower()]

for python_job in python_jobs:
    title_element = python_job.find("h2", class_="title")
    company_element = python_job.find("h3", class_="company")
    location_element = python_job.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
    git config --global user.name kazibweyassin
    git config --global user.email kazibweusama@gmail.com
          git remote add <name> <url>
