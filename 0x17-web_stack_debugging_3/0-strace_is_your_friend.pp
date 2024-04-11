#replacing .phpp with .php

exec { 'replace_class-wp-locale.phpp':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  path    => ['/bin', '/usr/bin'],
}
