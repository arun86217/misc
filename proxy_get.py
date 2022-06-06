#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import pandas as pd
import requests
from  net_data import url_proxy ,header_proxy


class proxy_list(object):
    
    page = requests.get(url=url_proxy, headers=header_proxy)
    page = BeautifulSoup(page.content,'lxml')
    table_columns = page.find('table').find_all('tr')
    elements =['th','td']
    # List_of_IP=[]
    # ip_list_header=[]

    def extract(self,row,elements, listing):
        temp_ip_list = []
        if row.find(elements):
            column = row.find_all(elements)
            for i in range(len(column)):
                try:
                    if len(column[i].string) !=0:
                        temp_ip_list.append(column[i].string)
                except :
                    pass
        return listing.append(temp_ip_list)

    def india_proxy(self,table_columns = table_columns,flag=0,elements=elements):
        ip_list_header=[]
        List_of_IP=[]
        for row in table_columns:
            
            if flag==0:
                self.extract(row,elements[0], ip_list_header)
                flag=1
            self.extract(row,elements[1], List_of_IP)
        List_of_IP_df = pd.DataFrame(List_of_IP[1:-1])
        List_of_IP_df.columns = ip_list_header[0]
        ip_india= List_of_IP_df[ List_of_IP_df['Country'] == 'India']
        http_list = self.df (ip_india[ip_india['Https'] =='no'])
        https_list = self.df (ip_india[ip_india['Https'] =='yes'])
        return http_list,https_list

    def df(self,ans):
        proxies = ans[['IP Address','Port']]
        proxies.set_index('IP Address',inplace=True)
        proxies =proxies.to_dict()
        proxies=proxies['Port'] 
        return proxies

    def list_of_proxies(self):
        http_dict , https_dict  = self.india_proxy()
        result_dict={}
        listed_list_https =[f'{ip}:{https_dict[ip]}' for ip in https_dict]
        listed_list_http =[f'{ip}:{http_dict[ip]}' for ip in http_dict]
        result_dict[0] = listed_list_http
        result_dict[1] = listed_list_https
        return result_dict