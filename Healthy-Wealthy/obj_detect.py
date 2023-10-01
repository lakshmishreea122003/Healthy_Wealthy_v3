from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import av
import cv2
import torch
from PIL import Image


# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

class VideoProcessor:
    def recv(self, frame):
        frm = frame.to_ndarray(format="bgr24")

        # Convert the frame to RGB format (required by YOLOv5)
        frm_rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)

        # Perform object detection using YOLOv5
        results = model(frm_rgb)

        # Process the results
        for result in results.pred:
            for det in result:
                x, y, w, h, conf, cls = det.tolist()
                cv2.rectangle(frm, (int(x), int(y)), (int(x+w), int(y+h)), (0, 255, 0), 3)
                label = model.names[int(cls)]
                cv2.putText(frm, label, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        return av.VideoFrame.from_ndarray(frm, format='bgr24')
