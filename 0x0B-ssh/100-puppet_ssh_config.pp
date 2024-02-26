# To config ~/.ssh/config

$my_path =  '/root/.ssh/config'

file {'config':
  ensure  =>  present,
  path    =>  $my_path,
  content =>  'Host server\n	HostName 3.90.70.250\n	User ubuntu\n	IdentityFile ~/.ssh/school\n	PasswordAuthentication no'
}
