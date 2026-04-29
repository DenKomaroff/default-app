import asyncio
from adapters.web import main, Config
from adapters.restapi import web_app
import socket
from random import randint
# from libs.dcs import DistributedClient


class Service:

    @property
    def app(self):
        return self._application

    def __init__(self, name, *, host=None, port=None):
        self.name = name
        self.host = host or '0.0.0.0'
        self.port = port or self.get_free_port()
        self._application = None
        self.debug = True

    def init_application(self, app):
        self._application = app
        return self

    def start(self):
        self.init_application(app=web_app)
        cfg = Config()
        cfg.bind = f'{self.host}:{self.port}'
        # DistributedClient(name=self.name, check=self.health_check)
        asyncio.run(main(self.app, cfg), debug=self.debug)
        return self

    def stop(self):
        pass

    def health_check(self):
        return self.app.health_check()

    @staticmethod
    def get_free_port(a=40801, b=40999):

        def get_host_ip():
            return socket.gethostbyname(socket.getfqdn())

        def port_is_open(host, port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((host, port))
            sock.close()
            return result == 0

        free_port = randint(a, b)
        while port_is_open(get_host_ip(), free_port):
            free_port = randint(a, b)
        return free_port
