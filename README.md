# Simple Python Flask Dockerised API#

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