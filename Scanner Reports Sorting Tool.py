from pathlib import Path as path
from subprocess import run,Popen
from os import mkdir
from shutil import copy2 as cp

#Author: Matthew Daffern
#Requires: At least Python 3.6
#Please note the following:
#Python interprets \ as the unicode escape character, and Microsoft very "nicely" uses that for folder structure organization. You will need to enter in \\
#If any folders exist in the unsorted folder that match the item ID exactly, the script will fail because it cannot overwrite objects.
#I have some of the most confusing variale names in here, so I tried to comment what I could.





def filepathfixer(filepathinput):
	compliantfilepath=path(filepathinput)
	return compliantfilepath
#creates a Pathlib Path object




def mkdirfiletree(compliantfilepathinput,difflistbuilder):
    dirlist=list()
    for i in difflistbuilder:
            dirlist.append(str(compliantfilepathinput)+'\\'+i)
    return dirlist
#accepts a valid path object along with a list of different items to create a list of folder locations

    
def newfiletree(dirlistinput):
    for i in dirlistinput:
        mkdir(str(i))
    return dirlistinput
#makes a list of folder locations based on the input and returns that same set object


def filelistbuilder(filepathinput):
	generator=filepathinput.iterdir()
	return generator
#creates a generator for the Pathlib Path object passed to it
def filelist(generatorinput):
    finalfilelist=set()
    for i in generatorinput:
        if ".bak" in str(i):
            finalfilelist.add(i)
    return finalfilelist
#takes a generator and adds each yield to a set object. I was having trouble with the code working on a generator object because for whatever reason the generator would just simply disappear and leave the variable assigned to nothing.

def filecopier(fileset,dirlist,compliantfilepathinput):
        for iterfile in fileset:
                #goes over the set
                filenamedir=iterfile
                characterizingfeature=input("What are you looking for in the text file lines?")
                with open(iterfile,'r+')as file:
                        #passes the item to a list
                        trasharray=file.readlines()
                        for i in trasharray:
                                if characterizingfeature in i:
                                        trasharray=i.split('=')
                                        itemname=trasharray[1]
                                        break
                #specific code that fixes formatting to get the item name and directories to what we want. It's kind of spaghetti since I did incremental changes to the code to produce my result.
                filenamelist=str(filenamedir).split('\\') 
                filename=str(filenamelist[int(len(filenamelist)-1)])
                filenamedir=str(filenamedir)
                filenamedir=filenamedir.strip('\n')
                itemname=itemname.split('\\')
                itemname=itemname[1].strip('\n')
                destdir=str(str(compliantfilepathinput)+'\\'+itemname+'\\'+filename)
                destdir=destdir.strip('\n')
                cp(filenamedir,destdir)

def difflistbuilder(generatorinput):
        #creates a set of folder names and uses the set property of only having unique items to keep duplicates out and simplify the writing.
        difffileset=set()
        characterizingfeature=input("What are you looking for in the text file lines?")
        for file in generatorinput:
                with open(file,'r') as openfile:
                        lines=openfile.readlines()
                        itemname=str()
                        for i in lines:
                                if characterizingfeature in i:
                                        #get your foldername
                                        break					
        if len(difffileset)==1:
                listfileset=list(difffileset)
                returnstatement="all items are the same! \n \n \n item id for the files is "+str(listfileset[0])
                print(returnstatement)
                return returnstatement
        finaldifffileset=set()
        for i in difffileset:
                stringname=str(i)
                stringname=stringname.strip('\n')
                finaldifffileset.add(stringname)
        return finaldifffileset
		
def newdirectorylister(dirlist):
	print('Your new directory list is: \n')
	for i in dirlist:
		print(i)
		
def exitstatement():
	switch='on'
	while switch=='on':
		exit=input('\n press any key and enter to exit \n \n')
		switch=exit

def inputerrorcatching(pathfunction):
    #Wrapper that does error handling for the initial user interaction.
    initialpathvariable=input('Please write your full path variable for the directory that needs to be sorted in the following format:\nC:\\Users\\\qtechadmin\\\Documents\\\Offline Side Projects\\\TestFolder\n \n')
    switch='on'
    if '\\' not in initialpathvariable:
            while switch=='on':
                    print("error: you have entered the path incorrectly. \n \n")
                    initialpathvariable=input('Please write your full path variable for the directory that needs to be sorted in the following format:\nC:\\Users\\\qtechadmin\\\Documents\\\Offline Side Projects\\\TestFolder\n \n')
                    if '\\' in initialpathvariable:
                            switch='off'

    resultingpath=pathfunction(initialpathvariable)
    return resultingpath

#the main function that ties it all together
def mainfunc():
    finalpath=inputerrorcatching(filepathfixer)
    finalfilelist=filelist(filelistbuilder(finalpath))
    difflist=difflistbuilder(finalfilelist)
    directory=mkdirfiletree(finalpath,difflist)
    newfiletree(directory)
    filecopier(finalfilelist,directory,finalpath)
    newdirectorylister(directory)
    exitstatement()
    
mainfunc()


