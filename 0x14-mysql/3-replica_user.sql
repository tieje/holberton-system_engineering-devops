create user 'replica_user'@'%' identified by 'root';
grant create, select on tyrell_corp.* to 'replica_user'@'%';
grant replication client, replication slave on *.* to 'replica_user'@'%';
grant replication slave on *.* to 'replica_user'@'%';
