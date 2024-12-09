# cloudtalents-startup-v1

Check out the [docker blog](https://www.linkedin.com/pulse/dockerizing-cloudtalents-startup-app-anoop-jayadharan-vskaf?utm_source=share&utm_medium=member_ios&utm_campaign=share_via) for a detailed explanation of the steps. 

# Docker
This section helps you learn dockerize a simple Python application.

## Application Components

* NGINX serves as reverse proxy
* Gunicorn acts as the application server
* Python Django web framework
* Postgres database to store session data

## Prerequisites
- Docker >= 24.0.7
- Docker Compose >=v2.30.3
- Tested on Ubuntu 20.04.6 LTS

## How it works

1. Clone the repository
```
git clone https://github.com/anoopjayadharan/cloudtalents-startup-v1.git
```

2. Create the following environment files

- .env.app
```

SECRET_KEY=
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=
SQL_USER=
SQL_PASSWORD=
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```
- .env.db
```
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
```


3. Build the Docker Image
```
docker-compose build
```

4. Run docker-compose up in detached mode
```
docker-compose up -d
```

5. Verify the container
```
docker-compose ps
```

6. Propogate Django changes to make to models into database schema
```
docker exec app python3 manage.py migrate
```

7. Change the permission of docker volume directory to facilitate the image upload
```
sudo chmod 777 -R /var/lib/docker/volumes
```

8. Access the application and upload images

# Kubernetes
To be filled
