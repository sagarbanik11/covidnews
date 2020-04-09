
from bs4 import BeautifulSoup
import requests 
from urllib.request import urlopen
from django.shortcuts import render

def index(request):
	ir = requests.get("https://www.ndtv.com/topic/covid~19")
	isoup = BeautifulSoup(ir.content, 'lxml')
	icontent = isoup.find_all('p',{'class':'header fbld'})
	idate=isoup.find_all('p',{'class':'list_dateline'})
	iintro=isoup.find_all('p',{'class':'intro'})
	icontent=icontent[:5]
	idate=idate[:5]
	iintro=iintro[:5]
	x=0
	inews_data_JSON = [ ]
	for idata in icontent:
   		if idata:
   			inews_data={
   				'headline':idata.text,
   				'link':idata.a.get('href'),
   				'date':idate[x].text,
   				'intro':iintro[x].text
   				}
   			inews_data_JSON.append(inews_data)
   		x += 1
	print( inews_data_JSON)


	ar = requests.get("https://www.nbcnews.com/health/coronavirus")
	asoup = BeautifulSoup(ar.content, 'lxml')
	acontent = asoup.find_all('h2',{'class':'title___2T5qK'})
	adate=asoup.find_all('div',{'class':'timestamp___nPKJN f2 lh-none founders-mono fw1 mb2'})
	acontent=acontent[:5]
	adate=adate[:5]
	x=0
	anews_data_JSON = [ ]
	for adata in acontent:
   		if adata:
   			anews_data={
   				'headline':adata.a.text,
   				'link':adata.a.get('href'),
   				'date':adate[x].text,
   				}
   			anews_data_JSON.append(anews_data)
   		x += 1
	print( anews_data_JSON)
	alldata = { "content" : inews_data_JSON ,"content2":anews_data_JSON}
	return render(request, "index.html",alldata)