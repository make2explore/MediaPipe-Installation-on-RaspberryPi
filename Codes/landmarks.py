# Copyright 2023 The MediaPipe Authors. All Rights Reserved. Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at# http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.# Main scripts to run gesture recognition.
# main script to run Hand Handmarks detection
import argparse
import sys
import time
import cv2
import mediapipe as mp # Crucial: Import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Global variables to calculate FPS
COUNTER, FPS = 0, 0
START_TIME = time.time()

def run(model: str, num_hands: int,
        min_hand_detection_confidence: float,
        min_hand_presence_confidence: float, min_tracking_confidence: float,
        camera_id: int, width: int, height: int) -> None:
  """Continuously run inference on images acquired from the camera.

  Args:
      model: Name of the gesture recognition model bundle.
      num_hands: Max number of hands can be detected by the recognizer.
      min_hand_detection_confidence: The minimum confidence score for hand
        detection to be considered successful.
      min_hand_presence_confidence: The minimum confidence score of hand
        presence score in the hand landmark detection.
      min_tracking_confidence: The minimum confidence score for the hand
        tracking to be considered successful.
      camera_id: The camera id to be passed to OpenCV.
      width: The width of the frame captured from the camera.
      height: The height of the frame captured from the camera.
  """

  # Start capturing video input from the camera
  cap = cv2.VideoCapture(camera_id)
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

  # Visualization parameters
  row_size = 50  # pixels
  left_margin = 24  # pixels
  text_color = (0, 0, 0)  # black
  font_size = 1
  font_thickness = 1
  fps_avg_frame_count = 10

  # Initialize the MediaPipe Hands solution
  with mp_hands.Hands(
      model_complexity=1,
      min_detection_confidence=min_hand_detection_confidence,
      min_tracking_confidence=min_tracking_confidence) as hands:

    # Continuously capture images from the camera and run inference
    while cap.isOpened():
      success, image = cap.read()
      if not success:
        sys.exit(
            'ERROR: Unable to read from webcam. Please verify your webcam settings.'
        )

      image = cv2.flip(image, 1)

      # Convert the image from BGR to RGB
      rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

      # Process the image with MediaPipe Hands.
      results = hands.process(rgb_image)

      # Show the FPS
      global FPS, COUNTER, START_TIME
      if COUNTER % fps_avg_frame_count == 0:
          FPS = fps_avg_frame_count / (time.time() - START_TIME)
          START_TIME = time.time()
      COUNTER += 1

      fps_text = 'FPS = {:.1f}'.format(FPS)
      text_location = (left_margin, row_size)
      current_frame = image
      cv2.putText(current_frame, fps_text, text_location, cv2.FONT_HERSHEY_DUPLEX,
                  font_size, text_color, font_thickness, cv2.LINE_AA)

      # Draw hand landmarks if detected
      if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
          mp_drawing.draw_landmarks(
              current_frame,
              hand_landmarks,
              mp_hands.HAND_CONNECTIONS,
              mp_drawing_styles.get_default_hand_landmarks_style(),
              mp_drawing_styles.get_default_hand_connections_style())

      cv2.imshow('Hand Landmarks', current_frame) # Changed window name

      # Stop the program if the ESC key is pressed.
      if cv2.waitKey(1) == 27:
          break

  cap.release()
  cv2.destroyAllWindows()

def main():
  parser = argparse.ArgumentParser(
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument(
      '--model',
      help='Name of gesture recognition model.',
      required=False,
      default='gesture_recognizer.task')
  parser.add_argument(
      '--numHands',
      help='Max number of hands that can be detected by the recognizer.',
      required=False,
      default=1)
  parser.add_argument(
      '--minHandDetectionConfidence',
      help='The minimum confidence score for hand detection to be considered '
           'successful.',
      required=False,
      default=0.5)
  parser.add_argument(
      '--minHandPresenceConfidence',
      help='The minimum confidence score of hand presence score in the hand '
           'landmark detection.',
      required=False,
      default=0.5)
  parser.add_argument(
      '--minTrackingConfidence',
      help='The minimum confidence score for the hand tracking to be '
           'considered successful.',
      required=False,
      default=0.5)
  parser.add_argument(
      '--cameraId', help='Id of camera.', required=False, default=0)
  parser.add_argument(
      '--frameWidth',
      help='Width of frame to capture from camera.',
      required=False,
      default=640)
  parser.add_argument(
      '--frameHeight',
      help='Height of frame to capture from camera.',
      required=False,
      default=480)
  args = parser.parse_args()

  run(args.model, int(args.numHands), args.minHandDetectionConfidence,
      args.minHandPresenceConfidence, args.minTrackingConfidence,
      int(args.cameraId), args.frameWidth, args.frameHeight)

if __name__ == '__main__':
  main()