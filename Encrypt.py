import io , random , time , os , way2sms , dropbox , gmail , tempfile , shutil , subprocess , sys , zlib , base64 , hashlib , math , gspread , pprint
from oauth2client.service_account import ServiceAccountCredentials
from itertools import islice
from ast import literal_eval
from tqdm import tqdm
from PIL import Image
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

#import threading
#from threading import Thread



dicto={"type": "service_account","project_id": "","private_key_id": "","private_key": "","auth_uri": "https://accounts.google.com/o/oauth2/auth","token_uri": "https://accounts.google.com/o/oauth2/token","auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/ebccard%40enbiocrypt-26c92.iam.gserviceaccount.com"}
scope=['https://spreadsheets.google.com/feeds']
creds=ServiceAccountCredentials.from_json_keyfile_dict(dicto,scope)

gmtest=gmail.GMail('@.com','')
dbx = dropbox.Dropbox("")
#w2s=way2sms.sms("","Q3236D")
#w2s=way2sms.sms("","")
m2=[]
emails=[]
mobiles=[]

z11=[27, 59, 236, 32, 242, 222, 162, 227, 45, 116, 56, 241, 33, 147, 121, 71, 158, 126, 68, 143, 85, 209, 81, 232, 144, 104, 204, 88, 250, 84, 243, 40, 224, 103, 44, 39, 167, 195, 221, 117, 92, 41, 52, 28, 50, 77, 15, 12, 172, 200, 219, 238, 169, 194, 154, 190, 38, 197, 160, 111, 65, 49, 187, 131, 231, 175, 21, 91, 191, 53, 235, 159, 120, 5, 164, 254, 8, 142, 19, 223, 30, 4, 109, 42, 36, 20, 14, 150, 29, 125, 62, 173, 16, 87, 55, 46, 80, 202, 171, 186, 1, 253, 151, 82, 210, 128, 119, 35, 249, 205, 229, 193, 146, 64, 178, 211, 75, 244, 170, 17, 247, 72, 181, 141, 215, 137, 124, 99, 188, 54, 97, 0, 102, 118, 106, 225, 86, 245, 60, 94, 155, 127, 107, 58, 76, 148, 214, 100, 7, 233, 66, 163, 89, 168, 115, 90, 139, 138, 184, 11, 208, 95, 152, 206, 122, 47, 196, 26, 239, 166, 43, 93, 177, 34, 165, 182, 79, 31, 129, 240, 98, 201, 96, 3, 23, 180, 161, 9, 114, 78, 67, 136, 10, 198, 2, 185, 212, 108, 179, 207, 157, 112, 199, 153, 251, 255, 110, 24, 105, 140, 217, 130, 37, 123, 113, 73, 48, 134, 220, 213, 218, 145, 57, 18, 6, 133, 226, 74, 216, 230, 237, 176, 156, 51, 248, 132, 174, 25, 203, 252, 63, 149, 228, 192, 13, 246, 234, 101, 70, 61, 189, 22, 83, 183, 135, 69]

while True:
	r11=random.sample(range(0,256),256)
	if r11[:]!=z11[:]:
		break

m11=[bytes([x]).decode('latin1') for x in z11]
asciicr={}
asciicr.update(zip(m11,r11))

def upresip(pv):
	fr=open("Recipient.txt","r")
	rv=[x.split(',') for x in fr.read().split(';')]
	#client = gspread.authorize(creds)
	#sheet=client.open('EnBioCrypt-Resip').sheet1
	#pointer1=int(sheet.cell(1, 1).value)
	
	client = gspread.authorize(creds)
	sheet=client.open('EnBioCrypt-Resip').sheet1
	cell_list1=sheet.range("A"+str(1)+':A'+str(1))
	#cell_list1[0].value=int(cell_list1[0].value)+1
	pointer1=int(cell_list1[0].value)
	cell_list = sheet.range("A"+str(pointer1+1)+':D'+str(pointer1+len(rv)))
	pointer1=int(cell_list1[0].value)+1
	#sheet.update_cell(pointer, 1 ,pointer)
	#pv.insert(0,pointer1)
	data=0
	for i in range(0,len(cell_list),4):
		email,mobile=rv[data]
		cell_list[i].value=pointer1
		cell_list[i+1].value=pv[0]
		cell_list[i+2].value=email
		cell_list[i+3].value=int(mobile)
		pointer1+=1
		cell_list1[0].value=int(cell_list1[0].value)+1
		data+=1
		emails.append(email)
		mobiles.append(mobile)
		
	cell_list.insert(0,cell_list1[0])
	sheet.update_cells(cell_list)
	fr.close()

