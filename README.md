# celery-example

该项目包含了关于 Celery 的三个 Demo，其中 `notify_friends_exp` 和 `favorite_book_exp` 参考文章 [利用 Celery 构建 Web 服务的后台任务调度模块](https://www.ibm.com/developerworks/cn/opensource/os-cn-celery-web-service/index.html)，
而 `register_module` 包含了一个 Web 的注册案例，对比了传统同步的注册与使用Celery任务调度下注册的性能差异。

## 性能测试

假设用户的注册有以下几个步骤：
1. 将账号插入到数据库中
2. 向用户发送邮件通知
3. 向用户发送欢迎消息

在以前同步的实现中，一次请求必须完整的走完以上三个步骤才能响应给用户，可是用户其实并不需要等待邮件通知和欢迎消息，只需要将账号插入数据库就可以去做他想做的事了。
因此，我们完全可以将这两个步骤拆分出来异步的执行，当第一个步骤完成了就可以将结果响应给用户了，尤其是在后面的步骤十分耗时的情况下，
通过这种方式可以极大的提高系统的吞吐量。异步执行的步骤可以作为消息放入消息队列中，而 Celery 则为我们封装了消息队列（也就是一个Broker），
我们只需要使用 Celery 提供的API就可以很轻松的实现生产者和消费者了。

`register_module`使用 Flask 作为 Web 框架，选用 RabbitMQ 作为 Celery 的 Broker，其中`register`与`celery_register`接口分别展示了传统同步的注册方式与使用 Celery 的注册方式，
相关步骤的耗时都以`time.sleep`的方式模拟。以下是两种实现方式的性能测试对比，测试并不十分严谨，旨在说明使用异步方式对于系统吞吐量上的提高：

首先是QPS上的对比，横坐标轴为并发数：
![](http://blog.default.nanwulife.com/%E4%BC%A0%E7%BB%9F%E6%8A%98%E7%BA%BF%E5%9B%BE.png)

其次再来看看TP95这个指标，要注意的是，这里的值并不具有实际意义：

![](http://blog.default.nanwulife.com/%E4%BC%A0%E7%BB%9F%E6%8A%98%E7%BA%BF%E5%9B%BE%20%281%29.png)

## 使用方式

1. 安装好 Flask、Celery 与 RabbitMQ
2. 启动 RabbitMQ 服务，使用命令 `celery -A register_module.register_tasks worker --loglevel=info`开启 Celery
3. 运行 `register.py`，浏览器打开`http://127.0.0.1:5000/register/testUser/testEmail`显示`success`
4. 使用 JMeter 完成相关测试

