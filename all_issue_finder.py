from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm import tqdm

response = requests.get("https://www.house.gov/representatives")
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find_all("table", class_="table")

df = pd.DataFrame(columns=["Name", "State", "District", "Party", "Link", "Issue Links"])

for letter in tqdm(table):
    state = letter.find_all("caption")[0].text.strip() #type: ignore
    for row in letter.find_all("tr")[1:]: #type: ignore
        district = row.find_all("td")[0].text.strip() #type: ignore
        name = row.find_all("td")[1].text.strip() #type: ignore
        party = row.find_all("td")[2].text.strip() #type: ignore
        raw_link = row.find_all("td")[1].find("a") #type: ignore
        link = str(raw_link)[9:str(raw_link).find('">')] #type: ignore
        df = df._append({"Name": name, "State": state, "District": district, "Party": party, "Link": link, "Issue Links": []}, ignore_index=True) #type: ignore

df = df.iloc[:441, :]

#print(df.head())

links = df["Link"].tolist()
idx = 0
for link in tqdm(links[:3]):
    # print(link)
    if link[-1] == "/":
        link += "issues"
    else:
        link += "/issues"
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    issues_container = soup.find("div", class_="evo-views-row-container")
    issue_links = []
    if issues_container is None:
        try:
            alternate_container = soup.find("div", class_="issues-listed")
            for issue in alternate_container.find_all("a", class_="issues-item"): #type: ignore
                issue_links.append(str(issue)[str(issue).find('href="') + 6:str(issue).find('">')])
        except AttributeError:
            pass
    else:
        for issue in issues_container.find_all("div", class_="h3 mt-0 font-weight-bold"): #type: ignore
            raw_issue = str(issue)[str(issue).find('<a href="') + 9:str(issue).find('</a>')]
            issue = raw_issue[:raw_issue.find('">')]
            issue_links.append(issue)
    df.at[idx, "Issue Links"] = [link + issue for issue in issue_links]
    # print(df.at[idx, "Name"], df.at[idx, "Issue Links"])
    idx += 1

sum_value = 0
for issue_links in df["Issue Links"]:
    sum_value += len(issue_links)
print(df.head(), sum_value)