def asciio(pv):
	client = gspread.authorize(creds)
	sheet=client.open('EnBioCrypt-ASCII').sheet1
	cell_list1=sheet.range("A"+str(1)+':A'+str(1))
	#cell_list1[0].value=int(cell_list1[0].value)+1
	cell_list1[0].value=int(cell_list1[0].value)+1
	pointer1=int(cell_list1[0].value)
	cell_list = sheet.range("A"+str(pointer1)+':IX'+str(pointer1))
	
	cell_list[0].value=pointer1
	cell_list[1].value=pv[0]
	
	j=0
	#print(len(cell_list),len(r11))
	for i in range(2,len(cell_list)):
		cell_list[i].value=r11[j]
		j+=1
	
	cell_list.insert(0,cell_list1[0])
	sheet.update_cells(cell_list)

def pause():
    programPause = input("\nPress the <ENTER> key to continue...")


def exfun(x):
	return 255-abs((x%509)-255)

#expt
def emver(email):
	pol=1
	while pol<=3:
		mn=random.randint(100000,999999)
		msg = gmail.Message('EnbioCrypt - A New Level Encryption',to=email,html="<center><img src='https://i.imgur.com/0evrOTf.jpg'/></center><br/><br/>Thanks For Using Our Service.<br/><br/>Your Verification Code is: <b>"+str(mn)+"</b><br/><br/>With Regards,<br/><b>CEO Of EnBioCrypt</b>")
		gmtest.send(msg)
		kl=int(input("\nEnter The Verification code sent over mail: "))
		if kl==mn:
			print("\nSuccessfully Verified Email..")
			f1.write(''.join(em))
			f1.write('\n')
			break
		else:
			print("\nVerification Failed,Code is resent,Attempts Left "+str(3-pol))
			pol+=1
	if pol>3:
		print("\nSession Expired!!!,Please Retry the registration process..");
		sys.exit()

def getph(email):
	dirpath1 = tempfile.mkdtemp()
	with open(dirpath1+"/details.txt", "wb") as f5:
		metadata, res = dbx.files_download(path='/EnBioCrypt/Logins/Emails/'+email+'/details.txt')
		#print(res.content)
		f5.write(res.content)
	f5.close()
	#os.remove(dirpath+"/test.txt")
	i=0
	f6=open(dirpath1+"/details.txt", "r")
	for j in f6:
		if i==2:
			break
		i+=1
		fin=j
	f6.close()
	shutil.rmtree(dirpath1)
	return fin[:10]

def getnam(email):
	dirpath1 = tempfile.mkdtemp()
	with open(dirpath1+"/details.txt", "wb") as f5:
		metadata, res = dbx.files_download(path='/EnBioCrypt/Logins/Emails/'+email+'/details.txt')
		#print(res.content)
		f5.write(res.content)
	f5.close()
	#os.remove(dirpath+"/test.txt")
	i=0
	f6=open(dirpath1+"/details.txt", "r")
	for j in f6:
		if i==3:
			break
		i+=1
		fin=j
	f6.close()
	shutil.rmtree(dirpath1)
	return fin


def mobcon(email):
	#shutil.rmtree(dirpath1)
	#os.remove(dirpath1+"/details.txt")
	fin=str(getph(email))
	try:
		r1=dbx.files_get_metadata('/EnBioCrypt/Logins/Emails/'+email+'/Phone/'+fin+'.txt')
		return int(fin)
	except:
		print("\nData Breach Attempt Detected...Session Ending...")
		sys.exit()
	
	
def moveri(email):
	pn=mobcon(email)
	pol=1
	while pol<=3:
		try:
			mn=random.randint(100000,999999)
			w2s.send(str(pn),"\nAuthentication Code is: "+str(mn)+"\n\n-Made With Love From EnBioCrypt." )
			kl=int(input("\nEnter The Authentication code sent over Mobile: "))
			if kl==mn:
				print("\nSuccessfully Authorized Phone Number..")
				break
			print("\nWrong Authentication code,The code has been resent,Attempts Left "+str(3-pol))
			pol+=1
		except:
			print("\nWrong Authentication code,The code has been resent,Attempts Left "+str(3-pol))
			pol+=1
	if pol>3:
		print("\nSession Expired!!!,Please Retry the registration process..")
		sys.exit()

def pscod(email):
	while True:
		try:
			ver=int(input("\nEnter 6 Digit Pin Code as Password: "))
			ver1=int(input("\nRe-Enter Pin Code: "))
			if len(str(ver))==6 and ver==ver1:
				print("\nSuccessfully Added Pass-code...")
				dbx.files_delete('/EnBioCrypt/Logins/Emails/'+email+'/PassCode')
				f11=open(dirpath1+"/test.txt","w")
				f11.write("Test")
				f11.close()
				with open(dirpath1+"/details.txt", "rb") as f21:
					dbx.files_upload(f2.read(),'/EnBioCrypt/Logins/Emails/'+email+'/PassCode/'+str(ver)+'.txt', mute = True)					
				print("\nSuccessfully Changed..")
				break
			else:
				print("\nVerification Codes Did Not Match...")
		except:
			print("\nWrong Pass-code pattern , Re-Enter...")
		
		
