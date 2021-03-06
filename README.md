# RBMQ Practice

## Example 1
### round robin for passing messages to receivers
![round robin](images/example1-round-robin.JPG)

## Example 2
### tasks survive failure of worker
![still round robin](images/example2.JPG)
### dispatching tasks fairly
![fair dispatching](images/example2-dispatch.JPG)

## Example 3
### broadcast messages
![broadcast](images/example3.JPG)

## Example 4
### direct exchange
![direct-exchange](images/example4.JPG)

## Example 5
### topic exchange
![topic-exchange](images/example5.JPG)

## TODO
- [ ] add timezone into docker

## Docker

### Using `rabbitmqctl` in the Container

> $ docker exec rabbitmq su rabbitmq -- /opt/rabbitmq/sbin/rabbitmqctl \<command\>

#### show status
> $ docker exec rabbitmq su rabbitmq -- /opt/rabbitmq/sbin/rabbitmqctl status

#### list exchanges
> $ docker exec rabbitmq su rabbitmq -- /opt/rabbitmq/sbin/rabbitmqctl list\_exchanges

#### list queues
> $ docker exec rabbitmq su rabbitmq -- /opt/rabbitmq/sbin/rabbitmqctl list\_queues

#### list detail of queues
> $ docker exec rabbitmq su rabbitmq -- /opt/rabbitmq/sbin/rabbitmqctl list\_queues name messages\_ready messages\_unacknowledged

#### list bindings
> $ docker exec rabbitmq su rabbitmq -- /opt/rabbitmq/sbin/rabbitmqctl list\_bindings

## [Source of Examples](https://www.rabbitmq.com/)
