import socket

# Set default timeout for each socket to 4 seconds
socket.setdefaulttimeout(4)

# Prompt user for target's IP address
target = input("Enter target's IP address: ")

while True:
    try:
        # Create a new socket
        s = socket.socket()
        
        # Prompt user to enter port number to scan or 'exit' to exit
        port = input("Enter port to scan or 'exit' to exit: ")
        
        try:
            port = int(port)
            print(f"You have chosen port {port}")  # Debugging print
        except ValueError:
            if "exit" in port:
                break  # Exit the loop if 'exit' is entered
            else:
                print("You have to choose a number or type 'exit' to exit.")
                
        # Connect to the specified target and port
        s.connect((target, port))
        
        # Send data to the server
        s.send("Hello service\n".encode())
        
        # Receive response from the server
        recv = s.recv(10000).decode()
        
        # Split received data into lines
        recv_lines = recv.splitlines()
        
        # Iterate through each line of received data
        for line in recv_lines:
            if "Server:" in line:
                # Print the server name extracted from the response header
                print("SERVER NAME: {}".format(line.split(":")[1].strip()))  # Display only the server name
    except Exception as error:
        print(error)  # Print any encountered errors