def chkpn(email):
	while True:
		try:
			pas=int(input("\nEnter Your Login Pass-code: "))
			r1=dbx.files_get_metadata('/EnBioCrypt/Logins/Emails/'+email+'/PassCode/'+str(pas)+'.txt')
			moveri(email)
			break
		except SystemExit:
			sys.exit()
		except:
			tyy=input("\nForgot Pass-Code,Wanna Reset?(y/n): ")
			if tyy=='y' or tyy=='Y':
				emver(email)
				pscode(email)
			tyy=input("\Wanna ?(y/n): ")
				
def chklogin():
	while True:
		try:
			email=input("\nEnter Your Login Mail Id: ")
			if '*' in email:
				raise ValueError("\nIf Your Trying to Use Wildcards, well then , you can't...")
			r1=dbx.files_get_metadata('/EnBioCrypt/Logins/EmailsDump/'+email+'.txt')
			chkpn(email)
			break
		except:
			lkj=input("\nYour Email (or password contains Alphabet) Was not found in OUR Database,Do you wanna re-enter Mail address?(y/n)")
			if lkj=='n' or lkj=='N':
				print("\nSession Expired..,You can use Signuper in case you wanna signup in our system..")
				print("\n\t\t--Designed By: EnBioCrypt\n\t\t--Copyrights: Dinesh Surisetti\n")
				pause()
				sys.exit()
	return email
#expt

#f7=open("tests.txt","w")

def nearp(sta): #m2 global and m2 to be added
	global m2
	m2=[]
	#n=[]
	if sta>=10:
		if sta<25:
			sta=random.randint(10,sta)
		else:
			sta=random.randint(32,50)
	for i in range(sta):
		while True:
			s=random.randint(33,125)
			if s!=96 and s<126:
				#n.append(s)
				#m2.append(n[-1])
				m2.append(s)
				break
	
#Negation And Encrypt Program:
def rev(p1,q1):
    for i in range(len(p1)):
        for j in range(8):
            if not q1[i][j]==0:
                q1[i][j]=0
            else:
                q1[i][j]=1
    return(q1)
#Binary to Decimal Conversion
def pros(p2,q2):
    n=[]
    k=0
    temp=0
    for i in range(len(p2)):
        for j in range(7,-1,-1):
            temp+=q2[i][j]*pow(2,k)
            k+=1
        n.append(temp)
        temp=0
        k=0
    return(n)


def chekf(mo):
	while True:
		try:
			mo+=str(random.randint(0,100000000))
			if hashlib.md5(mo.encode('latin1')).hexdigest() not in hasher:
				if usr!='n':
					if not os.path.exists(tempfile.gettempdir()+"\\Dumps\\"+mo+".png"):
						return mo
				else:
					r1=dbx.files_get_metadata('/EnBioCrypt/Dumps/'+str(hashlib.md5(mo.encode('latin1')).hexdigest())+'.png')
		except:
			return mo

def get(t):
	if t:
		return 1
	else:
		return 0

#Expt
def act1(email):
	print("\nWelcome to Download Encrypted Files From Storage (or) Generate Private Keys For Specified Files:\n") 
	mobno=getph(email)
	r1=dbx.files_list_folder('/EnBioCrypt/Logins/Emails/'+email+'/Storage('+email+')')
	if len(r1.entries)==0:
		print("\nNo Files to show..")
		pause()
	else:
		while True:
			r1=dbx.files_list_folder('/EnBioCrypt/Logins/Emails/'+email+'/Storage('+email+')')
			if len(r1.entries)==0:
				print("\nNo Files to show..")
				pause()
				break
			print("\nList of File Contents:")
			for i in range(len(r1.entries)):
				print(str(i+1)+'.'+r1.entries[i].name)
			chp=int(input("\n\nChoose the File No. to Download: "))
			if chp<=len(r1.entries) and chp>0:
				polo=input("\nWanna Download the File?(y/n): ")
				if polo=='y' or polo=='Y':	
					chp=chp-1
					with open("EncryptDumps/en"+r1.entries[chp].name, "wb") as f5:
						metadata, res = dbx.files_download(path='/EnBioCrypt/Logins/Emails/'+email+'/Storage('+email+')/'+r1.entries[chp].name)
						#print(res.content)
						f5.write(res.content)
					f5.close()
					print("\n The Requested Encrypted File has been downloaded to EncryptDumps with name: en"+r1.entries[chp].name)
					metadata,res = dbx.files_download(path='/EnBioCrypt/Logins/Emails/'+email+'/PrivateKeys/'+r1.entries[chp].name)
					mcon=(res.content).decode('ascii')
					msg = gmail.Message('EnbioCrypt - A New Level Encryption',to=email,html="<center><img src='https://i.imgur.com/0evrOTf.jpg'/></center><br/><br/>Thanks For Using Our Service.<br/><br/>Your Private KEy for File <b>en"+r1.entries[chp].name+"</b> is: <b>"+mcon+"</b><br/><br/>With Regards,<br/><b>CEO Of EnBioCrypt</b>")
					gmtest.send(msg)
					w2s.send(mobno,"\nCheck mail for file,sender's info.\n\nFile: en"+r1.entries[chp].name+"\n\nPrivate Key("+str(len(mcon))+"Chars):\n\n"+mcon+"\n\n-Made With Love From EnBioCrypt." )
					print("\nPrivate Key Has been Sent to Email and Mobile..")
				else:
					chp=chp-1
					metadata,res = dbx.files_download(path='/EnBioCrypt/Logins/Emails/'+email+'/PrivateKeys/'+r1.entries[chp].name)
					mcon=(res.content).decode('ascii')
					msg = gmail.Message('EnbioCrypt - A New Level Encryption',to=email,html="<center><img src='https://i.imgur.com/0evrOTf.jpg'/></center><br/><br/>Thanks For Using Our Service.<br/><br/>Your Private KEy for File <b>"+r1.entries[chp].name+"</b> is: <b>"+mcon+"</b><br/><br/>With Regards,<br/><b>CEO Of EnBioCrypt</b>")
					gmtest.send(msg)
					w2s.send(mobno,"\nCheck mail for file,sender's info.\n\nFile: "+r1.entries[chp].name+"\n\nPrivate Key("+str(len(mcon))+"Chars):\n\n"+mcon+"\n\n-Made With Love From EnBioCrypt." )
					print("\nPrivate Key Has been Sent to Email and Mobile..")
			else:
				print("\nPlease Choose Correctly...")
			iop=input("\nDo you wanna Download More files(y/n)?: ")
			if iop=='n' or iop=='N':
				break
		pause()
		
