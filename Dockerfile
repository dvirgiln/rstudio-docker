# JupyterHub
# This image is built by docker-compose

#ARG JUPYTERHUB_VERSION=0.9.2
#ARG JUPYTERHUB_VERSION=0.9.6
#ARG JUPYTERHUB_VERSION=latest
ARG JUPYTERHUB_VERSION=1.0.0

FROM jupyterhub/jupyterhub:${JUPYTERHUB_VERSION}

## Upgrade pip
RUN pip install --upgrade pip setuptools

## Make shared file system folder
RUN mkdir -p /jupyterhub/user
RUN apt-get update
RUN pip install psycopg2-binary

## Install dummyauthenticator for testing purposes
RUN pip install --no-cache jupyterhub-dummyauthenticator jupyterhub-ldapauthenticator

## Important: Mount the jupyterhub main configuration file
ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py


RUN useradd -m -G shadow -p $(openssl passwd -1 rhea) rhea
RUN chown rhea .

RUN for name in io ganymede ; do useradd -m -p $(openssl passwd -1 $name) $name; done

WORKDIR /srv/jupyterhub
