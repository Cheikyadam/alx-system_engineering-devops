# To config ~/.ssh/config
include stdlib

$my_path =  '/root/.ssh/config'

file_line {'Turn off passwd auth':
  ensure =>  present
  path   =>  $my_path,
  line   =>  'HostName 3.90.70.250'
}

file_line {'Turn off passwd auth':
  ensure =>  present
  path   =>  $my_path,
  line   =>  'User ubuntu'
}

file_line {'Turn off passwd auth':
  ensure =>  present
  path   =>  $my_path,
  line   =>  'PasswordAuthentication no'
}

file_line {'Declare identity file':
  ensure =>  present
  path   =>  $my_path,
  line   =>  '~/.ssh/school'
}
