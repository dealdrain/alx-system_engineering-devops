# creating a man killing a process

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
