import json
import threading
import socket
...
arr1 = [1,2,3]
arr2 = [4,5,6]
someVar = 7
data = json.dumps({"a": arr1, "b": arr2, "c": someVar})
socket.send(data.encode())