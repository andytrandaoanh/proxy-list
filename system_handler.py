import os, sys
from datetime import datetime

def openDir(targetdir):
	#open directory when done	
	rpath = os.path.realpath(targetdir)
	os.startfile(rpath)


def getDatedFilePath(initialString, dirOut):
	now = datetime.now()
	dateTime = now.strftime("%Y%m%d_%H%M")
	fileName = initialString + dateTime + ".txt"
	pathOut =  os.path.join(dirOut, fileName ) 
	return(pathOut)

def getDateStamp():
	getDateStamp = str(datetime.now())
	return(getDateStamp)

	

	
	
def readTextFile(filepath):
	try:
	    ofile = open(filepath, 'r', encoding = 'utf-8') 
	    data = ofile.read()
	    return data
	except FileNotFoundError:
	    print("file not found")    
	except Exception as e:
	    print(e)  



def writeListToFile(vlist, vpath):
    with open(vpath, 'w', encoding ='utf-8') as file:
        for item in vlist:    
            file.write(item + "\n")


def fileToLine(filepath):
    try:
        ofile = open(filepath, 'r', encoding = 'utf-8') 
        data = ofile.read()
        lines = data.split('\n')
        return lines
    except FileNotFoundError:
        print("file not found")    
    except Exception as e:
        print(e)   


def loadProxyLines(dirProxy):
	files = os.listdir(dirProxy)
	lines = []
	for fp in files:
		lines  += fileToLine(os.path.join(dirProxy, fp))
	temps = list(dict.fromkeys(lines))	
	outData = [item for item in temps if item]
	return sorted(outData)