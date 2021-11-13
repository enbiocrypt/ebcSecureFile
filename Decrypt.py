import time , shutil , subprocess , zlib , base64 , hashlib , dropbox , io , gspread , pprint , sys , random , math , tempfile , way2sms
from PIL import Image
from tqdm import tqdm
from termcolor import cprint
from pyfiglet import figlet_format
from oauth2client.service_account import ServiceAccountCredentials

dicto={"type": "service_account","project_id": "","private_key_id": "","private_key": "","client_email": "ebccard@.iam.gserviceaccount.com","client_id": "","auth_uri": "https://accounts.google.com/o/oauth2/auth","token_uri": "https://accounts.google.com/o/oauth2/token","auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/ebccard%40enbiocrypt-26c92.iam.gserviceaccount.com"}

dbx = dropbox.Dropbox("")

scope=['https://spreadsheets.google.com/feeds']
creds=ServiceAccountCredentials.from_json_keyfile_dict(dicto,scope)

z11=[27, 59, 236, 32, 242, 222, 162, 227, 45, 116, 56, 241, 33, 147, 121, 71, 158, 126, 68, 143, 85, 209, 81, 232, 144, 104, 204, 88, 250, 84, 243, 40, 224, 103, 44, 39, 167, 195, 221, 117, 92, 41, 52, 28, 50, 77, 15, 12, 172, 200, 219, 238, 169, 194, 154, 190, 38, 197, 160, 111, 65, 49, 187, 131, 231, 175, 21, 91, 191, 53, 235, 159, 120, 5, 164, 254, 8, 142, 19, 223, 30, 4, 109, 42, 36, 20, 14, 150, 29, 125, 62, 173, 16, 87, 55, 46, 80, 202, 171, 186, 1, 253, 151, 82, 210, 128, 119, 35, 249, 205, 229, 193, 146, 64, 178, 211, 75, 244, 170, 17, 247, 72, 181, 141, 215, 137, 124, 99, 188, 54, 97, 0, 102, 118, 106, 225, 86, 245, 60, 94, 155, 127, 107, 58, 76, 148, 214, 100, 7, 233, 66, 163, 89, 168, 115, 90, 139, 138, 184, 11, 208, 95, 152, 206, 122, 47, 196, 26, 239, 166, 43, 93, 177, 34, 165, 182, 79, 31, 129, 240, 98, 201, 96, 3, 23, 180, 161, 9, 114, 78, 67, 136, 10, 198, 2, 185, 212, 108, 179, 207, 157, 112, 199, 153, 251, 255, 110, 24, 105, 140, 217, 130, 37, 123, 113, 73, 48, 134, 220, 213, 218, 145, 57, 18, 6, 133, 226, 74, 216, 230, 237, 176, 156, 51, 248, 132, 174, 25, 203, 252, 63, 149, 228, 192, 13, 246, 234, 101, 70, 61, 189, 22, 83, 183, 135, 69]

m11=[bytes([x]).decode('latin1') for x in z11]
asciicr={}


#w2s=way2sms.sms("","Q3236D")
w2s=way2sms.sms("","")
#dirpath = tempfile.mkdtemp()

def asciifet(simage):
	client = gspread.authorize(creds)
	sheet=client.open('EnBioCrypt-ASCII').sheet1
	sheet.update_cell(1, 2, '=QUERY(A2:B431533,"select A where B='+"'"+simage+"'"+'")')
	val = sheet.cell(1, 2).value
	values_list11 = sheet.row_values(int(val))
	while True:
		try:
			values_list11.remove('')
		except:
			break
	return [int(x) for x in values_list11[2:]]

def pause():
    programPause = input("Press the <ENTER> key to continue...")

def exfun(x):
	return 255-abs((x%509)-255)	

def moveri(pn):
	pol=1
	mn=random.randint(10000000,99999999)
	#w2s.send(str(pn),"\nAuthrization  C o d e  is "+str(mn)+"\n\nMade With Love From EnBioCrypt." )
	w2s.send(str(pn),"code:"+str(mn))
	while pol<=5:
		try:
			if pol==1:
				kl=int(input("\nEnter The OTP code sent over Mobile(+91XXXXXX"+str(pn)[6:]+"): "))
			else:
				kl=int(input())
			if kl==mn:
				print("\nSuccessfully Verified Phone Number..\n")
				break
			print("\nWrong OTP code,Re-Enter: ",end="")
			pol+=1
		except:
			print("\nWrong OTP code,Re-Enter: ",end="")
			pol+=1
	if pol>5:
		print("\nToo Many Wrong Attempts...")
		sys.exit()
	
def conv(p,q):
	for i in range(len(p)):
		n=ord(p[i].encode('latin1'))
        #print(n)
		q.append(n)
	return q

    #return(q)
#Negation And Encrypt Program:
def rev(p1,q1):
	for i in range(len(p1)):
		for j in range(8):
			if not q1[i][j]==0:
				q1[i][j]=0
			else:
				q1[i][j]=1
	return q1

#return(q1)
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
cprint(figlet_format('E n B i o C r y p t !'),'green',attrs=['bold'])
mo=str(input("\nEnter The EBC Card File Name(Exclude .PNG): "))
#po=str(input("\nEnter The Extension Type of File Output: "))
dem=str(input("\nEnter The Email on which you received this EBC Card: "))
usr=input("\nWanna Decrypt Offline(y/n),[Make sure you have encrypted data offline]: ")
im=Image.open(mo+".png")
b21d=[]
b121d=[]
print("\n\nPlease Wait While we Verify Your Details and Scan the Image..")
x=0
y=0
for i in range(0,64,4):
	#print(b2d[i],b2d[i+1],b2d[i+2])
	if y==215:
		y=0
		x+=1
	if x>=215:
		break
	b21d+=list(im.getpixel((x,y)))
	y+=1
	
