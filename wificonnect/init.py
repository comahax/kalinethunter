#coding:utf-8
import os

def runcmd(cmd):
    cmd = cmd
    output = os.popen(cmd)
    print output.readlines()

def runcmd1(cmd):
    cmd = cmd
    output = os.popen(cmd)
    for l in output.readlines():
        if 'ESSID' in l:
            print l


if __name__ == '__main__':
    print '开启wlan1'
    cmd = 'ifconfig wlan1 up'
    runcmd(cmd)
    print '搜索附近wifi'
    cmd = 'iwlist wlan1 scan'
    runcmd1(cmd)

