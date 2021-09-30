# This file fixes a typo in WP settings in a Holberton server
exec { 'fix_wordpress_conf':
  provider => 'shell',
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}
