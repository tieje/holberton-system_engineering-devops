change master to
    master_host='34.139.127.8',
    master_user='replica_user',
    master_password='root',
    master_log_file='mysql-bin.000004',
    master_log_pos=154,
    master_port=3306;
-- Justin's answer:
CHANGE MASTER TO
MASTER_HOST='<Your Web-01 IP address>',
MASTER_USER='replica_user',
MASTER_PASSWORD='<Your replica_user's password>',
MASTER_LOG_FILE='<Get this from SHOW MASTER STATUS;>',
MASTER_LOG_POS=<Get this from SHOW MASTER STATUS;>;
