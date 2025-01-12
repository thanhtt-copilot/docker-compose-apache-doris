# Deploying Apache Doris with Docker

A recent project uses Apache Doris as a data warehouse. We need to set up a local testing environment for development. While deploying according to the official documentation, I encountered some issues and made some modifications.

This setup uses version 2.1.7. The relevant files have been uploaded to GitHub.

## Building the FE Image

Download the Doris binary package from [https://doris.apache.org/en-US/download/](https://doris.apache.org/en-US/download/) and save it to the `docker-build/fe/resource` directory. Choose the architecture as needed; here, I am using x64 (avx2).

Execute the following script:

```shell
cd docker-build/fe
docker build -t apache-doris:2.1.7-fe .
```

## Building the BE Image

Save the previously downloaded Doris binary package to the `docker-build/be/resource` directory.

Execute the following script:

```shell
cd docker-build/be
docker build -t apache-doris:2.1.7-be .
```

The official `init_be.sh` script has some issues and cannot start properly. I made some modifications.

`start_be.sh` was also modified and no longer requires disabling swap memory.

## Starting

Create a Doris installation directory to store Doris data, then execute the following script:

```shell
cd /path/to/doris
docker-compose up -d
```

Use `docker-compose logs -f be` to monitor the logs. When you see the "Ready to start BE!" log, the startup is successful.

## Connecting to Doris

Doris comes with two default accounts: `root` and `admin`. Both have no password. The `root` account has superuser privileges for the entire cluster and can perform various management operations, such as adding or removing nodes. The `admin` user does not have management permissions and is a superuser within the cluster, possessing all permissions except for cluster management-related ones.

Connect using the MySQL client:

```shell
mysql -uroot -P 9031 -h 127.0.0.1
```

Doris's built-in Web UI: [http://127.0.0.1:8031](http://127.0.0.1:8031)

## Shutdown

```shell
docker-compose down
```
