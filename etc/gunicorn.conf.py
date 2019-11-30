import os
import sys
import netifaces
from ipaddress import IPv4Address
import multiprocessing


def get_private_ips():
    ips = []
    for iface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(iface).get(netifaces.AF_INET, [])  # IPv4
        for addr in addrs:
            ip = addr.get('addr', '')
            if IPv4Address(ip).is_private:
                ips.append(ip)
    return ips


# path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(BASE_DIR))


# bind
_bind_ips = get_private_ips()


_bind_port = '18100'


bind = [':'.join([_ip, _bind_port]) for _ip in _bind_ips]


# worker
workers = multiprocessing.cpu_count()
worker_class = 'sync'


# other
timeout = 900
keep_alive = 2
preload = True
daemon = False


# logger
accesslog = os.path.join(BASE_DIR, 'logs/access.log')
errorlog = os.path.join(BASE_DIR, 'logs/gunicorn.log')
loglevel = 'warning'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(L)s'
logger_class = 'hammer_api.utils.log_handler.RotatingGLogger'
