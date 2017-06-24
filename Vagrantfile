# -*- m: ruby -*-
# vi: set ft=ret ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
    config.vm.provision :shell, path: "bootstrap.sh"
    config.vm.provision "file", source: ".vimrc", destination: ".vimrc"
end
