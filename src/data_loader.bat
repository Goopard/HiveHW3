scp -P 2222 user_agent_parser.py root@localhost:/usr/jobs/test.py
scp -P 2222 ..\input\city.en.txt root@localhost:/usr/jobs/cities.txt
scp -P 2222 ..\input\imp.20131019.txt root@localhost:/usr/jobs/input0.txt
scp -P 2222 ..\input\imp.20131020.txt root@localhost:/usr/jobs/input1.txt
scp -P 2222 ..\input\imp.20131021.txt root@localhost:/usr/jobs/input2.txt
scp -P 2222 ..\input\imp.20131022.txt root@localhost:/usr/jobs/input3.txt
scp -P 2222 ..\input\imp.20131023.txt root@localhost:/usr/jobs/input4.txt
scp -P 2222 ..\input\imp.20131024.txt root@localhost:/usr/jobs/input5.txt
scp -P 2222 ..\input\imp.20131025.txt root@localhost:/usr/jobs/input6.txt
scp -P 2222 ..\input\imp.20131026.txt root@localhost:/usr/jobs/input7.txt
scp -P 2222 ..\input\imp.20131027.txt root@localhost:/usr/jobs/input8.txt

ssh root@localhost -p 2222 command hadoop fs -mkdir /user/raj_ops/cities/
ssh root@localhost -p 2222 command hadoop fs -copyFromLocal /usr/jobs/cities.txt /user/raj_ops/cities/
ssh root@localhost -p 2222 command hadoop fs -mkdir /user/raj_ops/contest/
ssh root@localhost -p 2222 command hadoop fs -copyFromLocal /usr/jobs/input0.txt /user/raj_ops/contest/
ssh root@localhost -p 2222 command hadoop fs -copyFromLocal /usr/jobs/input1.txt /user/raj_ops/contest/
ssh root@localhost -p 2222 command hadoop fs -copyFromLocal /usr/jobs/input2.txt /user/raj_ops/contest/
ssh root@localhost -p 2222 command hadoop fs -copyFromLocal /usr/jobs/input3.txt /user/raj_ops/contest/
ssh root@localhost -p 2222 command hadoop fs -copyFromLocal /usr/jobs/input4.txt /user/raj_ops/contest/
ssh root@localhost -p 2222 command hadoop fs -copyFromLocal /usr/jobs/input5.txt /user/raj_ops/contest/
ssh root@localhost -p 2222 command hadoop fs -copyFromLocal /usr/jobs/input6.txt /user/raj_ops/contest/
ssh root@localhost -p 2222 command hadoop fs -copyFromLocal /usr/jobs/input7.txt /user/raj_ops/contest/
ssh root@localhost -p 2222 command hadoop fs -copyFromLocal /usr/jobs/input8.txt /user/raj_ops/contest/
