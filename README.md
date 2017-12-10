## Name
product-management

## Overview
商品を管理するWebアプリケーション

## 準備
### Docker
```bash
# MariaDBコンテナの起動（バージョンは任意）
$ docker run --name mariadb -e MYSQL_ROOT_PASSWORD=mariadb -p 3306:3306 -d mariadb:10.1.16

# MariaDBへの接続
$ mysql -h 127.0.0.1 -uroot -pmariadb

# 作業完了したらコンテナを停止
$ docker stop mariadb
```

### MariaDB設定
