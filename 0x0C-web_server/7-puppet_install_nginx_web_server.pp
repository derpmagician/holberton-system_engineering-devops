# Install Nginx web server with Puppet

$link = 'https://www.youtube.com/watch?v=QH2-TGUlwu4'
$content = "rewrite ^/redirect_me/$ ${link} permanent;"

package { 'nginx':
  ensure => installed,
}

file_line { 'Add redirection, 301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => $content,,
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Holberton School',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
