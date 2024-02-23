# using exec with puppet

exec {'killing':
  command => '/usr/bin/pkill killmenow',
  #environment => 'HOME=/root',
  path    => '/usr/bin'
  }
