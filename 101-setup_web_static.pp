package { 'nginx':
  ensure => installed,
  provider => 'apt'
}

# Create directories
file { ['/data/web_static/releases/test', '/data/web_static/shared']:
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Create index.html file
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n",
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Update Nginx configuration
file_line { 'nginx_hbnb_static_location':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "    location /hbnb_static {\n        alias /data/web_static/current/;\n    }\n",
  match  => "^server_name _;$",
}

# Restart Nginx service if the configuration is successful
exec { 'nginx_test_and_restart':
  command     => 'nginx -t && service nginx restart',
  path        => ['/usr/bin', '/usr/sbin', '/bin'],
  refreshonly => true,
}

