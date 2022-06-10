from tempfile import template
from jinja2 import Template, Environment, FileSystemLoader
import yaml

env = Environment(loader=FileSystemLoader("./"))
template = env.get_template('docker-compose.j2')
with open(r'./config.yaml') as file:
    config_list = yaml.load(file, Loader=yaml.FullLoader)


master_nodes = int(config_list['masters'])
configs = {}
configs['cluster_name'] = config_list['cluster_name']
configs['min_master'] = int(int(config_list['masters'])/2 + 1)
configs['master_port'] = config_list['master_port']
configs['network'] = config_list['network_name']
dependancies = {}
master_configs = {}
masters=" "
data_configs={}
data_nodes = config_list['nodes'] - master_nodes


if data_nodes <= 0:
    raise Exception('Data nodes cannot be 0')
datas = ""


for i in range(1, master_nodes+1):
    master_configs["es-master-" + str(i)] = {
        "hosts": masters,
        "is_master": "true",
        "is_data": "false"
    }
    dependancies["es-master-" + str(i)] = masters.split(",")
    masters = masters + " es-master-"+str(i)
    masters=masters.strip().replace(" ", ",")

node_configs = master_configs
datas = masters


for i in range(1, data_nodes+1):
    data_configs["es-data-" + str(i)] = {
        "hosts": datas,
        "is_master": "false",
        "is_data": "true"
    }
    dependancies["es-data-" + str(i)] = datas.split(",")
    datas = datas + " es-data-" + str(i)
    datas = datas.strip().replace(" ", ",")

node_configs.update(data_configs)
configs['nodes']=node_configs


docker_compose = open("docker-compose.yaml", "w")
docker_compose.write(template.render(configs, dependancies=dependancies))