import autofill
import determineanswer

fileExtension = input('File extension (.c, .py, .js):')             # File extension (for saving)
fileName = input("File name:")
authorInput = input('Author:')                                      # Author's name
dateMDY = input('Format date mm/dd/yyyy?:')                         # Display date as m/d/y or d/m/y
commentOption = input('Comment Format (;, #, //):')                 # How comments are typed in language
includePurpose = input('Include purpose field?:')                   # Include purpose field in comments
includeInput = input('Include input field?:')                       # Include input field in comments
includeOutput = input('Include output field?:')                     # Include output field in comments
extraOption = input(r'Extra content (use \n, \t, etc.):')           # Include extra code at end of file
languageDict = {                                                    # Dictionary to convert back to JSON
    "Author": "",
    "mdy": False,
    "Comments": "",
    "Purpose": True,
    "Input": False,
    "Output": False,
    "Extra": ""
}

languageDict["Author"] = authorInput                                            # Sets author in dictionary to user input
languageDict["Comments"] = commentOption                                        # Sets comment in dictionary to user input
languageDict["Extra"] = extraOption                                             # Sets extra content in dictionary to user input
languageDict["mdy"] = determineanswer.determineBool(dateMDY)                    # Sets mdy bool to user input
languageDict['Purpose'] = determineanswer.determineBool(includePurpose)         # Sets purpose bool to user input
languageDict['Input'] = determineanswer.determineBool(includeInput)             # Sets input bool to user input
languageDict['Output'] = determineanswer.determineBool(includeOutput)           # Sets input bool to user input

finalisedFile = open(f'results/{fileName}{fileExtension}', "wt")
try:
    finalisedFile.write(autofill.createAutoFill(languageDict))
except:
    print("Something went wrong writing the file D:")
else:
    print("\nFile successfully created! Check results folder.")
finalisedFile.close()