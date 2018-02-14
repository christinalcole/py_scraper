#import libraries
import requests
from bs4 import BeautifulSoup

list_page = 'https://www.amazon.com/Best-Sellers-Toys-Games/zgbs/toys-and-games/ref=zg_bs_toys-and-games_home_all?pf_rd_p=089b8285-7691-4849-a7f5-b2fca56bf24a&pf_rd_s=center-1&pf_rd_t=2101&pf_rd_i=home&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=SGTHVTKSYJRG8VXK1JET&pf_rd_r=SGTHVTKSYJRG8VXK1JET&pf_rd_p=089b8285-7691-4849-a7f5-b2fca56bf24a'

page = requests.get(list_page)

soup = BeautifulSoup(page.text, 'html.parser')



rank_list = soup.find_all('span', attrs={'class':'zg_rankNumber'})
toy_name_list = soup.find_all(class_='p13n-sc-truncate p13n-sc-line-clamp-2')

rank_array = []
toy_array = []

for rank in rank_list:
    rank_array.append(rank.text.strip())

for toy in toy_name_list:
    toy_array.append(toy.text.strip())


result=zip(rank_array, toy_array)
result_list=list(result)

for r_l in result_list:
    for y in r_l:
        print (y)
