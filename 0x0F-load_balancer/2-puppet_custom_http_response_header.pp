#!/usr/bin/env bash
#!/usr/bin/env bash
#task advance with pupppet
exec { 'http header':
       command  => 'sudo apt-get update -y;
       sudo apt-get install nginx -y;
       sudo sed -i "/server_name _/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default
       sudo service nginx restart',
       provider => shell,
}
#automate custom header response
exec { 'update':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell'
}


#installs nginx
-> package { 'nginx':
  ensure   => present,
  name     => 'nginx',
  provider => 'apt'
}


#sets index content
-> file { 'index.html':
  ensure  => present,
  path    => '/var/www/html/index.html',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => 'Holberton School'
}


#sets 404 contentfile
-> { '404.html':
  ensure  => present,
  path    => '/var/www/html/404.html',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => "Ceci n'est pas une page"
}


#sets config
-> exec { 'Set default /redirect_me':
  command  => 'sed -i "48i \\\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}" /etc/nginx/sites-available/default',
  user     => 'root',
  provider => 'shell'
}


-> exec { 'Set default /404':
  command  => 'sed -i "42i \\\n\terror_page 404 /404.html;" /etc/nginx/sites-available/default',
  user     => 'root',
  provider => 'shell'
}


-> exec { 'Set X-Served-By':
  command  => 'sed -i "48i \\\t\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default',
  user     => 'root',
  provider => 'shell'
}


-> exec { 'Start nginx':
  command  => 'service nginx restart',
  user     => 'root',
  provider => 'shell'
}
