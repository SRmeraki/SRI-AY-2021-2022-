import requests
from bs4 import BeautifulSoup

page = requests.get("https://news.mit.edu/topic/biomaterials")
soup = BeautifulSoup(page.content, 'html.parser')


def find_articles():
    bio_articles =[]
    all_headings = soup.findAll('span',{'itemprop':'name headline'})
    for span in all_headings:
        bio_articles.append(span.get_text())

    return bio_articles

def find_dates():
    bio_dates = []
    all_dates = soup.findAll('p', {'class': 'term-page--news-article--item--publication-date'})
    for p in all_dates:
        bio_dates.append(p.get_text())

    return bio_dates


def format_output():
    final_output=[]
    articles=find_articles()
    dates = find_dates()
    for i in range(len(articles)):
        output = articles[i] + '--->' + dates[i] +'\n'
        final_output.append(output)
    return final_output

def save_to_file():
    out = format_output()
    with open("data.txt","a+") as file:
        file.writelines((out))
        file.close()
        print("File created")

save_to_file()
