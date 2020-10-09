docker volume create jiraVolume

sudo chmod 666 /var/run/docker.sock

docker run -e JVM_SUPPORT_RECOMMENDED_ARGS="-Dhttp.proxyHost=10.169.33.81 -Dhttp.proxyPort=8080 -Dhttps.proxyHost=10.169.33.81 -Dhttps.proxyPort=8080 -Dhttp.nonProxyHosts=\"localhost|10.169.48.34|10.169.48.211|10.169.48.89|10.170.28.96|10.169.48.33\"" -v jiraVolume:/var/atlassian/application-data/jira --name="jira" -d -p 9080:8080 atlassian/jira-software
