# containers [![Build Status](https://travis-ci.org/CleverParty/containers.svg?branch=master)](https://travis-ci.org/CleverParty/containers)

# Checkpoints :

1) (major) golang and python containers work in unison.
2) (major) Docker images are able to host website in 2 clicks.
3) Isolated GET ping issues in golang-gin routers.

Proposed : A Full fledged dockerised communication platform

Pro-Tip :-

(A) When using Django App on localhost , the folowing  commands make life easier :
 -  "ps -ef | grep runserver" and also  "pkill -9 -f runserver" to kill the runserver on the chosen port.

(B) When using the conda enviroment , on macOS its easier to load into the base python env(base) by using : "source ~/.zshrc" after setting the bash-profile by adding "source ~/.bash_profile" to the ~/.zshrc file.

(C) When in the base env, you can change the env by loading the required env through the source command,  and it will work like a charm.

# notes : 

# to start server : zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties

# simplified steps for kafka:
step 1 : brew install kafka
step 2 : start brokers, and kafka cluster requirements
step 3 : create topics , producers and consumers on said topic
step 4 : enjoy TCP protocol speeds
default is set to localhost:9092 to change default port edit file at : vim /usr/local/etc/kafka/server.properties

# ==> Caveats
To have launchd start kafka now and restart at login:
brew services start kafka
To have launchd start zookeeper now and restart at login:
  brew services start zookeeper
 Or, if you don't want/need a background service you can just run:
  - zkServer start
 ==> kafka
 To have launchd start kafka now and restart at login:
  - brew services start kafka
 Or, if you don't want/need a background service you can just run:
  - zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties & kafka-server-start /usr/local/etc/kafka/server.properties