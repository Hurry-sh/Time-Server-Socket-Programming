import socket
import ssl

host = "127.0.0.1"
# host = "172.20.10.4"

server_address = (host, 9999)

context = ssl.create_default_context()

# The given 2 statements here were added because the program would not run otherwise. 
# This is due to Certificate_Not_Verified error.
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

with socket.create_connection(server_address) as client_socket:
    with context.wrap_socket(client_socket, server_hostname=host) as ssock:
        try:
            location_prompt = ssock.recv(1024).decode()
            print(location_prompt, end='')
            location = input()
            ssock.sendall(location.encode())

            while True:
                time_prompt = ssock.recv(1024).decode()
                print(time_prompt, end='')
                display_time = input().upper()
                ssock.sendall(display_time.encode())

                if display_time == 'Y':
                    for _ in range(10):
                        time_response = ssock.recv(1024).decode()
                        print(time_response)
                else:
                    break
        finally:
            ssock.close()



