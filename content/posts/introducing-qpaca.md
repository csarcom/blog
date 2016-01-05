Title: Introducing Qpaca - A Python project using Docker as development environment
Date: 2015-12-28 12:00
Category: Development
Tags: Docker, Python, Qpaca

Abstract
========

This post is not intended to be a Docker introduction. It will demonstrate how you can use Docker and docker-compose to run a full development environment. I will use as example a project called  [Qpaca](https://github.com/WeLikeAlpacas/qpaca).

Motivation
==========

The main reason to start doing Qpaca and write down this post was to learn Docker, and change my development environment with Vagrant. The problem with VMs is that they are expensive, if you want to keep components isolates it will be a pain to run a lot of VMs and keep Vagrantfiles working, with Docker and docker-compose is really simple and fast to code, test and ship it.

There a lot of benefits to use Docker as development environment:

* Have a development environment closer to production, it can be even closer if you are using Docker in production too.
* Docker containers are lightweight and easy to run.
* Easy to share your work with peers.
* Easy to create functional tests with external dependencies.
* It is fun!
	
Environment
===========

For now Docker runs only on linux, if you are using linux, you can install Docker following [Docker's documentation](https://docs.docker.com/linux/step_one/)

But, if you are using Mac OSX or Windows, you will need [Docker Toolbox](https://www.docker.com/docker-toolbox) and [VirtualBox 4.3](https://www.virtualbox.org/wiki/Download_Old_Builds_4_3)(I could not get it 100% using other version). After Docker Virtual Machine created, you need to forward all ports that you will need.

	VirtualBox -> right click on VM(default) -> Settings -> Network -> Port Forwarding -> Add all rules listing image below.

![VirtualBox Port Forwarding]({filename}/images/vb-forwarding.png)

About Qpaca
===========

Qpaca is a queue implementation wrote using Python, it uses RabbitMQ as message broker(maybe others in the future) and kombu. The project implement a publisher-subscriber model. We will have a entire platform with publisher(API REST), RabbitMQ, subscriber(s), InfluxDB and Grafana, the last two are projects that Qpaca use to write store data and show it in form of graphs, for real-time monitoring.

Running Qpaca
=============

Run Qpaca:

	git clone https://github.com/WeLikeAlpacas/Qpaca.git
	docker-compose up -d 

After couple of seconds, all container swill be up and running, in total we have 5 containers, 1 publisher, 1 subscriber, 1 RabbitMQ, 1 InfluxDB and 1 for Grafana.
If you want to run more subscriber containers, just run:

	docker-compose scale subscriber=<NUMBER>

Using Qpaca
===========

Look at docker-compose logs:

	docker-compose logs -f 

Now you can simulate a publish, I am using Postman for that. You should make a POST requests at http://127.0.0.1:8000/publish/. the content of the message must be json, and looks like it:

	{"payload": "Hello World!"}

At docker-compose log you can see the sent message and subscribers receiving that same message, you will see too some POST on InfluxDB, it is our way of mapping how many messages were sent and received, all this date are available at:

	http://localhost:3000/dashboard/db/pubsub

If you want to do something with received messages you can change the callback function at Qpaca/examples/subscriber.py

	:::python
	def custom_callback(body, message):
	    """
	    Do something with received messages
	    """
	    pass


You can simulate a higher request pool running:

	docker run -it --link pythonpubsub_publisher_1:pythonpubsub_publisher_1 -v /$(pwd):/app csarcom/python-pubsub python example/client.py

What about production?
======================

I did not have the opportunity to run Docker in production yet, so I kept focus at using Docker as development environment, but I would take a look at some points if I was considering Docker for production.

* How to orquestrate all containers with many hosts and different configurations?
* How to treat logs?
* How to monitoring containers?
* High Availability, service discovery between containers.
* Security, mostly at third-party images

There is a lot of information about all items above, and many successful articles about Docker in production, worth the research.
