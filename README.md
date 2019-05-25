# 莲花项目

## 本地环境搭建

依赖环境：
 1. docker
 2. docker-compose

步骤：
 1. `git clone https://github.com/largerbigsuper/LianHua.git`
 2. `cd LianHua`
 3. `docker-compose up`
 
数据迁移:

```shell
docker-compose run web python manage.py makemigrations common customers products stores data

docker-compose run web python manage.py migrate

```

访问 `127.0.0.1`

## app 登录认证

需要登录的请求需要在请求头上携带`Authorization`参数，值为 `Token token`

token 为登录成功获取的 token

示例：

```
Authorization: Token d29ca8f1f2d0f8958b0aa206cbdd7cb241829233
```
 