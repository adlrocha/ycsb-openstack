#################################
#OpenStack automate experiment
#Alfonso de la Rocha - 2015
#################################


nova boot --flavor 1 --image cirros --key-name arocha-cloud --user-data \
run-ycsb.sh\
--security-groups default VM-NAME --nic net-id=269e9008-98b7-4544-901d-b43cbb6daf85

#According
nova floating-ip-associate VM-NAME 10.7.126.1

#Waits for a signal from the VM and runs the next one to simulate a PaaS