lenext,lencount,temp1,temp2=im.getpixel((x,y))
y+=1

for i in range(lencount):
	#print(b2d[i],b2d[i+1],b2d[i+2])
	if y==215:
		y=0
		x+=1
	if x>=215:
		break
	b121d+=list(im.getpixel((x,y)))
	y+=1
	
while len(b121d)!=lenext:
	b121d.pop()

ext=''.join(bytes([i]).decode('latin1') for i in b121d)
simage=''.join(bytes([i]).decode('latin1') for i in b21d[:32])
sverif=''.join(bytes([i]).decode('latin1') for i in b21d[32:64])
no=im.getpixel((214,214))[0]

client = gspread.authorize(creds)
sheet=client.open('EnBioCrypt').sheet1
sheet.update_cell(1, 3, '=QUERY(A2:C431533,"select B where B='+"'"+simage+"'"+' AND C='+"'"+sverif+"'"+'")')

if sheet.cell(1, 3).value != simage:
	sys.exit()
	
sheet.update_cell(1, 2, '=QUERY(A2:C431533,"select A where B='+"'"+simage+"'"+' AND C='+"'"+sverif+"'"+'")')
val = sheet.cell(1, 2).value
values_list = sheet.row_values(int(val))

client = gspread.authorize(creds)
sheet=client.open('EnBioCrypt-Resip').sheet1
sheet.update_cell(1, 2, '=QUERY(A2:D431533,"select D where B='+"'"+simage+"'"+' and C='+"'"+dem+"'"+'")')

try:
	mobval = int(sheet.cell(1, 2).value)
except:
	print("\nNo Such Email Registered,Please Try Again..")
	sys.exit()
	
moveri(mobval)
r11=asciifet(simage)
asciicr.update(zip(r11,m11))

#print(asciicr)
#pause()

start_time = time.time()
while True:
	try:
		values_list.remove('')
	except:
		break

values_list=values_list[3:]
values_list.reverse()
gonee="Dinesh"
cprint(figlet_format('E n B i o C r y p t !'),'green',attrs=['bold'])
print("\n\nDecrypting The Files, Please Wait..\n")
f3=open("DecryptDumps/"+mo+"."+ext,"wb")
for i in tqdm(range(no)):
	if gonee=="case":
		break
	if usr=="n":
		metadata,res=dbx.files_download("/EnBioCrypt/Dumps/"+simage+".png")
		im2=Image.open(io.BytesIO(res.content))
	else:
		im2=Image.open(tempfile.gettempdir()+"\\Dumps\\"+simage+".png")
	#im2 = Image.open(mo+'.png')
	
	width , height = im2.size
	
	sizf,sizl,lens,lenr=im2.getpixel((0,0))
	sizer=""
	
	while sizf<=sizl:
		sizer+=''.join(str(i) for i in list(im2.getpixel((0,sizf))))
		sizf+=1
	sizer=int(sizer[:lens])
	l=values_list.pop()[1:-1]
	#q12=[[0 for i in range(8)] for j in range(len(l))]
	b2d=[]
	q12=[]
	q12=conv(l,q12)
	x=1
	y=0
	
	#print(b2d,len(b2d))
	#while len(b2d)%3 !=0:
	#	b2d.append(0)
	
	tem=[]
	nxtf=[]
	gone=""
	while True:
		#print(b2d[i],b2d[i+1],b2d[i+2])
		if y==width:
			y=0
			x+=1
		if x>=height:
			break
		for i in im2.getpixel((x,y)):
			if len(tem)==int(sizer):
				gone="case"
				break
			tem.append(255-i)
		if gone:
			break
		y+=1
	
	finstr2=hashlib.md5(l.encode('latin1')).hexdigest()
	z=0
	h=0
	k=0	
	for i in range(len(tem)):
		if z>=32:
			z=0
			finstr2=hashlib.md5(finstr2.encode('latin1')).hexdigest()
			h+=1
		if h>=32:
			h=0
		
		numbers1="{0:b}".format(exfun(sum(bytearray(hashlib.md5(finstr2[z].encode('latin1')).hexdigest(),'latin1'))))
		#numbers1=[int(x) for x in numbers1]
		
		if k>=len(q12):
			k=0
		
		b2d.append((tem[i]^q12[k]) ^ int(numbers1,2))
		
		z+=1
		k+=1

	if im2.getpixel((int(math.sqrt(sizer/4))+1,int(math.sqrt(sizer/4))+1))==(1,1,1,1):
		opl=''.join(asciicr[i] for i in b2d)
		f3.write(base64.decodestring(str.encode(opl)))
		gonee="case"
	else:
		opl=''.join(asciicr[i] for i in b2d[:-32])
		f3.write(base64.decodestring(str.encode(opl)))
		simage=''.join(asciicr[i] for i in b2d[int(sizer)-32:])
	#print(simage,len(simage))
	#pause()
f3.close()
print("\n\n")
cprint(figlet_format('E n B i o C r y p t !'),'green',attrs=['bold'])
print("\nDone, saved on file:"+mo+"."+ext)
print("\nTotal Time For Decryption:%s seconds" % (time.time() - start_time))
print("\n\t\t--Designed By: EnBioCrypt\n\t\t--Copyrights: Dinesh Surisetti\n")
pause()