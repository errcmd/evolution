# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1536"
    vb.customize ["modifyvm", :id, "--audio", "none"]
  end

  # must be at the top
  config.vm.define "lb-0" do |c|
      c.vm.hostname = "lb-0"
      c.vm.network "private_network", ip: "192.168.199.40"

      c.vm.provision :shell, :path => "kube/scripts/vagrant-setup-haproxy.bash"

      c.vm.provider "virtualbox" do |vb|
        vb.memory = "512"
      end
  end

   # only 2 controllers instead of 3 because not enough RAM on laptop, if RAM > 16 feel free to change to 3
  (0..1).each do |n|
    config.vm.define "controller-#{n}" do |c|
        c.vm.hostname = "controller-#{n}"
        c.vm.network "private_network", ip: "192.168.199.1#{n}"

        c.vm.provision :shell, :path => "kube/scripts/vagrant-setup-hosts-file.bash"

        c.vm.provider "virtualbox" do |vb|
          vb.memory = "1536"
        end
    end
  end

   # only 1 worker instead of 3 because of RAM, if RAM > 16 feel free to change to 3
  (0..0).each do |n|
    config.vm.define "worker-#{n}" do |c|
        c.vm.hostname = "worker-#{n}"
        c.vm.network "private_network", ip: "192.168.199.2#{n}"

        c.vm.provision :shell, :path => "kube/scripts/vagrant-setup-routes.bash"
        c.vm.provision :shell, :path => "kube/scripts/vagrant-setup-hosts-file.bash"
    end
  end

  config.vm.define "traefik-0", autostart: false do |c|
      c.vm.hostname = "traefik-0"
      c.vm.network "private_network", ip: "192.168.199.30"

      c.vm.provision :shell, :path => "kube/scripts/vagrant-setup-routes.bash"

      c.vm.provider "virtualbox" do |vb|
        vb.memory = "512"
      end
  end
end
