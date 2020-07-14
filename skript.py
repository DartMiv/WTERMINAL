import os, glob, configparser, shutil, winshell
import win32com.client 
import pythoncom
import signal
import time



def Win(windowsPyt, PCadd):

    PCadd = PCadd
    print(PCadd)
    
    try:
       
        os.chdir(windowsPyt)
    except Exception:
       pass
    else:
        pass
    opsin = True
    for failini in glob.glob(".ini"):
        print(failini)
        failss = '.ini'
        if failini == failss:
            conf = configparser.ConfigParser()
            print (conf.read('.ini'))
            try:
                print(conf.get(" "))
                conf.set(" ")
                conf.set(" ")
            
                with open('.ini', 'w') as configfile:
                    conf.write(configfile)
                
            except BaseException:
                conf = configparser.ConfigParser()
                conf.read('.ini')
                conf.add_section(" ")
                conf.set(" ")
                conf.set(" ")
                conf.set(" ")
                with open('.ini', 'w') as configfile:
                    conf.write(configfile)
            Perenos(PCadd, opsin)
        else:
            opsin = False
            print(opsin)

        return(1)
    return(0)
             

def Perenos(PCadd, opsin):

    PCadd = PCadd

    userPyt = '/C$/Users'
    userPytXp = '\C$\Documents and Settings'
    userPyt = PCadd + userPyt
    userPytXp = PCadd + userPytXp
    try:

        u = os.getcwd()
        print(u)   
        os.chdir (userPytXp)
        userdir = os.listdir()
        u = os.getcwd()		
        print(u)
        print(userdir)

        for userDec in userdir:
            try:
                    os.chdir(userDec)
                    os.chdir(r'Рабочий стол')
					
  
                    for failexe in glob.glob("*.lnk"):
                        print(failexe)
                        shell = win32com.client.Dispatch("WScript.Shell")
                        old_program_path_RegDoc = r" "
                        old_program_path_StatDoc = r" "
                        old_program_path_FinDoc = r" "
   	                
                        shortcu = shell.CreateShortCut(failexe)
                        target = shortcu.Targetpath
                        if target == old_program_path_RegDoc:
                            shortcu.Targetpath = r'" "'
                            shortcu.save()
                        elif target == old_program_path_StatDoc:
                            shortcu.Targetpath = r'" "'
                            shortcu.save()
                        elif target == old_program_path_FinDoc:
                            shortcu.Targetpath = r'" "'
                            shortcu.save() 
            except OSError:
                userDec2 = os.getcwd()
                print(userDec2)
                os.chdir(userPytXp)
                continue
            userDec2 = os.getcwd()
            print(userDec2)
            os.chdir(userPytXp)
                    
    except OSError:
        u = os.getcwd()
        print(u)   
        os.chdir (userPyt)
        userdir = os.listdir()
        u = os.getcwd()		
        print(u)
        print(userdir)
        for userDec in userdir:
              
            try:
                    os.chdir(userDec)
                    os.chdir('Desktop')
                    
                    for failexe in glob.glob("*.lnk"):
                        print(failexe)
                    
                        shell = win32com.client.Dispatch("WScript.Shell")
                        old_program_path_RegDoc = r" "
                        old_program_path_StatDoc = r" "
                        old_program_path_FinDoc = r" "
                    
                        shortcu = shell.CreateShortCut(failexe)
                        target = shortcu.Targetpath
                        if target == old_program_path_RegDoc:
                            shortcu.Targetpath = r'" "'
                            shortcu.save()
                        elif target == old_program_path_StatDoc:
                            shortcu.Targetpath = r'" "'
                            shortcu.save()
                        elif target == old_program_path_FinDoc:
                            shortcu.Targetpath = r'" "'
                            shortcu.save()
        
        
        			
            except OSError:
                
            
                userDec2 = os.getcwd()
                print(userDec2)
                os.chdir(userPyt)
                continue
            userDec2 = os.getcwd()
            print(userDec2)
            os.chdir(userPyt)				

			
t = True			
l = []
i = 1
while i > 0:
    
    with open ('C:\BAT\host.txt', "r") as f:

        l = f.read().split()
		
    i = int(len(l))
    print(type(i))
    print(i)
    
    print(l)
    for PCadd in l:
        print(PCadd)
        windowsPyt = '\C$\windows'

        

        windowsPyt = PCadd + windowsPyt
        Tr = Win(windowsPyt, PCadd)
        print(Tr)

        if Tr == 1:
            with open('C:\BAT\host.txt', "r") as f:
                lines = f.read().split()
                print(type(lines))
                print(lines)
                print(type(PCadd))
                lines.remove(PCadd)
                with open('C:\BAT\host.txt', "w") as new_f:
                    for line in lines:        
                        new_f.write(line + "\n")
                        
            
            
            
             
           
            

