### Testing Under Windows

```dos
PS C:\Workspace\test-makefile-stutdino\src\lab01> echo 500 50 | node .\main.js

    Sampling Period : 50 sec
    ==============================
    gTime = 0,50,100,150,200,250,300,350,400,450,500
    gT1   = 30,112,121,158,124,29,101,4,80,1,1
    gT2   = 59,53,133,0,27,154,71,134,122,33,184
    gMemo = NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA

PS C:\Workspace\test-makefile-stutdino\src\lab01> echo 100 10 | node .\main.js

    Sampling Period : 10 sec
    ==============================
    gTime = 0,10,20,30,40,50,60,70,80,90,100
    gT1   = 190,159,23,53,118,163,188,122,184,19,34
    gT2   = 97,73,33,70,154,26,170,88,182,147,148
    gMemo = NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
````