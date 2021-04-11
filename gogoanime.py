import requests
import os
import time 
from bs4 import BeautifulSoup
import sys
base_url = sys.argv[1]
default_formats =['HDP','360P','480P','1080P']
start_time =time.time()
def link_status(url):
	page = requests.get(url)
	if page.status_code ==200:
		result = (1,page.text)
		return result
	else:
		return 0
def links(url):
	result = link_status(url)
	if result[0]:
		read_html = BeautifulSoup(result[1],'lxml')
		return read_html
	else:
		return None
def download_link(element):
	link_to_download = element.find('a')['href']
	quality = element.find('a')
	return (quality)
strart_episode = int(sys.argv[2])
end_episode = int(sys.argv[3])
series_name = base_url.split('/')[-1].replace("-","_")+str(strart_episode)+"-"+str(end_episode)+str(round(time.time(),0))+".txt"
name= os.path.join(os.getcwd(),series_name)
with open(name,'w') as f:
	f.close()
while (strart_episode <=end_episode):
	print(f'scraping for episode{strart_episode}')
	page = base_url+'-episode-'+str(strart_episode)
	link_before_download = links(page).find_all('li',{'class':'dowloads'})[0].find('a')['href']
	download_lnks={}
	elements = links(link_before_download).find_all('div',{'class':'dowload'})
	for element in elements:
		if 'mp4' in element.find('a').contents[0]:
			quality = element.find('a').contents[0].split('\n')[-1].strip().replace(' - mp4',"")[1:-1]
			link_to_download = element.find('a')['href']
			download_lnks[quality]=[link_to_download]
	try:
		if '1080P' in download_lnks.keys():
			link_to_download = download_lnks['1080P']
		elif '720P' in download_lnks.keys():
			link_to_download = download_lnks['720P']
		elif 'HDP' in download_lnks.keys():
			link_to_download = download_lnks['HDP']
		elif '480P' in download_lnks.keys():
			link_to_download = download_lnks['480P']
		else:
			link_to_download = download_lnks['360P']
		with open(name,'a') as f:
			f.write(link_to_download[0])
			f.write('\n')
			f.close()
	except Exception as e:
		print("first try")
		print(f'error for episode {strart_episode} link')
	strart_episode = strart_episode+1
end_time=time.time()
time_took =round(end_time-start_time,0)
print(f' The File  {series_name} is in {os.getcwd()} and took {time_took} seconds')