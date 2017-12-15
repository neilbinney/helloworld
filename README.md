# Distelli Test Project.

## Getting Started

Project is designed to build on own hardware running Ubuntu 16.04.  

Ensure that the version of git being used is later than 2.5:

```
root@pi-sit01:/# git --version
git version 2.7.4
```

## Installing the Distelli Agent

Install the agent:

```
[root@pi-sit01 ~]# wget -qO- https://www.distelli.com/download/client | sh
    Installing Distelli CLI 3.66.33 for architecture 'Linux-x86_64'...
    Downloading https://s3.amazonaws.com/download.distelli.com/distelli.Linux-x86_64/distelli.Linux-x86_64-3.66.33.gz
To install the agent, run:
    sudo /usr/local/bin/distelli agent install
```

Configure the agent:

```
[root@pi-sit01 ~]# /usr/local/bin/distelli agent install
Login can be automated. See: http://distel.li/AgentCreds
Distelli Email: neil.binney@puppet.com
      Password:
Server Info: https://www.distelli.com/neilbinney/servers/258db99f-7390-ba46-b683-fa163eb353f5
Starting sysv daemon with conf:	/etc/init.d/dtk-supervise-cc1233c06f7ad94a8d34ac610381242f9ae28bb8
Starting Distelli supervisor
```

Check the agent is running:

```
[root@pi-sit01 ~]# /usr/local/bin/distelli agent status
Distelli Agent https://www.distelli.com/neilbinney/servers/258db99f-7390-ba46-b683-fa163eb353f5 is Running
```


