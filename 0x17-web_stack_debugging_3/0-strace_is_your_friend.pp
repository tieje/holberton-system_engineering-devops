# fixes apache config
exec { 'modify_file':
    command => "sudo sed -i 's/phpp/php/g' '/var/www/html/wp-settings.php'",
    path    => '/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
