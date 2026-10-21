import sys
import urllib.request

if len(sys.argv) < 2:
    print("Error: Provide the server URL.")
    sys.exit(1)

server_url = sys.argv[1]

if not sys.stdin.isatty():
    message_text = sys.stdin.read().encode('utf-8')
    req = urllib.request.Request(server_url, data=message_text)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))

else:
    with urllib.request.urlopen(server_url) as response:
        print(response.read().decode('utf-8'))
