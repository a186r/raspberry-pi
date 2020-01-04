import RPi.GPIO as GPIO

led_pin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(100)

try:
    while True:
        duty_s = input("Please input your duty: ")
        duty = int(duty_s)
        pwm_led.ChangeDutyCycle(duty)
finally:
    GPIO.cleanup()