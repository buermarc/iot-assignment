import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

TriggerPIN = 17
EchoPIN = 27

GPIO.setup(TriggerPIN, GPIO.OUT)
GPIO.setup(EchoPIN, GPIO.IN)
GPIO.output(TriggerPIN, False)

try:
    while True:
        GPIO.output(TriggerPIN, True)
        time.sleep(0.1)
        GPIO.output(TriggerPIN, False)

        Timer1 = time.time()
        while GPIO.input(EchoPIN) == 0:
            Timer1 = time.time()

        while GPIO.input(EchoPIN) == 1:
            Timer2 = time.time()

        Duration = Timer2 - Timer1
        Distance = (Duration * 34300) / 2

        Distance = format((Duration * 34300) / 2, '0.2f')
        print("Distance: ", Distance, " cm")
        time.sleep(.5)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nDid cleanup")

except Exception:
    GPIO.cleanup()
