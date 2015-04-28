###############################
#YCSB Benchmark automatization
#Alfonso de la Rocha - 2015
#Modified by Yuning Hui on cassandra start judgements - 2015.4.24
###############################

#USAGE: ./ycsb-experiment workload_file [-threads] x [-target] y
#For the workload you just specify the name of the file
#located in the workload directory with the attributes of
#your experiment


sudo /sbin/cassandra > ./tmp.log

a=`grep "state jump to normal" ./tmp.log`

while [ "$a" = "" ]
do
    a=`grep "state jump to normal" ./tmp.log`
done

cd /home/centos/YCSB-compilation

#Default values
threads=1
target=100

#Check arguments
if [[ -z "$1" ]]
then
    echo "You must specify a workload in ./workloads/"
    exit 2
fi

if [ "$2" = "-threads" ];
then
    threads=$3
    echo "Threads specified "
fi


if [ "$4" = "-target" ];
then
    target=$5
    echo "Target specified "
fi

#Run the benchmark
./bin/ycsb load cassandra-cql -P ./workloads/$1
./bin/ycsb run cassandra-cql -P ./workloads/$1 -threads $threads -target $target

