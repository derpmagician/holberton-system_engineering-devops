# This file fixes a typo in WP settings in a Holberton server
exec { 'fix wordpress conf':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}
