import requests
import json
from string import Template
requests.urllib3.disable_warnings()

class AuthenticationError(Exception):
    pass
class Client:
    def __init__(self, host, usr, pwd):
        #self.jar = requests.cookies.RequestsCookieJar()
        self.host = host
        self.usr = usr
        self.pwd = pwd
        self.client = requests.Session() 
#Pushing the configuration in the APIC controller   
    def POST(self, url, data,Role):
        response= self.client.post('https://%s%s' % (self.host, url),data=json.dumps(data),timeout=5,verify=False)
        resp=response.text
        if 'error' in resp:
          print("\n!!!!{}: Config already exist or config issue..Code{}\n".format(Role,response))
          print("!!!!Error code:{}\n".format(resp))
          #raise AuthenticationError
        else:
          print(">>>>{}:>>>>>Done # Status Code>{}".format(Role,response))
        return response

#Login into APIC Controller using static Credentials.
    def login(self):
        data = {"aaaUser": {"attributes": {"name": self.usr, "pwd": self.pwd}}}
        res= self.client.post('https://%s/api/aaaLogin.json' % (self.host),data=json.dumps(data),timeout=5,verify=False)
        print(res)
        if res.status_code != 200 or 'error' in res.json()['imdata'][0]:
            raise AuthenticationError

    def VMM(self,Tname,APP,EPG,DOMAIN): 
        Role='T1:VMM change on :{},EPG:{}'.format(Tname,EPG) 
        print("\nConfiguring the EPG:{}\n".format(EPG))  
        data ={"fvRsDomAtt":{"attributes":{"primaryEncap":"","resImedcy":"pre-provision","tDn":"uni/vmmp-VMware/"+DOMAIN,"status":"modified"},"children":[]}}
        return self.POST('/api/node/mo/uni/tn-{}/ap-{}/epg-{}/rsdomAtt-[uni/vmmp-VMware/{}].json'.format(Tname,APP,EPG,DOMAIN), data,Role)
 
    def VMM_rollback(self,Tname,APP,EPG,DOMAIN): 
        Role='T1:VMM change on :{},EPG:{}'.format(Tname,EPG) 
        print("\nConfiguring the EPG:{}\n".format(EPG))  
        data ={"fvRsDomAtt":{"attributes":{"primaryEncap":"","resImedcy":"immediate","tDn":"uni/vmmp-VMware/"+DOMAIN,"status":"modified"},"children":[]}}
        return self.POST('/api/node/mo/uni/tn-{}/ap-{}/epg-{}/rsdomAtt-[uni/vmmp-VMware/{}].json'.format(Tname,APP,EPG,DOMAIN), data,Role)

def main():
    client.login()

if __name__ == '__main__':
    main()
