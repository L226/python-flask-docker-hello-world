# Simple Python Flask Dockerised API

### [docker image](https://hub.docker.com/r/lfriescozero/python-api-demo/)

Build

```bash
$ docker build -t api .
```

Run

```bash
$ docker run -it -p 8080:8080 api
```

```bash
$ curl http://localhost:8080
> "hello world"
```
