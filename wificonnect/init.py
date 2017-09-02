#coding:utf-8
import os
import subprocess
import time
wifilist = []
def runcmd(cmd):
    cmd = cmd
    output = os.popen(cmd)
    print output.readlines()

def runcmd1(cmd):
    cmd = cmd
    output = os.popen(cmd)
    for l in output.readlines():
        number = 0
        if 'ESSID' in l:
            print str(number)+":"+l
            wifilist.append(l.split(':')[1])


if __name__ == '__main__':
    print '开启wlan1'
    cmd = 'ifconfig wlan1 up'
    runcmd(cmd)
    print '搜索附近wifi'
    cmd = 'iwlist wlan1 scan'
    runcmd1(cmd)
    print '输入你要连接的wifi编号'
    a = raw_input('please input the wifi number which you want to connect')
    a = int(a)
    cmd = "rm /etc/wpa_supplicant.conf"
    runcmd(cmd)
    cmd = "touch /etc/wpa_supplicant.conf"
    runcmd(cmd)
    cmd = 'wpa_passphrase ' + wifilist[a]
    #cmd = "ls"
    print cmd
    pipe = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    in = raw_input('password')
    pipe.stdin.write(in)
    pipe.stdin.flush()
    time.sleep(2)
    out = pipe.stdout.read()
    print out
    file = "/etc/wpa_supplicant.conf"
    with open(file,'w') as f:
        f.write(out)
    cmd = 'wpa_supplicant -i wlan1 -c /etc/wpa_supplicant.conf'
    runcmd(cmd)



