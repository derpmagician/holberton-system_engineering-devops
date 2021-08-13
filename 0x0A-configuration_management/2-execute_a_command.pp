# Kills a process named 'killmenow' using Puppet

exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/bin']
}
