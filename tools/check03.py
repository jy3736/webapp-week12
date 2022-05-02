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
    print("測試通過!")
    print(f"\n{c}")
    exit(0)


def execMain(dat):
    dat = dat.encode('utf-8')
    p = subprocess.Popen('node .\main.js',
                         shell=False,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE
                         )
    p.stdin.write(dat)
    p.stdin.close()
    output, error = p.communicate()
    output = output.decode('utf-8')
    return output


def main():
    dat, exp = expected()
    test01(execMain(dat), exp)


if __name__ == "__main__":
    main()