def act2(email):
	print("\nWelcome to Share Files From Drive to Friends Section\n\n")
	r1=dbx.files_list_folder('/EnBioCrypt/Logins/Emails/'+email+'/Storage('+email+')')
	nam=getnam(email)
	if len(r1.entries)==0:
		print("\nNo Files to share with..")
		pause()
	else:
		while True:
			print("\nList of File Contents:")
			for i in range(len(r1.entries)):
				print(str(i+1)+'.'+r1.entries[i].name)
			chp=int(input("\n\nChoose the File No. to Share: "))
			if chp<=len(r1.entries) and chp>0:
				chp=chp-1
				ipl=input("Do you wanna share Temporary Link?(y/n): ")
				if ipl=='y' or ipl=='Y':
					result = dbx.files_get_temporary_link('/EnBioCrypt/Logins/Emails/'+email+'/Storage('+email+')/'+r1.entries[chp].name)
				else:
					result=dbx.sharing_create_shared_link('/EnBioCrypt/Logins/Emails/'+email+'/Storage('+email+')/'+r1.entries[chp].name, short_url=True, pending_upload=None)
				smil=input("\nEnter Recipient's Mail Id: ")
				sphn=str(input("\nEnter Recipient's Phone no.: "))
				metadata,res = dbx.files_download(path='/EnBioCrypt/Logins/Emails/'+email+'/PrivateKeys/'+r1.entries[chp].name)
				mcon=(res.content).decode('ascii')
				sup=r1.entries[chp].name
				if len(sup)>8:
					sup1=sup[:4]+"..."+sup[-5]+".txt"
				else:
					sup1=sup
				w2s.send(sphn,"\nCheck mail for file,sender's info.\n\nFile: "+sup1+"\n\nPrivate Key("+str(len(mcon))+"Chars):\n\n"+mcon+"\n\n-Made With Love From EnBioCrypt." )
				if ipl=='y' or ipl=='Y':
					msg = gmail.Message('EnbioCrypt - A New Level Encryption',to=smil,html="<center><img src='https://i.imgur.com/0evrOTf.jpg'/></center><br/><br/>Thanks For Using Our Service.<br/>The Encrypted File has been uploaded in our storage space , <b>The link for Your Encrypted File is:</b><br/><br/>Sender's Name: <b>"+nam+"<br/><br/></b>File Name: <b>en"+r1.entries[chp].name+"</b><br/><br/><b>"+result.link+"</b><br/><br/>The Private Key Has been/will be sent to <b>Mobile Phone: +91xxxxxx"+sphn[6:]+"</b><br/><br/><b>NOTE:</b>The download link will be only available for limited time,<b>Please be sure to download ASAP(Within 4 Hours)</b>.<br/><br/>With Regards,<br/><b>CEO Of EnBioCrypt</b>")
				else:
					msg = gmail.Message('EnbioCrypt - A New Level Encryption',to=smil,html="<center><img src='https://i.imgur.com/0evrOTf.jpg'/></center><br/><br/>Thanks For Using Our Service.<br/>The Encrypted File has been uploaded in our storage space , <b>The link for Your Encrypted File is:</b><br/><br/>Sender's Name: <b>"+nam+"<br/><br/></b>File Name: <b>en"+r1.entries[chp].name+"</b><br/><br/><b>"+result.url+"</b><br/><br/>The Private Key Has been/will be sent to <b>Mobile Phone: +91xxxxxx"+sphn[6:]+"</b><br/><br/><b>NOTE:</b>The download link will be only available for limited time,<b>Please be sure to download ASAP(Within 4 Hours)</b>.<br/><br/>With Regards,<br/><b>CEO Of EnBioCrypt</b>")
				gmtest.send(msg)
				print("\n The Requested Encrypted File has been sent to "+smil+" and Private Key to "+sphn)
			else:
				print("\nPlease Choose Correctly...")
			iop=input("\nDo you wanna Share More files(y/n)?: ")
			if iop=='n' or iop=='N':
				break
		pause()

