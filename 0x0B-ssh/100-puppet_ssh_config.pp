# To config ~/.ssh/config

$my_path =  '/root/.ssh/config'

file {'config':
  ensure  =>  present,
  path    =>  $my_path,
  content => "Host server\n\tHostName 3.90.70.250\n\tUser ubuntu\n\tIdentityFile ~/.ssh/school\n\tPasswordAuthentication no"
}
