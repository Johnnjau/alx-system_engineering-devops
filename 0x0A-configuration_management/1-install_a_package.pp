# Installs puppet-lint

package { 'puppet-lint':
  ensure   => '4.2.4',
  provider => 'gem',
}
