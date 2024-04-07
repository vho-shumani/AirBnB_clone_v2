# Nginx configuration file content
$nginx_conf = @(EOT)
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 https://th3-gr00t.tk;
    }

    error_page 404 /404.html;

    location /404 {
        root /var/www/html;
        internal;
    }
}
EOT

# Install Nginx package
package { 'nginx':
  ensure   => 'installed',
  provider => 'apt',
}

# Ensure directory structure
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/releases/test', '/data/web_static/shared']:
  ensure => 'directory',
}

# Create index.html file for test
file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "Holberton School Puppet\n",
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

# Set ownership of directories
exec { 'chown -R ubuntu:ubuntu /data/':
  command => 'chown -R ubuntu:ubuntu /data/',
  path    => ['/usr/bin/', '/usr/local/bin/', '/bin/'],
}

# Ensure web server directories and files
file { ['/var/www', '/var/www/html', '/var/www/html/index.html', '/var/www/html/404.html']:
  ensure => 'directory',
}

# Create index.html and 404.html files
file { ['/var/www/html/index.html', '/var/www/html/404.html']:
  ensure  => 'present',
  content => "Holberton School Nginx\n",
}

# Ensure Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf,
}

# Restart Nginx service
exec { 'nginx_restart':
  command     => '/etc/init.d/nginx restart',
  refreshonly => true,
}

