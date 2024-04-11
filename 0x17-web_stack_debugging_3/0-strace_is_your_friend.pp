#To correct class-wp-locale.phpp
include stdlib

file_line { 'replace_class-wp-locale.phpp':
  ensure => present,
  line   => 'require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );',
  match  => '*class-wp-locale.phpp*',
  path   => '/var/www/html/wp-settings.php',
}
