# hallo bro :v

from modul import *
import random


def head(url,respons):
	return {"Host":url.split("//")[1],"upgrade-insecure-requests":"1","cache-control":"max-age=0","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","referer":respons.url,"accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","user-agent":"Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36"}

class yo_ndak_tau_kok_tanya_saya:
	def __init__(self,url,cookie):
		
		self.url=url
		self.cookies=cookie

	def hoetang(self,id_post,tipe,komen,react=None,**data):
		try:
			respoN=req.get(self.url+id_post,cookies=self.cookies)
			respon=parser(respoN.text,"html.parser")
			for x in respon.find_all("a",{"href":True}):
				if "/reactions/picker/?is_permalink=1" in x["href"]:
					if "Tanggapi" in x.text:
						react=self.url+x["href"]
			if react!=None:
				for x in parser(req.get(react,cookies=self.cookies).text,"html.parser").find_all("a",{"href":True}):
					if f"reaction_type={tipe}" in x["href"]:
						req.get(self.url+x["href"],cookies=self.cookies)
			nv=respon.find_all("input",{"type":"hidden","name":True,"value":True})
			act=respon.find("form",{"method":"post","action":True})
			if len(nv)!=0 and act!=None:
				data.update({x["name"]:x["value"] for x in nv})
				data.update({"comment_text":komen})
				req.post(self.url+act["action"],headers=head(self.url,respoN),cookies=self.cookies,data=data)
		except: pass

	def follow(self,url_profil):
		try:
			respon=parser(req.get(self.url+url_profil,cookies=self.cookies).text,"html.parser")
			for x in respon.find_all("a",{"href":True}):
				if "/a/subscribe.php" in x["href"]:
					if "Ikuti" in x.text:
						req.get(self.url+x["href"],cookies=self.cookies)
		except: pass
		
	def change_bio(self,kata,**data):
		try:
			respon=parser(req.get(f"{self.url}/profile/basic/intro/bio",cookies=self.cookies).text,"html.parser")
			nv=respon.find_all("input",{"type":"hidden","name":True,"value":True})
			act=respon.find("form",{"method":"post","action":True})
			if len(nv)!=0 and act!=None:
				data.update({x["name"]:x["value"] for x in nv})
				data.update({"bio":kata,"publish_to_feed":"on"})
				req.post(self.url+act["action"],data=data,cookies=self.cookies)
		except: pass





	
