import os, subprocess, shutil




xDirName = ""
xBasePath = ""
xFilePath = ""



def main():
    global xDirName
    global xBasePath


    xDirName = "zmyDir"
    xBasePath = "C:/z/"

    makeDirectory()

def makeDirectory():
    global xDirName
    global xBasePath
    global xFilePath 

    xPath = os.path.join(xBasePath, xDirName)
    print(xPath)

    
    subprocess.Popen(r'explorer /select, "'+xPath+'"')



main()
