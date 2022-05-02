from time import sleep
import sys, os
import subprocess
import re, random


def expected():
    dat = [random.randint(1,100) for i in range(10)]
    cdat = ",".join([str(s) for s in dat])
    sdat = " ".join([str(s) for s in dat])    
    s = f"sum({cdat}) = {sum(dat)}"
    return sdat , s


def cleanup(s):
    r = s.strip()
    r = [line.replace(' ', '') for line in r.split("\n")]
    return r


def failed(c, e):
    print(f"Your Output :\n{c}")
    print(f"Expected    :\n{e}")
    exit(1)


def test01(c, e):
    chk = cleanup(c)
    exp = cleanup(e)
    if chk[0] != exp[0]:
        failed(c, e)


def execMain(cmd):
    p = subprocess.Popen(["node",cmd],
                         shell=False,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE
                         )
    output, error = p.communicate()
    output = output.decode('utf-8')
    p.stdin.close()
    return output


def main():
    global expected
    # cwd = os.path.abspath(os.getcwd())
    test01(execMain('./src/lab03/main.js'), expected)
    print("測試通過!")
    exit(0)



if __name__ == "__main__":
    main()
