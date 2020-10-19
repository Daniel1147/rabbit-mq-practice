# RBMQ Practice

## example1
### round robin for passing messages to receivers
![round robin](images/example1-round-robin.JPG)

## example2
### tasks survive failure of worker
![still round robin](images/example2.JPG)
### dispatching tasks fairly
![fair dispatching](images/example2-dispatch.JPG)

## TODO
- [ ] add timezone into docker

## Docker

### Using `rabbitmqctl` in the Container

```
$ docker exec rabbitmq su rabbitmq -- /opt/rabbitmq/sbin/rabbitmqctl <command>
```

## [Source of Examples](https://www.rabbitmq.com/)
