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

1. Create folder for configuring docker service through systemd
mkdir /etc/systemd/system/docker.service.d

2. Create service configuration file at /etc/systemd/system/docker.service.d/http-proxy.conf

 cd /etc/systemd/system/docker.service.d

 vi http-proxy.conf

 Add the below data in the http-proxy.conf file as per your requirements
 
 '''
 
 [Service]

 Environment="HTTP_PROXY=http://proxy.iiit.ac.in:8080/" "NO_PROXY=localhost,127.0.0.0/8,10.0.0.0/8,192.168.0.0/16,172.16.0.0/12"
 
 '''

3. Reload systemctl so that new settings are read

sudo systemctl daemon-reload

4. Verify that docker service Environment is properly set

sudo systemctl show docker --property Environment

5. Restart docker service so that it uses updated Environment settings

sudo systemctl restart docker

____________________________________
