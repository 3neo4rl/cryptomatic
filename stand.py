def syn_err():
    print("Your selectet input has risen an error. Pleas only input that what the program tould you.")
def end():
    input()
    #Funktion for Windows, put on the end of the program and the Windows Command Line Interpreter of python can run it
def any_err():
    print ("An unexpectet error happend. Please send a bug report to the coders of this program,")
def bug(version, prg, email):
    bug_v = 1
    print ("Bug reporter v1.0")
    a = input ("What is your problem? ")
    ret = open("bug.br", "w")
    print("In your programfile is a 'bug.br' data, please send this data to the E-Mail " + email + ". Thank you :)")
def version():
    print ("STANDART PROGRAMM LIBARY FOR BUGS AND ERRORS")
    print ("VERSION: 0.01")
