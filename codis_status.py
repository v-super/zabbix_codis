#!/usr/bin/env python
import os
import sys
import json
import hashlib
import urllib2

namespcae_json = os.popen('codis-admin --dashboard-list --zookeeper=codis-master.xxx.io:2181 2> /dev/null').read()
namespcae_json = json.loads(namespcae_json)
#namespace_num = len(namespcae_json)
namespace_name = sys.argv[1]
namespace_token = hashlib.sha256("Codis-XAuth-[" + namespace_name + "]").hexdigest()[0:32]

def registerUrl():
    url ="http://127.0.0.1:8080/api/topom/stats/" + namespace_token + "?forward=" + namespace_name
    data = urllib2.urlopen(url).read()
    return data

data = json.loads(registerUrl())

def qps():
    qps_sum = 0
    for value in data['proxy']['stats'].values():
        qps_sum += value['stats']['ops']['qps']
    return qps_sum

def sessions():
    sessions_sum = 0
    for value in data['proxy']['stats'].values():
        sessions_sum += value['stats']['sessions']['alive']
    return sessions_sum

def redis_mem():
    used_memory_sum = 0
    for group in data['group']['models']:
        master_server = group['servers'][0]['server']
        used_memory_sum += int(data['group']['stats'][master_server]['stats']['used_memory'])
    return used_memory_sum

def keys():
    keys_sum = 0
    for group in data['group']['models']:
        master_server = group['servers'][0]['server']
        if data['group']['stats'][master_server]['stats'].has_key('db0'):
            keys_sum += int(data['group']['stats'][master_server]['stats']['db0'].split(',')[0].split('=')[1])
    return keys_sum

def max_mem():
    max_memory_sum = 0
    for group in data['group']['models']:
        master_server = group['servers'][0]['server']
        max_memory_sum += int(data['group']['stats'][master_server]['stats']['maxmemory'])
    return max_memory_sum

FUNC_MAP = {
"qps":qps,
"sessions":sessions,
"redis_mem":redis_mem,
"keys":keys,
"max_mem":max_mem
}

print FUNC_MAP[sys.argv[2]]()
