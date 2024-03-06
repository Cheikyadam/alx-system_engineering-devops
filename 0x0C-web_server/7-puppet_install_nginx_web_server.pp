ng script Nginx
# installation

include stdlib

package {'nginx':
  ensure => 'installed'
  }

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

exec {'ufw':
  command => '/usr/sbin/ufw allow "Nginx HTTP"',
  path    => '/usr/sbin/',
  #timeout => 0,
  user    => root,
  }

exec {'index':
  command => "/usr/bin/echo 'Hello World!' > /var/www/html/index.nginx-debian.html",
  path    => '/usr/bin',
  user    => root
  }


$my_path =  '/etc/nginx/sites-available/default'
$my_line =  "server_name _;\n\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}"
file_line {'config_ident':
  ensure =>  present,
  path   =>  $my_path,
  match  =>  '*server_name _;',
  line   =>  $my_line,
}

exec {'restart':
  command => '/usr/sbin/service nginx restart',
  path    => '/usr/sbin/',
  timeout => 0,
  user    => root
  #sudo    => true
  }
