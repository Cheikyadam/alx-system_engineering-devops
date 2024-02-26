# To config ~/.ssh/config
include stdlib
$my_path =  '/etc/ssh/ssh_config'

file_line {'config_ident':
  ensure =>  present,
  path   =>  $my_path,
  match  =>  '^*IdentityFile*rsa',
  line   =>  '#   IdentityFile ~/.ssh/school'
}

file_line {'config_passw':
  ensure =>  present,
  path   =>  $my_path,
  match  =>  '^*PasswordAuthentication',
  line   =>  '#   PasswordAuthentication no'
}
