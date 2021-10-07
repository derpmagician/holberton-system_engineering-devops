# Limit fix for nginx

exec { 'Increase fd':
    command => '/bin/echo "ULIMIT=\"-n 500\"" > /etc/default/nginx'
}
-> exec { 'Restart nginx':
    command => 'sudo service nginx restart',
    path    => ['/usr/bin/']
}

