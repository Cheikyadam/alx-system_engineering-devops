# Installing a package with puppet using pip3

package { 'Flask':
  ensure   =>  'latest',
  provider =>  'pip3'
  }
