# Pika (Python Module)
UID: 202204181148
Tags: #🌱 
Links: [[Inter-process Communication]]

## Overview
> [!abstract]
> Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that tries to stay fairly independent of the underlying network support library.

## IO and Event Looping

As [[Advanced Message Queuing Protocol]](AMQP) is a two-way [[Remote Procedure Call]] (RPC) protocol where the client can send requests to the server and the server can send requests to a client, Pika implements or extends IO loops in each of its asynchronous connection adapters. These IO loops are blocking methods which loop and listen for events. Each asynchronous adapter follows the same standard for invoking the IO loop. The IO loop is created when the connection adapter is created. 

## Continuation-Passing Style

Interfacing with Pika asynchronously is done by passing in callback methods you would like to have invoked when a certain event completes. For example, if you are going to declare a queue, you pass in a method that will be called when the [[RabbitMQ]] server returns a [Queue.DeclareOk](http://www.rabbitmq.com/amqp-0-9-1-quickref.html#queue.declare) response.

In our example below we use the following five easy steps:

1.  We start by creating our connection object, then starting our event loop.
2.  When we are connected, the _on_connected_ method is called. In that method we create a channel.
3.  When the channel is created, the _on_channel_open_ method is called. In that method we declare a queue.
4.  When the queue is declared successfully, _on_queue_declared_ is called. In that method we call `channel.basic_consume` telling it to call the handle_delivery for each message RabbitMQ delivers to us.
5.  When RabbitMQ has a message to send us, it calls the handle_delivery method passing the AMQP Method frame, Header frame, and Body.