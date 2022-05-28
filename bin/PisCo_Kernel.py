import sys
import os

def rc(cmd):
    lst = cmd.split()
    cs = 1
    txt=""
    for i in range(len(lst)):
        if cs == 0:
            txt =txt + lst[i] + ' '*2
        else:
            cs = 0
        txt = txt[0:-1]
    if lst[0] == "output":
        print(txt)
    elif lst[0] == "print":
        print(txt,end="")
    elif lst[0] == "quit":
        quit()
    elif lst[0] == "eval":
        rc(txt)
    elif lst[0] == "eval":
        os.system(txt)
    else:
        print("Error!")
        print("Code:'" + cmd + "' Not a Command")
        print("Command Error:Command '" + lst[0] + "' Not a Command.")

mlh = ""
csr=1
vj = len(sys.argv)
for i in range(vj):
    if csr == 0:
        mlh =  mlh + sys.argv[i] + ' '*2
        mlh = mlh[0:-1]
    else:
        csr=0

rc(mlh)