def act3(email):
	while True:
		try:
			mo=str(input("\nEnter The File Name: "))
			po=str(input("\nEnter The File Extension Type: "))
			#print("\nActual Data and Encryption:")
			mobno=str(getph(email))
			rector=email
			start_time = time.time()
			f=open(mo+"."+po)
			dirpath = tempfile.mkdtemp()
			f1=open(dirpath+"/en"+mo+".txt", "w" ,encoding="latin1")
			#f3=open("enkey"+mo+".txt", "w",encoding="latin1")
			#rprime=[0 for i in range(8)]
			siz=os.stat(mo+"."+po)
			rprime=nearp(int(siz.st_size))
			for m in f:
				marr=[[0 for i in range(8)] for j in range(len(m))]
				revarr=[[0 for i in range(8)] for j in range(len(m))]
				#f1.write(line)
				conv(m,marr,rprime)
				for i in range(len(m)):
					for j in range(8):
						revarr[i][j]=marr[i][j]
				rev(m,revarr)
				b2d=pros(m,revarr)
				#b2dp=pros(m,marr)
				#print(d)
				#print(len(b2d))
				#print("\nFinal Encrypted String is:",''.join(bytes([i]).decode('cp437') for i in b2d))
				for i in b2d:
					#print(b2)
					f1.write(''.join(bytes([i]).decode('latin1')))
				#print(m2,len(m2))
			f.close()
			f1.close()
			
			def chekf():
				mpc=""
				for i in mo:
					mpc+=str(i)
				while(True):
					try:
						r1=dbx.files_get_metadata('/EnBioCrypt/Logins/Emails/'+email+'/Storage('+email+')/en'+mpc+'.txt')
						mpc+=str(random.randint(0,100000000))
					except:
						return mpc
			
			moc=chekf()
			#print('rename '+dirpath+"\en"+mo+'.txt '+'en'+moc+'.txt >/dev/null 2>&1')
			subprocess.check_output('rename '+dirpath+"\en"+mo+'.txt '+'en'+moc+'.txt', shell=True)
			#os.system('rename '+dirpath+"\en"+mo+'.txt '+'en'+moc+'.txt')>/dev/null 2>&1')
			#pause()
			with open(dirpath+"\en"+moc+".txt", "rb") as f2:
				dbx.files_upload(f2.read(),'/EnBioCrypt/Logins/Emails/'+email+'/Storage('+email+')/en'+moc+'.txt', mute = True)
			
			gm=input("\nDo You want have a copy of Encrypted File?(Will be Stored in 'Dumps' Folder)(y/n)?: ")
			if gm=='y' or gm=='Y':
				subprocess.check_output('move '+dirpath+'\* Dumps', shell=True)
			#os.system('move '+dirpath+'\* Dumps >/dev/null 2>&1')
			#result = dbx.files_get_temporary_link('/EnBioCrypt/Dumps/en'+moc+'.txt')
			msg = gmail.Message('EnbioCrypt - A New Level Encryption',to=rector,html="<center><img src='https://i.imgur.com/0evrOTf.jpg'/></center><br/><br/>Thanks For Using Our Service.<br/>The Encrypted File has been uploaded in our storage space , <b>The link for Your Encrypted File is can be manually generated.</b><br/><br/>File Name: <b>en"+moc+".txt</b> has been uploaded successfully.<br/><br/>The Private Key Has been/will be sent to <b>Mobile Phone: +91xxxxxx"+mobno[6:]+"</b><br/><br/>With Regards,<br/><b>CEO Of EnBioCrypt</b>")
			gmtest.send(msg)
			finstr=""
			finstr=''.join(bytes([int(i)]).decode('latin1') for i in m2)
			f9=open(dirpath+"/test.txt", "w")
			f9.write(finstr)
			f9.close()
			with open(dirpath+"/test.txt", "rb") as f00:
				dbx.files_upload(f00.read(),'/EnBioCrypt/Logins/Emails/'+email+'/PrivateKeys/en'+moc+'.txt', mute = True)
			f00.close()
			shutil.rmtree(dirpath)
			#print(m2)
			sup1=""
			sup="en"+moc
			if len(sup)>8:
				sup1=sup[:4]+"..."+sup[-1]+".txt"
			else:
				sup1=sup+".txt"
			w2s.send(mobno,"\nCheck mail for file,sender's info.\n\nFile: "+sup1+"\n\nPrivate Key("+str(len(finstr))+"Chars):\n\n"+finstr+"\n\n-Made With Love From EnBioCrypt." )
			f2.close()
			#f3.write(finstr)
			print("Done Encryption..\nSent Encrypted File: "+"en"+moc+".txt to :"+rector+"\nPrivate Key has been sent to: "+mobno)
			print("\nTotal Time For Encryption:%s seconds" % (time.time() - start_time))
		except:
			print("\nWrong File Name , Error Uploading Retry..")
		slet=input("\nWanna Upload More Files?(y/n): ")
		if slet=='n' or slet=='N':
			break
	pause()
			
