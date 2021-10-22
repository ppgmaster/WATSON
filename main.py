import sys,shutil

runtah=["surya_gans/__pycache__","modul/__pycache__","wibu/__pycache__","saya_gans/ngewe/__pycache__"]

if sys.version[0]!="3":
	exit(" ! harap gunakan python3")

from surya_gans import awokawokawok
try: [shutil.rmtree(x) for x in runtah]
except: pass
awokawokawok()
