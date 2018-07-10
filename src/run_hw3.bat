scp -P 2222 hw3 root@localhost:/usr/jobs/hw3
ssh root@localhost -p 2222 command "hive --database HW3 -f /usr/jobs/hw3 > /usr/jobs/output.txt"
scp -P 2222 root@localhost:/usr/jobs/output.csv ..\output\output.txt
ssh root@localhost -p 2222