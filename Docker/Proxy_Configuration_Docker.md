#### Configure proxy for yum

Refer link: https://www.linuxtechi.com/proxy-settings-yum-command-on-rhel-centos-servers/

#### Open Editor and add conf file for proxy

vi /etc/yum.conf

Add the below proxy in the conf file
'''
proxy=http://xx.xxx.xx.xx:xxxx
proxy_username=yyyyyy
proxy_password=zzzzz
'''
____________________________________

#### Docker installation

First Old version has to be unistalled if installed earlier

$ sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
				  
____________________________________

#### Setup yum repository

$ sudo yum install -y yum-utils

$ sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
	

#### list available versions

$ yum list docker-ce --showduplicates | sort -r

#### install docker 

$ sudo yum install docker-ce-19.03.9 docker-ce-cli-19.03.9 containerd.io

$ sudo systemctl start docker

____________________________________

#### To enable  proxy for Docker 

Refer link: https://www.sbarjatiya.com/notes_wiki/index.php/HTTP_proxy_configuration_for_Docker_on_CentOS_7

____________________________________
