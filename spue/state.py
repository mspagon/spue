import json
import os
import requests


def on(ip, user, light):
    body = {"on": True}
    response = requests.put(
        "{ip}/api/{user}/lights/{light}/state".format(ip=ip, user=user, light=light),
        data=json.dumps(body)
    )
    return response.json()


def off(ip, user, light):
    body = {"on": False}
    response = requests.put(
        "{ip}/api/{user}/lights/{light}/state".format(ip=ip, user=user, light=light),
        data=json.dumps(body)
    )
    return response.json()


def main():
    ip = os.getenv("HUE_IPADDRESS")
    user = os.getenv("HUE_USER")
    response = on(ip, user, 5)
    print(response)


if __name__ == '__main__':
    main()
