#Sky is the limit

exec { 'limit_fix':
  command => "sed -i 's/^ULIMIT.*/ULIMIT=\"-n 15000\"/g' /etc/default/nginx",
  path    => ['/bin', '/usr/bin'],
}


exec { 'nginx_restart':
  command => '/usr/sbin/service nginx restart',
  path    => '/bin:/usr/bin:/sbin:/usr/sbin',
  user    => 'root'
}
