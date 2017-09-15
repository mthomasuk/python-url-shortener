import requests
import json

if __name__ == "__main__":
    host_address = "http://localhost:8000"

    # Basic test, should return 404
    base = requests.get(host_address + "/")

    if base.status_code != 404:
        print("[ERROR] no 404 when calling / got back HTTP response code: " +
              str(base.status_code))

    elif base.headers['content-type'] != 'application/json':
        print("[ERROR] when calling / got back non JSON data: " +
              base.headers['content-type'])

    else:
        print("[SUCCESS] when calling /")

    # Bit more advanced, should still return 404
    base = requests.get(host_address + "/3267e22b-02ff-4078-8700-7b6cf741f2b3")

    if base.status_code != 404:
        print("[ERROR] no 404 when calling / got back HTTP response code: " +
              str(base.status_code))

    elif base.headers['content-type'] != 'application/json':
        print("[ERROR] when calling / got back non JSON data: " +
              base.headers['content-type'])

    else:
        print("[SUCCESS] when calling /")

    # Even more advanced, should succeed and return JSON data
    base = requests.post(
        host_address + 
        "/3267e22b-02ff-4078-8700-7b6cf741f2b3", 
        '{"url":"http://www.google.com"}'
    )
    key = base.json()["shortened_url"].split("/")[3]

    if base.status_code != 201:
        print("[ERROR] when calling / got back HTTP response code: " +
              str(base.status_code))

    elif base.headers['content-type'] != 'application/json':
        print("[ERROR] when calling / got back non JSON data: " +
              base.headers['content-type'])

    else:
        print("[SUCCESS] when calling /")

    # Super advanced, should return a redirect
    base = requests.get(host_address + "/" + key)

    if base.status_code != 301:
        print("[ERROR] no 301 when calling / got back HTTP response code: " +
              str(base.status_code))

    elif base.headers['content-type'] != 'application/json':
        print("[ERROR] when calling / got back non JSON data: " +
              base.headers['content-type'])

    else:
        print("[SUCCESS] when calling /")
