docker volume create jiraVolume

sudo chmod 666 /var/run/docker.sock

docker run -e JVM_SUPPORT_RECOMMENDED_ARGS="-Dhttp.proxyHost=xx.xxx.xx.xx -Dhttp.proxyPort=8080 -Dhttps.proxyHost=xx.xxx.xx.xx -Dhttps.proxyPort=8080 -Dhttp.nonProxyHosts=\"localhost|xx.xxx.xx.xx|xx.xxx.xx.xx|xx.xxx.xx.xx|xx.xxx.xx.xx|xx.xxx.xx.xx\"" -v jiraVolume:/var/atlassian/application-data/jira --name="jira" -d -p xxxx:xxxx atlassian/jira-software
