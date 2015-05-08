#Automatically start a new VM and assign a floating IP to it.
#Run with root access and source ~/keystone


import commands
import time

def getfreeip():
    ret=commands.getoutput("nova floating-ip-list")
    m=ret.splitlines()

    blank=" | -                                    | -             | " #search for the first unoccupied ip

    for i in m:                              #take out the ip address
        if(i.find(blank)!=-1):
            return i[2:13]


def startvm():
    freeip=getfreeip()

    ret=commands.getoutput("nova boot --flavor 1 --image 5e50ba9e-e4cb-4d10-a13b-787c023c3275 --key-name huiyuning --nic net-id=f3327bd6-9658-425e-be09-44c6eb14e603 aaa")
    m=ret.splitlines()
    vmid=m[20][41:77]
    time.sleep(1)
    commands.getoutput("nova floating-ip-associate " + vmid + " " + freeip)
    print freeip


startvm()


