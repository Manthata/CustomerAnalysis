#!/usr/bin/env python
import time 
import argparse
import socketio
import cv2
import base64
import os
from importlib import import_module
# from imutils.video import FPS
# from imutils.video import FPS




"""
Use object detection to detect objects in the frame in realtime. The
types of objects detected can be changed by selecting different models.
To change the computer vision model, follow this guide:
https://dashboard.alwaysai.co/docs/application_development/changing_the_model.html
To change the engine and accelerator, follow this guide:
https://dashboard.alwaysai.co/docs/application_development/changing_the_engine_and_accelerator.html
"""

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
    print("Load module {}".format('camera_' + os.environ['CAMERA']))
else:
    from camera import Camera

# instanctiate the socket client class
sio = socketio.Client(reconnection=True, reconnection_attempts=5, reconnection_delay=3,
                      reconnection_delay_max=5, randomization_factor=0.5, logger=True, binary=False, json=None)

@sio.event
def connect():
    print()
    print("[INFO]client wants to connect")
    print("[INFO] successfully connected to the server")


#create an error handle if connection to the server failed 
@sio.event
def connect_error(err):
    print("[INFO] failed to connect to the server {}".format(err))

#create a handler for when disconnecting to the server 


@sio.event
def disconnect():
    # mainstreamer.close()

    print("[INFO] disconnected from the serever")

@sio.event
def reconnect():
    recob = {
        "server-addr": "https://localhost:3000",
        "stream-fps": "20"
    }
    main(recob["server-addr"], recob["stream-fps"])
    


# Create the class for the cv client  
class CVClient(object):
    def __init__(self, server_addr, stream_fps):
        self.server_addr = server_addr
        self.server_port = 5001
        self._stream_fps = stream_fps
        self._last_update_t = time.time()
        self._wait = (1/self._stream_fps)

    # the setup function 
    def setup(self): 
        print("[INFO] connecting to the server {}....".format(self.server_addr))
        #connect to the server
        print("{}".format(self.server_addr))
        # sio.connect(
        #     "{}".format(self.server_addr),
        #     transports=["websocket"],
        #     namespaces=["/cv"]
        #     )
        
        sio.connect(
            "{}".format(self.server_addr),
            namespaces="/cv", transports="websocket"
        )
        print("we have connected maybe?")
        
        time.sleep(2)
        return self
    
    #create a function to convert image to jpeg
    def _conver_image_to_jpeg(self, image):
        # Encode frame as jpeg
        # frame = cv2.imencode(".jpg", image)[1].tobytes()

        # Encode frame in base 64 and remove utf8 encoding 
        
        # frame = base64.b64decode(image)
        
        # frame = base64.b64decode(image)
        return "data:image/jpeg;base64,{}".format(image)

    
    #send the data to the server 
    def send_data(self, frame, text):
        cur_time = time.time()
        if cur_time - self._last_update_t > self._wait:
            self._last_update_t = cur_time
            # w = 649
            # h = 480
            # dim = (w, h)
            # frame = cv2.resize(frame, dim)
           
            sio.emit("cv2server", 
                {
                    "image":self._conver_image_to_jpeg(frame),
                    "text": text
                }, namespace="/cv"
            )
            # sio.emit("data", { "image": self._conver_image_to_jpeg(frame)}, namespace="/cv" )
    
    def check_exist(self):
        pass
    def close(self):
        sio.disconnect()
  

#-------------------------------------------------------------------------------------------------------------------------------------
# create the main module 
def main(server_addr, stream_fps):
  
    # print("loaded model:\n{}\n".format(obj_detect.model_id))
    # print("Engine: {}".format(obj_detect.engine))
    # print("Accelerator: {}\n".format(obj_detect.accelerator))
    # print("Labels:\n{}\n".format(obj_detect.labels))
    

    try:

        streamer = CVClient(server_addr, stream_fps).setup()

        


        
        # loop detection 
        while True: 
            text = "Frame_count: {}".format(stream_fps)
            frame = Camera().get_frame()
          
            # results = obj_detect.detect_objects(frame, confidence_level = .5)
            # frame = edgeiq.markup_image(
            #     frame, results.predictions, colors = obj_detect.colors
            # )
            # Generate a text to display 
            # text= ["Model: {}".format(obj_detect.model_id)]
            # text.append(
            #         "Inference time: {:1.3f} s".format(results.duration
            #         ))
            # text.append("Objects:")

            # for prediction in results.predictions:
            #     text.append("{}: {:2.2f}%".format(
            #         prediction.label, prediction.confidence * 100))

            streamer.send_data(frame, text)

            if streamer.check_exist():
                break
           
    finally:
        if streamer is not None:
            streamer.close()

        # print("elapsed time: {:.2f}".format(fps.get_elapsed_seconds()))
        # print("approx. FPS: {:.2f}".format(fps.compute_fps()))

        print("Program Ending")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='I have nothing to say really')
    # parser.add_argument(
    #         '--camera', type=int, default='0',
    #         help='The camera index to stream from.')
    parser.add_argument(
            '--server-addr',  type=str, default='localhost:5000',
            help='The IP address or hostname of the SocketIO server.')
    parser.add_argument(
            '--stream-fps',  type=float, default=20.0,
            help='The rate to send frames to the server.')
    args = parser.parse_args()
    main( args.server_addr, args.stream_fps)




