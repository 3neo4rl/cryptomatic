#! /usr/bin/python3

import stand, sys, os

# - Informations for the Bug reporter
version = 1
prg = "cryptomatik"
email = ""
# - Informations for the Bug reporter
print("Welcome to the cryptogapic program from")
while 1 == 1:
    do = input("Decrypt(d) or encrypt(e)")
    pas = input("Passwort? ")
    if do == "e":
        crypt = input("Please insert the text you want to encrypt. ")
        data = input("Please insert the name of the data to safe")
        pa = 0
        pal = len(pas) - 1
        count = 0
        ret = " "
        while count <= len(crypt) -1:
            pa += 1
            if pa > pal:
                pa = 1
            pas_ = pas[pa]
            num = ord(pas_)
            ret += chr(ord(crypt[count]) + num)
            count += 1
        print (ret)
        a = open(data, "w")
        a.write(ret)
        a.close()
    if do == "d":
        data = input("Please insert the name of the encrypted data. ")
        if not os.access(data, os.R_OK):
            print ("Access to the Data " +data+ " denied.")
        else:
            a = open(data)
            crypt = a.read()
            pa = 0
            pal = len(pas) - 1
            count = 0
            en = " "
            while count <= len(crypt) - 1:
                pa += 1
                if pa > pal:
                  pa = 1
                if count == 0:
                    count = 1
                pas_ = pas[pa]
                num = ord(pas_)
                e = crypt[count]
                en += chr(ord(e) - num)
                count += 1
            print(en)
    if do == "bug":
        stand.bug(version, prg, email)
