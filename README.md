# Simple Python Flask Dockerised API

[Docker image](https://hub.docker.com/r/lfriescozero/python-api-demo/)

Note: it appears that Gunicorn does not work on ECS with an ALB. [Possibly this.](https://github.com/benoitc/gunicorn/issues/1194)

Build

```bash
$ docker build -t api .
```

Run

```bash
$ docker run -it -p 2368:2368 api
```

```bash
$ curl http://localhost:2368
> "hello world"
```
