from flask import Flask, render_template
import Adafruit_BBIO.GPIO as GPIO
import os

app = Flask(__name__)

# Set the GPIO pin for the LED
led_pin = "P9_14"
# Set the LED pin as an output
GPIO.setup(led_pin, GPIO.OUT)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/toggle_led/<state>')
def toggle_led(state):
    if state == 'on':
        GPIO.output(led_pin, GPIO.HIGH)
    elif state == 'off':
        GPIO.output(led_pin, GPIO.LOW)
    return state


# Get the current working directory
current_directory = os.getcwd()

# Print the current working directory
print("Current Working Directory:", current_directory)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
