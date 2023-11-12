#!/usr/bin/python

# -*- coding: utf-8 -*-

ZMMBOX="/opt/mail/bin/zmmailbox"
BFOLDER="company.test"

import sys,os   
import pdb


if len(sys.argv)>1 :
    os.path.realpath
    if sys.argv[1][-1]=='/':
        basedir=sys.argv[1]
    else:
        basedir=sys.argv[1]+'/'
    if os.path.exists(basedir):    
        n = raw_input("WARNING: Program will remove all empty files and everything except *.msg files from the directory !"+"\nDo you agree? (y / n)")
        if n=='y' or n=='Y':
            findempty=os.popen('find '+basedir+' -size 0').readlines()  
            for fi in findempty:
                print 'Removeing :'+fi.replace('\n','')
                os.remove(fi.replace('\n',''))
            findmrk=os.popen('find '+basedir+' -type f ! -name *.msg').readlines()
            for fi in findmrk:
                print 'Removeing :'+fi.replace('\n','')
                os.remove(fi.replace('\n',''))            
            for PATH, dirs, files in os.walk(basedir):            
                if PATH!=basedir:
		    mydomain=(basedir.replace("/", ""))
                    DOMAIN=(mydomain)
                    USER=PATH.replace('/','-').split('-')[1]
                    DIR=PATH.replace(DOMAIN+'/'+USER+'/','')
                    if DIR == PATH: DIR='';
                    if USER!='':
                        k=0
                        print '==============================='
                        print 'PATH = '+PATH
                        print "Search and modify imap files.." 
                        for f in files:                                               
                            fileExt=os.path.splitext(f)[1]
                            if fileExt=='':
                                fhash=f.replace(fileExt,'')[-8:]
                                fr=open(PATH+'/'+f,'r')
                                tmp=fr.readline()
                                tmp=tmp.replace('\n','').replace('\r','')
                                if tmp[:1]=='0' and tmp[-8:]==fhash:
                                    content=fr.read()      
                                    fw=open(PATH+'/'+f,'w+')
                                    fw.write(content)
                                    fw.close()
                                    k+=1
                                fr.close()
			DIR=(content.replace(".IMAP", ""))
                        print "Modify : "+str(k)+" files"
                        print '-------------------------'
                        print 'Start import emails'                    
                        print 'DOMAIN = '+DOMAIN
                        print 'USER = '+USER
                        print 'DIR = '+DIR
                        createcmd=ZMMBOX+' -z -m '+USER+'@'+DOMAIN+' createFolder "/'+DIR+'"' 
                        if DIR!='':
                            addmailcmd=ZMMBOX+' -z -m '+USER+'@'+DOMAIN+' addMessage "/'+DIR+'/" "'+PATH+'"'
                        else:
                            addmailcmd=ZMMBOX+' -z -m '+USER+'@'+DOMAIN+' addMessage "/'+DIR+'/" "'+PATH+'"'
                        os.system(createcmd)
                        os.system(addmailcmd)
    else:
        print "Path not exist"
        
else:
    print "Example: migrate.py path_to_dir_with_domains"
