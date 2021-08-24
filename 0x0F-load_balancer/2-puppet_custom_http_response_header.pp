# creating a custom HTTP header response, but with Puppet.

package { 'nginx':
  ensure => 'installed',
}

file_line { 'Add headers':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => '.*listen \[.*;',
  line   => '	add_header X-Served-By $hostname;'
}

service {'nginx':
  ensure  => 'running',
  require => Package['nginx']
}
