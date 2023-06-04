import Adafruit_BBIO.GPIO as GPIO
import http.server
import json
import os
import socketserver
import time




# Set the GPIO pin for the LED
led_pin = "P9_14"
# Set the LED pin as an output
GPIO.setup(led_pin, GPIO.OUT)


# Define the request handler
class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Get the requested file path
        file_path = '.' + (self.path if self.path != '/' else '/index.html')
        file_extension = os.path.splitext(file_path)[1]
        content_type = 'text/html'

        # Uncomment if you want to add CSS to your web page
        """
        if file_extension == '.css':
            content_type = 'text/css'
        """

        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                content = file.read()
                self.send_response(200)
                self.send_header('Content-type', content_type)
                self.end_headers()
                self.wfile.write(content)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Page not found')

    def log_message(self, format, *args):
        # Disable console logging for each request
        return


# Set up the HTTP server
server_address = ('', 8888)
httpd = socketserver.TCPServer(server_address, RequestHandler)


# Define the socket.io event handler
def handle_change_state(data):
    new_data = json.loads(data)
    print("LED =", new_data['state'])
    # Turn the LED ON or OFF
    GPIO.output(led_pin, new_data['state'])


# Start listening for connections
print("Server running ...")
httpd.serve_forever()
