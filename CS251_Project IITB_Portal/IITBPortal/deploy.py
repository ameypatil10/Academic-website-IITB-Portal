#!/usr/bin/env python
from deployer.client import start
from deployer.node import Node

class DjangoDeployment(Node):
    pass

if __name__ == '__main':
    start(DjangoDeployment)