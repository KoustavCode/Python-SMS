
import urllib, urllib2, cookielib, sys
from getpass import getpass
# Extracting the cookies
def cook(cj):
        j=str(cj)
        t2=j.find(' for ')
        t1=int(j.find('~'))+1
        tokken=str(j[t1:t2])
        return tokken   


def main():
        print '''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
ooooooo  ooooo                                 oooo    oooo                                    .                        
 `8888    d8'                                 `888   .8P'                                   .o8                        
   Y888..8P     .ooooo.  oooo d8b              888  d8'     .ooooo.  oooo  oooo   .oooo.o .o888oo  .oooo.   oooo    ooo
    `8888'     d88' `88b `888""8P              88888[      d88' `88b `888  `888  d88(  "8   888   `P  )88b   `88.  .8' 
   .8PY888.    888   888  888                  888`88b.    888   888  888   888  `"Y88b.    888    .oP"888    `88..8'  
  d8'  `888b   888   888  888                  888  `88b.  888   888  888   888  o.  )88b   888 . d8(  888     `888'   
o888o  o88888o `Y8bod8P' d888b    ooooooooooo o888o  o888o `Y8bod8P'  `V88V"V8P' 8""888P'   "888" `Y888""8o     `8'    
                                                                                                                       
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
        number=int(raw_input(' [+] Please Enter Your Username : '))
        password=raw_input(' Enter your password: ')
       
        # Login 
          
        url='http://site24.way2sms.com/Login1.action'
        data={'username':str(number),'password':str(password)}
        data=urllib.urlencode(data)

        cj=cookielib.CookieJar()
        header={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0'}
        req=urllib2.Request(url, data, headers=header)
        opennr=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), urllib2.HTTPRedirectHandler())
        print ' Please Wait. Trying To Login In '
        req=opennr.open(req)
        sucess=str(req.info())
        sucess=sucess.find('Set-Cookie')
        if (sucess==-1):
                print '\n',' Login Successful '
                pass
        else:
                print '\n',' Login Failed '
                raw_input('')
                sys.exit(0)

        #  Tokken Receiving Mechanism
        tokken=cook(cj)
        print '\n [+] Tokken Received : ', tokken
        
        # Sms Sending System Configuration 
        url='http://site24.way2sms.com/smstoss.action'
        head={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0','Refere':str('http://site24.way2sms.com/sendSMS?Token='+tokken)}
        mobile=[7980364863,7001590037]                              ##int(raw_input(' [*] Please Enter Mobile Number For Sending SMS : '))
        #================   Checking Mechanizam =====================================
     ##   if len(str(mobile))==10:
     ##           pass
       ## else:
         ##       print " [*] Invalid Username"
           ##     sys.exit(0)

           # Text multiple numbers
        while True:
                message_raw=str(raw_input('  Please Enter Message For Sending. Note ! Not More Then 140 Words: '))
                message=message_raw.replace(' ', '+')
                msglen=140-len(message)
                if len(message)<140:
                        break
                else:
                        pass
        for i in mobile:
        	data='ssaction=ss&Token='+tokken+'&mobile='+str(i)+'&message='+str(message)+'&msgLen='+str(msglen)
        	req=urllib2.Request(url, data=data, headers=head)
        	print ' Sending SMS .... '
        	req=opennr.open(req)

        print '\n',' SMS Sent '
        raw_input('\n\n')


if __name__=='__main__':
        main()