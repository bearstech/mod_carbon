import time
from socket import socket
import collectd
sock = None

CARBON_SERVER = '127.0.0.1'
CARBON_PORT = 2003

def config(conf):
    collectd.debug('Configuring Stuff')

def init():
    collectd.debug('initing stuff')
    global sock
    sock = socket()
    try:
        sock.connect((CARBON_SERVER,CARBON_PORT))
    except:
        collectd.warn("Couldn't connect to %(server)s on port %(port)d, is carbon-agent.py running?" % { 'server':CARBON_SERVER, 'port':CARBON_PORT })

def shutdown():
    global sock
    sock.close()

def write(vl, datas=None):
    now = int(time.time())
    global sock
    lines = []
    for i in vl.values:
        stuff = [vl.host, vl.plugin, vl.type]
        if vl.plugin_instance != "":
            stuff.append(vl.plugin_instance)
        stuff.append(vl.type)
        lines.append("%s %s %d" % (".".join(stuff), i, now))
    message = '\n'.join(lines) + '\n' #all lines must end in a newline
    collectd.info(message)
    sock.sendall(message)

collectd.register_config(config)
collectd.register_init(init)
collectd.register_shutdown(shutdown)
collectd.register_write(write)
