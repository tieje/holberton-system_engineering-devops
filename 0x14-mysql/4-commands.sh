
server-id               = 1
sudo sed -i 's/bind-address/#bind-address'

# web-02
# linux
sudo sed -i 's/server-id\s*= 1/server-id = 2/' /etc/mysql/mysql.conf.d
