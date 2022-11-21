import json
import datetime

x = datetime.datetime.now()
d = x.strftime("%d")
m = x.strftime("%m")
y = x.strftime("%Y")

#with open('presets/assembly.json') as f:
#    assemblyJSON = json.load(f)

def createAutoFill(codeDict):
    fileAuthor = "{} Author: {}\n".format(codeDict['Comments'],codeDict['Author'])
    if codeDict['mdy'] == True:
        fileDate = "{} Date: {}\n\n".format(codeDict['Comments'],x.strftime('%x'))
    else:
        fileDate = "{} Date: {}/{}/{}\n\n".format(codeDict['Comments'],d,m,y)

    if codeDict['Purpose'] == True:
        filePurpose = "{} Purpose:\n{}\n\n".format(codeDict['Comments'],codeDict['Comments'])
    else:
        filePurpose = ""
    
    if codeDict['Input'] == True:
        fileInput = "{} Input:\n{}\n\n".format(codeDict['Comments'],codeDict['Comments'])
    else:
        fileInput = ""

    if codeDict['Output'] == True:
        fileOutput = "{} Output:\n{}\n\n".format(codeDict['Comments'],codeDict['Comments'])
    else:
        fileOutput = ""

    if codeDict['Extra']:
        fileExtra = codeDict['Extra']
    else:
        fileExtra = ""

    return f"{fileAuthor}{fileDate}{filePurpose}{fileInput}{fileOutput}{fileExtra}"
    