def act4(email):
	print("\nWelcome to Delete File From Storage Section:\n\n")
	r1=dbx.files_list_folder('/EnBioCrypt/Logins/Emails/'+email+'/Storage('+email+')')
	if len(r1.entries)==0:
		print("\nNo Files to share with..")
		pause()
	else:
		while True:
			r1=dbx.files_list_folder('/EnBioCrypt/Logins/Emails/'+email+'/Storage('+email+')')
			print("\nList of File Contents:")
			for i in range(len(r1.entries)):
				print(str(i+1)+'.'+r1.entries[i].name)
			if len(r1.entries)==0:
				print("\n No Files to Delete..")
				break
			chp=int(input("\nChoose the File No. to Delete: "))
			if chp<=len(r1.entries) and chp>0:
				chp=chp-1
				ipl=input("Do you really wanna Delete?(y/n): ")
				if ipl=='y' or ipl=='Y':
					dbx.files_delete('/EnBioCrypt/Logins/Emails/'+email+'/Storage('+email+')/'+r1.entries[chp].name)
					dbx.files_delete('/EnBioCrypt/Logins/Emails/'+email+'/PrivateKeys/'+r1.entries[chp].name)
					print("\nSuccessfully Deleted..")
				else:
					print("\n No Files Were Deleted..")
					break
			else:
				print("\n No Files to Delete..")
				break
			sellop=input("\nWanna Delete more Files?(y/n): ")
			if sellop=='n' or sellop=='N':
				break
		pause()
	
def act5(email):
	pn=str(getph(email))
	print("\nWelcome to Revoke Storage Link Section.\n\n")
	sl=dbx.sharing_create_shared_link('/EnBioCrypt/Logins/Emails/'+email+'/Storage('+email+')', short_url=True, pending_upload=None)
	msg = gmail.Message('EnbioCrypt - A New Level Encryption',to=em,html="<center><img src='https://i.imgur.com/0evrOTf.jpg'/></center><br/><br/>Thanks For Using Our Service.<br/><br/>Your Storage Link is: <b>"+sl.url+"</b><br/><br/><b>NOTE: </b>The Above Storage is Private Link Which will ONLY contain Your Encrypted Files,<b>The LINK IS PRIVATE, share it with your own RISK</b>,Private Keys can only be obtained On Mobile that to only when you Request it.<br/><br/>With Regards,<br/><b>CEO Of EnBioCrypt</b>")
	gmtest.send(msg)
	w2s.send(str(pn),"\nYour PRIVATE Storage LINK is:\n\n"+sl.url+"\n\nCheck Mail for More Info.\n\n-Made With Love From EnBioCrypt." )
	print("\nPRIVATE Storage LINK has been sent to Mobile and Email...");
	pause()

def act6():
	print("\nExit \n\n")
	print("\nSuccessful Logout.. , Thanks for using our Service..")
	print("\n\t\t--Designed By: EnBioCrypt\n\t\t--Copyrights: Dinesh Surisetti\n")
	pause()
	sys.exit()
	

fillo=input("\nDo you Login and share File?(y/n): ")
if fillo=='y' or fillo=='Y':
	em=chklogin()
	while True:
		print("\nMenu Dashboard\n\n1.Download Encrypted Files From Storage (or) Generate Private Keys For Specified Files\n2.Share Files From Drive to Friends.\n3.Encrypt and Upload Files to Storage\n4.Delete Files from storage\n5.Revoke Storage Link\n6.Exit\n\n\nNOTE: Features Of Changing PAssword/NAme/MAil are still under Development\n      We strictly Suggest to avoid sharing the storage link, That must be shared at your own interest\n      We Don't provide direct share feature up here,Choose without Login Feature for that,Expected to be added in near future. \n      Temporary Link can only retain for 4 hours of share(Recommended)\n\n")
		chip=int(input("\nEnter Your Choice:" ))
		if chip==1:
			act1(em)
		elif chip==2:
			act2(em)
		elif chip==3:
			act3(em)
		elif chip==4:
			act4(em)
		elif chip==5:
			act5(em)
		elif chip==6:
			act6()
		elif chip>6 and chip<=0:
			print("\nWrong Choice.. Re-Enter the choice")
		else:
			print("\nWrong Choice...")
