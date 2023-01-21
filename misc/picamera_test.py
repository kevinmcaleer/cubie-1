from picamera2 import Picamera2, Preview
from libcamera import controls
import time

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
while True:
    picam2.start_preview(Preview.QTGL)
    picam2.start()
    picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})
    success = picam2.autofocus_cycle()
    print(f'Autofocus is {success}')
    job = picam2.autofocus_cycle(wait=False)

    success = picam2.wait(job)
time.sleep(2)
picam2.capture_file("test.jpg")

