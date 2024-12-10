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

SECRET_KEY=<FILL_HERE>
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=<FILL_HERE>
SQL_USER=<FILL_HERE>
SQL_PASSWORD=<FILL_HERE>
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```
- .env.db
```
POSTGRES_USER=<FILL_HERE>
POSTGRES_PASSWORD=<FILL_HERE>
POSTGRES_DB=<FILL_HERE>
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

Check out the [k8s blog](https://www.linkedin.com/posts/anoop-jayadharan-ba677998_in-the-previous-post-we-used-docker-compose-activity-7272231653991731200-5TlU?utm_source=share&utm_medium=member_desktop) for step by step execution.

## Prerequisites
- Kubernetes cluster >= v1.31.1
- Docker >= 24.0.7
- Docker Compose >=v2.30.3
- Tested on Ubuntu 20.04.6 LTS
- alias 'k=kubectl'

```
anoop@cks-master:~/cloudtalents-startup-v1$ k get nodes
NAME         STATUS   ROLES           AGE    VERSION
cks-master   Ready    control-plane   4d6h   v1.31.1
cks-worker   Ready    <none>          4d6h   v1.31.1
```

## How it works

1. Clone the repository
```
git clone https://github.com/anoopjayadharan/cloudtalents-startup-v1.git

cd kubernetes/
```

2. Create the secret files

- db-secrets
```
POSTGRES_USER=<FILL_HERE>
POSTGRES_PASSWORD=<FILL_HERE>
POSTGRES_DB=<FILL_HERE>
```
- django-secrets
```
SECRET_KEY=<FILL_HERE>
SQL_DATABASE=<FILL_HERE>
SQL_USER=dbadmin
SQL_PASSWORD=<FILL_HERE>
SQL_HOST=db
SQL_PORT=5432
```

3. Create k8s secret resources
```
k create secret generic postgres-secret --from-env-file db-secrets
k create secret generic app-secret --from-env-file django-secrets
```

4. Install Rancher local-path provisioner
```
kubectl apply -f https://raw.githubusercontent.com/rancher/local-path-provisioner/v0.0.30/deploy/local-path-storage.yaml
```

5. Create Postgres StatefulSet
```
k apply -f postgres-sts.yaml
```

6. Create Django deployment
```
k apply -f app-deploy.yaml
```

7. Execute Django migration
```
k exec -it <app pod name> -- python3 manage.py migrate
```

8. Create NGINX deployment
```
k apply -f nginx-deploy.yaml
```

9. Install [NGINX Ingress Controller](https://docs.nginx.com/nginx-ingress-controller/installation/installing-nic/installation-with-manifests/) following the offcial documentation
```
git clone https://github.com/nginxinc/kubernetes-ingress.git --branch v3.7.2
```

10. Modify nodePort to 31780 
```
k edit svc -n nginx-ingress nginx-ingress
search for nodePort
change it to 31780
```

11. Create an ingress resource
```
k apply -f ingress.yaml
```

12. Add a local DNS entry for app FQDN pointing to the k8s master node IP

13. Access the application from a web browser
```
http://cloudtalentstartup.com:31780
```
