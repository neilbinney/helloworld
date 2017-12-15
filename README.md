# Distelli Test Project.

## Getting Started

Project is designed to build on own hardware running Ubuntu 16.04.  

Ensure that the version of git being used is later than 2.5:

```
root@pi-sit01:/# git --version
git version 2.7.4
```

## Installing the Distelli Agent

As root install the agent:

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

## Distelli Web-UI

###  Configure Server

* Select **Servers** from the top of the WebUI
* Select the server you have created from the list
* Enable **Key Management Server**
* Enable **Job/Build Server**
* Specify a name in **Capabilities** to pair application builds to server 

[![server](https://github.com/neilbinney/helloworld/raw/screenshots/screenshots/server.png)](#features)



### Create the Application

* Select **Applications** from the top of the WebUI
* Select **New APP** button
* Name the Application

### Connect your application to source control

[![connect_repo](https://github.com/neilbinney/helloworld/raw/screenshots/screenshots/connect_repo.png)](#features)

### Select a repository

[![select_repo](https://github.com/neilbinney/helloworld/raw/screenshots/screenshots/select_repo.png)](#features)
### Select branches

[![select_branch](https://github.com/neilbinney/helloworld/raw/screenshots/screenshots/select_branch.png)](#features)
### Configure build steps
* Select **Build Distelli Release**
* Tick **Advanced user? Use a distelli-manifest.yml instead of editing your build steps in the app.** box.
[![config_build](https://github.com/neilbinney/helloworld/raw/screenshots/screenshots/config_build.png)](#features)
### Review your build configuration
* Tick **Build on my own hardware**
* Specify a name in **Build Capabilities** to pair application builds to server
[![review](https://github.com/neilbinney/helloworld/raw/screenshots/screenshots/review.png)](#features)
### Start the build
Select **Looks Good.  Start Build**
Select **Go To Builds**

Distelli will pull a fresh copy of the repo each time it builds the app.

### Create application environment

* Select **Applications** from the top of the WebUI
* Select Environments
* Select Create Environment

  Create Environment
[![environment](https://github.com/neilbinney/helloworld/raw/screenshots/screenshots/environment.png)](#features)
### Create application environment

* Select **Servers** from the top of the WebUI
* Select **Edit Environments**
* Select the new environment and click **Add Environments** to add the environment to the server

[![addenvironment](https://github.com/neilbinney/helloworld/raw/screenshots/screenshots/addenvironment.png)](#features)
###  Deploying the App
Following a successful build a release is created.

*From the build page select **New Deployment**


[![deplyment](https://github.com/neilbinney/helloworld/raw/screenshots/screenshots/deploy1.png)](#features)

## Django Code

A Django 'hello world' example.

For run this example need to install Django
framework execute the follow command::

    $ sudo pip install -r requirements.txt

And later followed by::

    $ python manage.py migrate

At which point you should see::

    Operations to perform:
      Apply all migrations: admin, contenttypes, sites, auth, sessions
    Running migrations:
      Rendering model states... DONE
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying sessions.0001_initial... OK
      Applying sites.0001_initial... OK
      Applying sites.0002_alter_domain_unique... OK

After which you can run::

    $ python manage.py runserver

And open the following URL in your web browser:

 - http://127.0.0.1:8000/

And you can see the hello world example like this :

.. figure:: https://github.com/django-ve/helloworld/raw/master/docs/django_helloword.png
   :width: 332px
   :align: center
   :alt: A Django 'Hello World' example


