### Testing Under Windows

```dos
PS C:\Workspace\test-makefile-stutdino\src\lab02> type .\data1.txt
1 2 3 4 5
6 7 8 9 10
1 2 3 4 5
6 7 8 9 10

PS C:\Workspace\test-makefile-stutdino\src\lab02> type .\data1.txt | node .\main.js
sum(1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10) = 110

PS C:\Workspace\test-makefile-stutdino\src\lab02> echo 1 2 3 4 5 | node .\main.js
sum(1,2,3,4,5) = 15
````