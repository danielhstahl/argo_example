import json, pprint, requests, textwrap, time, os

if os.getenv("LOCAL") is not None:
    host = "localhost"
else:
    host = "172.17.0.1"  # or whatever is in your /etc/hosts when you `minikube ssh`


print("livy host is ", host)

host = f"http://{host}:8998"
data = {"kind": "spark"}
headers = {"Content-Type": "application/json"}
r = requests.post(host + "/sessions", data=json.dumps(data), headers=headers)
result = r.json()
session_url = host + r.headers["location"]
statements_url = session_url + "/statements"
# {u'state': u'starting', u'id': 0, u'kind': u'spark'}
print(result)

while result["state"] == "starting":
    r = requests.get(session_url, headers=headers)
    result = r.json()
    print(result)
    time.sleep(1)

print(result)

data = {"code": open("spark_test.scala", "r").read()}
r = requests.post(statements_url, data=json.dumps(data), headers=headers)
pprint.pprint(r.json())
result = r.json()
statement_url = host + r.headers["location"]
while result["state"] != "available":
    r = requests.get(statement_url, headers=headers)
    result = r.json()
    print(result)
    time.sleep(1)


# statement_url = host + r.headers["location"]
r = requests.get(statement_url, headers=headers)
pprint.pprint(r.json())


requests.delete(session_url, headers=headers)
# {u'id': 1,
# u'output': {u'data': {u'text/plain': u'Pi is roughly 3.14004\nNUM_SAMPLES: Int = 100000\ncount: Int = 78501'},
#             u'execution_count': 1,
#             u'status': u'ok'},
# u'state': u'available'}
