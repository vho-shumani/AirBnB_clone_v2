#Configures a web server for deployment of web_static.

package { 'nginx':
  ensure   => installed,
} 
file { [
    '/data/web_static/shared',
    '/data/web_static/releases/test'
  ]:
    ensure => directory,
  }

file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => "Holberton School\n"
} 

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
} 

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

file { '/var/www':
  ensure => 'directory'
}

file { '/var/www/html':
  ensure => 'directory'
} 

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Holberton School Nginx\n"
} 

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n"
} 

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf
} 

exec { 'nginx restart':
  path => '/etc/init.d/'
}
