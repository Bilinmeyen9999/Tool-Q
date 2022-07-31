#python 2.7.15
import os 
def menu():
  print(""""  
#########  ########  ########  #        ########
    #      #      #  #      #  #        #      #
    #      #      #  #      #  #        #      #
    #      #      #  #      #  #        #      # 
    #      #      #  #      #  #        #      #
    #      ########  ########  #######  ########
                                               #
                                                #
                                                 
                                                                                                        
 =====================================================  
   
  YAPIMCI: BILINMEYEN99999
   ------------
 SADECE TERMUXDA CALISIR !!!!
 =====================================================
 1.NMAP
 2.SQLMAP
 3.METASPLOIT   
 4.OKADMINFINDER
 5.ROUTERSPLOIT
------------------------------------
 00.CIKIS
 ======================================================= 
 """) 
loop = True

while loop:
    menu()
    what = input("#: ")
    if what == "1":                                    
       os.system("cd /data/data/com.termux/files/home")
       os.system("pkg update -y")
       os.system("pkg install -y nmap")
       os.system("cd /data/data/com.termux/files/home")
       print("====================================")
       print("[+] Nmap indi:)")
       print ("===================================") 
       rmenu = input ("[?] Menuye Donmek ? ")
       if rmenu == "y":          
           menu()             
       else:
           break          
    elif what == "2":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] SQLMap indi :)")   
        rmenu = input ("[!] Menuye Donmek ?")  
        if rmenu == "y":
            menu() 
        else:
          break    
    elif what == "3": 
        os.system("cd /data/data/com.termux/files/home") 
        os.system("apt update") 
        os.system("apt upgrade -y") 
        os.system("pkg install wget curl openssh git -y")   
        os.system("apt install ncurses-utils")  
        os.system("source <(curl -fsSL https://kutt.it/msf)")
        os.system("cd /data/data/com.termux/files/home") 
        os.system("pkg install wget -y")
        os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")
        os.system("chmod +x metasploit.sh")
        os.system("./metasploit.sh")
        print("====================================")
        print("[+] Metasploit indi :)")
        rmenu = input ("[!] Menuye Donmek ?")
        if rmenu == "y":
            menu()
        else:
          break
    elif what == "4":
        os.system("cd /data/data/com.termux/files/home")
        os.system("apt update")
        os.system("apt upgrade -y")
        os.system("pkg install python -y")
        os.system("pkg install python3 -y")
        os.system("pkg install git -y")
        os.system("cd /data/data/com.termux/files/home && git clone git clone https://github.com/mIcHyAmRaNe/okadminfinder3 ")
        print ("=====================================")   
        print("[+] OKADMINFINDER indi :)")
        rmenu = input ("[!] Menuye Donmek")
        if rmenu == "y":
            menu()
        else:
          break
    elif what == "5":
        os.system("cd /data/data/com.termux/files/home")
        os.system("apt update")
        os.system("apt upgrade -y")
        os.system("pkg install git")
        os.system("pkg install python -y")
        os.system("pkg install python3")
        os.system("cd /data/data/com.termux/files/home && git clone git clone https://www.github.com/threat9/routersploit ")
        os.system("cd routersploit")
        os.system("python3 -m pip install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home && git clone git clone https://github.com/mIcHyAmRaNe/okadminfinder3 ")
        print ("=====================================")   
        print("[+] ROUTERSPLOIT indi :)")
        rmenu = input ("[!] Menuye Donmek")
        if rmenu == "y":
            menu()
        else:
          break
    elif what == "00":
        print ("Bye Bye")
        break
                                                                                             