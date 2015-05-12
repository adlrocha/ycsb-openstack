import string
import commands
import time

fwlm=open('workloadmodel','r')
swlm=fwlm.read()
fswm=open('startworkloadmodel','r')
sswm=fswm.read()

def generatefile(config):
	tmpwl=swlm
	tmpsw=sswm

	tmpwl=string.replace(tmpwl,'aaa',config[4])
	tmpwl=string.replace(tmpwl,'bbb',config[2])
	tmpwl=string.replace(tmpwl,'ccc',config[3])
	fout=open('/home/clientdown/workload','w')
	fout.write(tmpwl)
	fout.close()

	tmpsw=string.replace(tmpsw,'aaa',config[5])
	tmpsw=string.replace(tmpsw,'bbb',config[6])
	fout=open('/home/clientdown/startworkload.sh','w')
	fout.write(tmpsw)
	fout.close()


def getfreeip():
    ret=commands.getoutput("nova floating-ip-list")
    m=ret.splitlines()

    blank=" | -                                    | -             | " #search for the first unoccupied ip

    for i in m:                              #take out the ip address
        if(i.find(blank)!=-1):
            return i[2:13]

	
	
def startvm(config):
    generatefile(config)	
    freeip=getfreeip()
	
    ret=commands.getoutput("nova boot --flavor 2 --image 20cf5437-6eea-4498-9ae0-125a4f973a11 --key-name huiyuning --nic net-id=f3327bd6-9658-425e-be09-44c6eb14e603 aaa")
    m=ret.splitlines()
    vmid=m[20][41:77]
    time.sleep(1)
    commands.getoutput("nova floating-ip-associate " + vmid + " " + freeip)
    print freeip



 

fconfig=open('config','r')
fconfig.readline()
for line in fconfig:
	s=line.split()
	startvm(s)




