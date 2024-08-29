from bs4 import BeautifulSoup
import requests, csv, re
from datetime import datetime
date = datetime.today().date()
print(str(date))
URL = "https://apewisdom.io/all-crypto/"
#URL = "https://www.compulago.com/?srsltid=AfmBOorSFDl2YfmBiB_Nr0JDECCW2_pRDAugRqLFGsH2a14Yt9EkBSp9"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
criptos = soup.find_all("div", class_="company-name")
criptos = str(criptos)
criptos = criptos.replace('<div class="company-name">','|')
criptos = criptos.replace('</div>,','|')
criptos = criptos.replace('[','')
criptos = criptos.replace('</div>]','')
criptos = criptos.replace(' ','')
criptoclean = criptos.split("|")
print("###########")
#clean empty data from the list
criptoclean[:] = [x for x in criptoclean if x]
print(criptoclean)
with open('reddit.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(criptoclean)
 
URL = "https://apewisdom.io/all-crypto/"
#URL = "https://www.compulago.com/?srsltid=AfmBOorSFDl2YfmBiB_Nr0JDECCW2_pRDAugRqLFGsH2a14Yt9EkBSp9"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
criptos2 = soup.find_all("td", class_="td-center rh-sm")
print("######################")
#print(str(criptos2))
criptos2 = str(criptos2)
criptos2 = criptos2.replace('<td class="td-center rh-sm" data-sort="','|')
criptos2 = criptos2.replace('</td>,','|')
criptos2 = criptos2.replace(' ','')
criptos2 = criptos2.replace('[','')
criptos2 = criptos2.replace('</span></td>]','')
criptos2 = criptos2.replace('<spanclass="percentage-red">','')
criptos2 = criptos2.replace('<spanclass="percentage-green">','')
criptos2 = criptos2.replace("N/A","0%")
criptos2 = criptos2.replace('</span></td>','')
criptos2 = criptos2.replace('</span>','')
criptoclean2 = criptos2.split("|")
#remove empty data from the list
criptoclean2[:] = [x for x in criptoclean2 if x]
#extract only non par
criptoclean2 = [criptoclean2[i] for i in range(len(criptoclean2)) if i % 2 == 1]
print("#############")
#extract only data with percentages and clean the dirty data
pattern = r'(-?\d+%)+'
percentages = [re.search(pattern, elem).group(1) for elem in criptoclean2]
print(percentages)
 
with open('redditpercentages.csv', 'w+', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(percentages)
 
#########################
#Merge de data:
datamerge = {
  "Date": str(date),
  "Ranking1": str(criptoclean[0]),
  "Ranking2": str(criptoclean[1]),
  "Ranking3": str(criptoclean[2]),
  "Ranking1percentage": str(percentages[0]),
  "Ranking2percentage": str(percentages[1]),
  "Ranking3percentage": str(percentages[2])
}
print("##########")
print(datamerge)
 
######MAKING THE CSV
with open('RedditData.csv', mode='a', newline='') as file:
    #
    writer = csv.DictWriter(file, fieldnames=['Date','Ranking1','Ranking2','Ranking3','Ranking1percentage','Ranking2percentage','Ranking3percentage'])
    # writing the index header
    if file.tell() == 0:
        writer.writeheader()
    # writing de data
    writer.writerow(datamerge)