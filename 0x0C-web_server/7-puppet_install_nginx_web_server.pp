# running script Nginx

include ufw
include stdlib

package {'Nginx':
  ensure => 'installed'
  }

ufw::rule {'allow_http':
  direction => 'in',
  port      => 80,
  action    => 'allow',
}

exec {'index':
  command => '/usr/bin/echo "Hello World!" > /var/www/html/index.nginx-debian.html',
  #environment => 'HOME=/root',
  path    => '/usr/bin'
  }


$my_path =  '/etc/nginx/sites-available/default'
my_line =  "server_name _;\n\n\tlocation \/redirect_me {\n\t\treturn 301 https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4;\n\t}"
file_line {'config_ident':
  ensure =>  present,
  path   =>  $my_path,
  match  =>  '*server_name _;',
  line   =>  $my_line 
}