#Expt

else:
	while True:	
		cprint(figlet_format('E n B i o C r y p t !'),'green',attrs=['bold'])
		mo=str(input("\nEnter The File Name: "))
		po=str(input("\nEnter The File Extension Type: "))
		#print("\nActual Data and Encryption:")
		print("\nEnter the Recipient Details on Recipient.txt File.{Format: Email1,Phone1;Email2,Phone2;....}")
		pause()
		usr=input("\nWanna Encrypt OFFLINE(y/n): ")
		kter=str(input("\nEnter Sender's Name: "))
		if usr!='n':
			if not os.path.exists(tempfile.gettempdir()+"\\Dumps"):
				os.mkdir(tempfile.gettempdir()+"\\Dumps")
		start_time = time.time()
		f=open(mo+"."+po,"rb")
		siz=os.stat(mo+"."+po)
		temp_size=0
		fihash=[]
		hasher=[]
		pv=[]
		cou=0
		print("Total File Size:",round(siz.st_size/1024/1024,2),"MB")
		no=int(siz.st_size/(siz.st_size/10))
		while cou<no:
			moc=chekf(mo)
			if hashlib.md5(moc.encode('latin1')).hexdigest() not in hasher:
				hasher.append(hashlib.md5(moc.encode('latin1')).hexdigest())
				cou+=1
		
		print("\nDone Scanning..\n")
		#print(hasher,len(hasher),cou)
		#pause()
		done=int(siz.st_size/10)
		cprint(figlet_format('E n B i o C r y p t !'),'green',attrs=['bold'])
		print("\nPlease Wait while we Encrypt and Upload Your File: \n")
		
		for i in tqdm(range(no)):
			if not fihash:
				fihash.append(mo)
				fihash.append(kter)
				fihash.append(hasher[-1])
				pv.append(hasher[-1])
				verid=''.join(x for x in hasher)
				pv.append(hashlib.md5(verid.encode('latin1')).hexdigest())
			
			m=f.read(done)+f.readline()
			m=base64.encodestring(m)
			m=m.decode("latin1")
			im1 = Image.new('RGBA',(int(math.sqrt(len(m)/4)+2),int(math.sqrt(len(m)/4)+2)))
			nearp(int(siz.st_size))
			if not m:
				break
			
			#print(m)
			if hasher:
				moc=hasher[-1]
				hasher=hasher[:-1]
			
			if hasher:
				m+=hasher[-1]
			
			marr=[asciicr[x] for x in m]

			finstr=''.join(bytes([int(i)]).decode('latin1') for i in m2)
			pv.append('"'+finstr+'"')
			finstr2=hashlib.md5(finstr.encode('latin1')).hexdigest()
			#change in below for loop
			z=0
			h=0
			k=0
			b2d=[]
			
			for i in range(len(m)):
				if z>=32:
					z=0
					finstr2=hashlib.md5(finstr2.encode('latin1')).hexdigest()
					h+=1
				if h>=32:
					h=0
				numbers="{0:b}".format(exfun(sum(bytearray(hashlib.md5(finstr2[z].encode('latin1')).hexdigest(),'latin1')))).zfill(8)
				if k>=len(m2):
					k=0
				b2d.append(255-((marr[i]^int(numbers,2)) ^ m2[k]))
				k+=1
				z+=1

			x=1
			y=0
			count=str(len(b2d))
			
			while len(b2d)%4 !=0:
				b2d.append(255)
			for i in range(0,len(b2d),4):
				#print(b2d[i],b2d[i+1],b2d[i+2])
				if y==int(math.sqrt(len(m)/4)+2):
					y=0
					x+=1
				if x>=int(math.sqrt(len(m)/4)+2):
					break
				im1.putpixel((x,y),(b2d[i],b2d[i+1],b2d[i+2],b2d[i+3]))
				y+=1
			
			ter=len(count)
			#print(1,count,int(ter/4)+get(ter%4),ter,4-ter%4)
			im1.putpixel((0,0),(1,int(ter/4)+get(ter%4),ter,len(po)))

			while len(count)%4 !=0:
				count+="1"
			y=1	
			while count:
				im1.putpixel((0,y),(int(count[0]),int(count[1]),int(count[2]),int(count[3])))
				y+=1
				count=count[4:]
			
			if hasher:
				im1.putpixel((int(math.sqrt(len(m)/4)+1),int(math.sqrt(len(m)/4)+1)),(0,0,0,0))
			else:
				im1.putpixel((int(math.sqrt(len(m)/4)+1),int(math.sqrt(len(m)/4)+1)),(1,1,1,1))
			
			if usr=='n':
				stream=io.BytesIO()
				im1.save(stream,"PNG")
				stream.seek(0)
				dbx.files_upload(stream.getvalue(),"/EnBioCrypt/Dumps/"+moc+".png",mute=True)
			else:
				im1.save(tempfile.gettempdir()+"\\Dumps\\"+moc+".png","PNG")
			
			im1.close()
			#print(b2d)
			#pause()
		print("\nGenerating Final Image Please Wait..\n")
		#pause()
		upresip(pv)
		asciio(pv)
		client = gspread.authorize(creds)
		sheet=client.open('EnBioCrypt').sheet1
		cell_list1=sheet.range("A"+str(1)+':A'+str(1))
		cell_list1[0].value=int(cell_list1[0].value)+1
		pointer=int(cell_list1[0].value)
		cell_list = sheet.range("A"+str(pointer)+':M'+str(pointer))
		#sheet.update_cell(pointer, 1 ,pointer)
		pv.insert(0,pointer)
		for i in range(len(cell_list)):
			cell_list[i].value=pv[i]
		cell_list.insert(0,cell_list1[0])
		sheet.update_cells(cell_list)
		#sheet.update_cell(pointer, i+2 ,pv[i])
		sheet.update_cell(1, 1 , pointer)
		print("\n")
	
		im1 = Image.new('RGBA',(215,215))
		fg = open("otherscrap.txt","r")
		fg1 = open("opscomp.txt","r")
		
		for i in fg:
			result21=i.split('=')
		ress=list(literal_eval(x) for x in result21)
		del result21
		
		for i in fg1:
			result21=i.split('=')
		rest=list(literal_eval(x) for x in result21)
		del result21
		
		fire=pv[1]+pv[2]
		marry=[list(map(int,format(ord(x.encode('latin1')), 'b').zfill(8))) for x in fire]
		#marry=[[int(x) for x in marry[i]] for i in range(len(marry))]
		b21d=pros(fire,marry)
		x=0
		y=0
		for i in range(0,len(b21d),4):
			#print(b2d[i],b2d[i+1],b2d[i+2])
			if y==215:
				y=0
				x+=1
			if x>=215:
				break
			im1.putpixel((x,y),(b21d[i],b21d[i+1],b21d[i+2],b21d[i+3]))
			y+=1
		im1.putpixel((x,y),(len(po),int(len(po)/4)+get(len(po)%4),0,0))
		y+=1
		
		fire1=po
		marry1=[list(map(int,format(ord(x.encode('latin1')), 'b').zfill(8))) for x in fire1]
		#marry1=[[int(x) for x in marry1[i]] for i in range(len(marry1))]
		b121d=pros(fire1,marry1)
		
		while len(b121d)%4 !=0:
			b121d.append(255)
		
		for i in range(0,len(b121d),4):
			#print(b2d[i],b2d[i+1],b2d[i+2])
			if y==215:
				y=0
				x+=1
			if x>=215:
				break
			im1.putpixel((x,y),(b121d[i],b121d[i+1],b121d[i+2],b121d[i+3]))
			y+=1
		
		while True:
			if y==215:
				y=0
				x+=1
			if x>=215:
				break
			if (x,y) in ress:
				pos=ress.index((x,y))
				im1.putpixel((x,y),rest[pos])
			else:
				im1.putpixel((x,y),(random.randint(0,256),random.randint(0,256),random.randint(0,256),random.randint(0,256)))
			y+=1
		im1.putpixel((214,214),(no,0,0,0))
		cprint(figlet_format('E n B i o C r y p t !'),'green',attrs=['bold'])
		im1.save(mo+".png")
		#print(emails)
		for x in range(len(emails)):
			msg = gmail.Message('EnbioCrypt - A New Level Encryption',to=emails[x],html="<center><img src='https://i.imgur.com/0evrOTf.jpg'/></center><br/><br/>Thanks For Using Our Service.<br/>The Encrypted File has been uploaded in our storage space , <b>The Generated EBC card Image Has been Attached with this mail.</b><br/><br/>Sender's Name: <b>"+kter+"<br/><br/></b>File Name: <b>"+mo+".png</b><br/><br/>Further OTP's will be sent at the time of verification to <b>Mobile Phone: +91xxxxxx"+mobiles[x][6:]+"</b><br/><br/><b>NOTE:</b>The Attached Image can be used to Fetch the data from cloud after providing successful Identity Verification , <b> Make Sure to have Decrypter</b>.<br/><br/>With Regards,<br/><b>CEO Of EnBioCrypt</b>",attachments=[mo+'.png'])
			gmtest.send(msg)
		
		print("\nFinal Image Generated.. Saved with name "+mo+".png")
		print("\nDone Encryption..\nSent EBC card to all provided recipient Mails")
		print("\nTotal Time For Encryption:%s seconds" % (time.time() - start_time))
		shro=input("\nWanna Share more file?(y/n): ")
		if shro=='n' or shro=='N':
			print("\n\t\t--Designed By: EnBioCrypt\n\t\t--Copyrights: Dinesh Surisetti\n")
			pause()
			break