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
 