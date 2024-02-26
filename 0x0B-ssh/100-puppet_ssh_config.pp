# To config ~/.ssh/config

$my_path =  ' /etc/ssh/ssh_config'

file {'config':
  ensure  =>  present,
  path    =>  $my_path,
  content => "Host server\n\tHostName 3.90.70.250\n\tUser ubuntu\n\tIdentityFile ~/.ssh/school\n\tPasswordAuthentication no"
}
