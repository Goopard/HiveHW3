scp -P 2222 hw3_init root@localhost:/usr/jobs/hw3_init
ssh root@localhost -p 2222 command hive --database HW3 -f /usr/jobs/hw3_init
ssh root@localhost -p 2222