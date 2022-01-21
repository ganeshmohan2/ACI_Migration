def main():
    import epginput as data
    from MasterVMM import Client
    host = "172.28.239.5"
    usr = "apic#fallback\\admin"
    pwd = "J21@:fwD"
    i = input("Enter the no.of EPG's you want to Change:")
    for x in range(int(i)):
     try:
       Tenant = str((data.epg_list[x]["Tenant"]))
       APP = str((data.epg_list[x]["APP"]))
       EPG = str((data.epg_list[x]["EPG"]))
       DOMAIN = str((data.epg_list[x]["Domain"]))
       print ("")
       print(Tenant)
       print("Logging into APIC Controller:{}".format(host))
       #print("Configure the Tenant :{}".format(Tenant))
       #print("Configure the EPG :{}".format(EPG))
       #print("Configure the APP :{}".format(APP))
       #print("Configure the VMMDomain :{}".format(DOMAIN))
       
       ACTION = input("Are you sure you want to push the configuration (y/n): ")
       if ACTION in ("y","yes","Y","YES"): 
         FABRIC=Client(host, usr, pwd)
         print("Calling the Master function -> Authenticating into the Controller")
         FABRIC.login()
         print("Authentication success")
         FABRIC.VMM(Tenant, APP, EPG, DOMAIN)
       elif ACTION in ("n","no","N","No"):
         print("Ending the script")
       else: 
        print("Please enter yes or no.")
     except IndexError:
       print("Oops!  Out of the vlan migration range.  please check and Try again...")

if __name__ == '__main__':
  main()