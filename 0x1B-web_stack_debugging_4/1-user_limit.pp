# Reconfigure the OS for 'holberton' to login and open a file without any error message


exec { 'increase-file-limits-for-holberton':
  command => '/bin/sed -i -E -e "/^holberton\s+(hard|soft)\s+.*$/s/([45])$/50000/" /etc/security/limits.conf',
  path    => '/bin',
  unless  => '/bin/grep -E "^holberton\s+(hard|soft)\s+.*50000" /etc/security/limits.conf',
}

file { '/etc/security/limits.conf':
  ensure  => file,
  mode    => '0644',
  require => Package['coreutils'],
}
