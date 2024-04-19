#Sky is the limit

exec { 'limit_fix':
  command => "sed -i 's/^ULIMIT.*/ULIMIT=\"-n 15000\"/g' /etc/default/nginx",
  path    => ['/bin', '/usr/bin'],
}
