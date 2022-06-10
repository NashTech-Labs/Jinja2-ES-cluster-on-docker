# Readme

This repository contains a Jinja2 template file named `docker-compose.j2` and a python file `template.py` which renders the jinja2 template to `docker-compose.yaml`. The `docker-compose.yaml` thus rendered contains multi-node elasticsearch setup. We can configure the number of master and data nodes using the `config.yaml` file. This docker-compose deploys an elasticsearch 5.6.4

## Prerequisites

- Python3
- docker and docker-compose

## Install the requirements

To install required libraries, use the command:
```
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```

## Configure using config.yaml
| Key | Description |
| - | - |
| cluster_name | Name of the elastic search cluster|
| nodes | Total number of nodes in the cluster|
| masters | Total number of amster nodes in the ES cluster |
| master_port | The port on host where the master node will be exposed |
| network_name | The name of the network to create to deploy the cluster |

## Render the template

Make changes to the `config.yaml` file with appropriate values. The execute the following command to render the templateL:
```
python3 template.py
```

We will see a `docker-compose.yaml` file created.

## Create the ES cluster

To create the cluster, execute:
```
docker-compose up -d
```

## Verifying
To verify that the ES is running, execute the command:
```
curl localhost:<port-specified>
```