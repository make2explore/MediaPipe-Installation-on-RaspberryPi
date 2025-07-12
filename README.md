## How to Install MediaPipe framework on a Raspberry Pi  
  
MediaPipe is a versatile open-source framework by Google, ideal for building machine learning pipelines for tasks like hand tracking, face detection, and pose estimation. Installing it on a Raspberry Pi can be a great way to leverage its capabilities for real-time computer vision projects on a compact, low-power device. This guide walks you through the steps to set up MediaPipe on a Raspberry Pi running a compatible operating system, such as Raspberry Pi OS (based on Debian).  
  
### Prerequisites 🧰
  
Before you begin, ensure you have:  

- A Raspberry Pi (preferably 4 or latest varient for better performance). with Raspberry Pi OS (64-bit) installed.  
   Raspberry Pi 4 or 5 is highly recommended for better performance. While older models (like Pi 3) might work for simpler tasks, they will likely struggle with real-time applications.  
   - ✅ We have tested this with Raspberry Pi 4 Model B Rev 1.1  
   - with Raspberry Pi OS (64-bit) Debian version: 12 (bookworm)  
   - 32-bit OS did not worked for us when we tested it.  
   <p align="center">
   <img src="/Images/m2e-Rpi4-MP.png" width="450" height="350">  
   </p>

   <p align="center">
   <img src="/Images/m2e-Rpi4-OS.png" width="450" height="350">
   </p>
    
- At least 10GB of free storage (preferably on a microSD card or external drive). MediaPipe and its dependencies can take up a fair amount of space, so ensure your SD card has enough free storage.  
- A USB webcam or Raspberry Pi Camera Module (We use Logitech C270 USB Webcam)  
  
-----------------------------------------------------------------------------------------------------------------------------------------
  
### Step-by-Step Installation Guide 🚀  
  
#### Step 1: Update Your System  
Open the terminal and ensure your Pi is up to date:  
```
sudo apt update && sudo apt upgrade -y
```

#### Step 2: Increase Swap Memory (Optional)  
- When it comes to optimizing memory on your Raspberry Pi, especially for demanding tasks like running MediaPipe and OpenCV for vision applications, ZRAM is the hands-down winner. It effectively transforms the crippling I/O bottleneck of traditional SD card swap into a manageable CPU overhead, resulting in a significantly more responsive, stable, and performant system.  
  
- By following the simple steps in our [Guide](https://github.com/make2explore/MediaPipe-Installation-on-RaspberryPi/tree/main/Enlarge-Swap), you can easily implement ZRAM and give your Raspberry Pi the memory boost it needs to tackle complex projects without hitting frustrating performance walls. Say goodbye to sluggishness and frequent crashes, and embrace a smoother, more efficient Raspberry Pi experience!  
[How to Increase Swap Memory on Raspberry Pi](https://github.com/make2explore/MediaPipe-Installation-on-RaspberryPi/tree/main/Enlarge-Swap)  
  
- If you have Raspberry Pi 4/5 with more than 4GB's of RAM, You might not need to increase the swap memory.  
- ✅ We have tested it with default setup. 2GB RAM and 512MB of default (SD card) Swap space
  
#### Step 3: Preparing Virtual Environment (Recommended)  
We’ll install the MediaPipe framework package in a virtual environment. Creating a virtual environment will isolate the Python libraries we’re using, in this case, the MediaPipe and OpenCV library, from the rest of the system. We’ll create our virtual environment on a directory on our Desktop. Enter the following command on a Terminal window to move to the Desktop. Run follwoing command in new terminal to change the directory and Enter into our Projects folder:  
Run the next command in your terminal to check Python version 3.X:  
   ```
   python --version
   ```
   
Install pip3 and Python 3 Virtual environment:  
   ```
   sudo apt install -y python3-pip python3-virtualenv
   ```
Go to Desktop -  
   ```
   cd ~/Desktop
   ```
Create a folder for your project. This is where we’ll create the virtual environment and install the library. We’ll create a folder called projects.
   ```
   mkdir projects
   ```
Enter into that newly created folder:  
   ```
   cd ~/Desktop/projects
   ```
Create a virtual environment for this directory called `myenv`. This must be the same directory where we’ll install the OpenCV library. Replace `myenv` with the desired name for your virtual environment.  
   ```
   python3 -m venv projects-env
   ```
Then, you can run the following `ls` command to check that the virtual environment is there.  
   ```
   ls -l
   ```
Then next step is to Activate the virtual environment:  
   ```
   source projects-env/bin/activate
   ```
Your terminal prompt should change following to indicate that you are now in the virtual environment.
  
### Step 4: Installing the MediaPipe Library  
Now that we are in our virtual environment, we can install the MediaPipe library. Run the following command:  
   ```
   pip3 install mediapipe
   ```

It will take time. so have a patience and wait for the command to complete.  
  
### Step 5: Testing Mediapipe installation  
Now to ensure that MediaPipe has been installed successfully. In your terminal window, open Python prompt:  
   ```
   python
   ```
Then, in the Python prompt, import the OpenCV library.  
   ```
   import mediapipe
   ```
If all goes well, you will see mediapipe get successfully imported. Now you can download and run the codes given in [this](https://github.com/make2explore/MediaPipe-Installation-on-RaspberryPi/tree/main/Codes) repository.  
  
----------------------------------------------------------------------------------------------------------------  
  
  
## MediaPipe examples with Raspberry Pi

This example uses [MediaPipe](https://github.com/google/mediapipe) with Python on
a Raspberry Pi to perform real-time gesture recognition using images
streamed from the camera.  

### Download the repository

First, clone this Git repo onto your Raspberry Pi.  
```
git clone https://github.com/make2explore/MediaPipe-Installation-on-RaspberryPi.git
```

Go to codes folder
```
cd MediaPipe-Installation-on-RaspberryPi/Codes/
```  
### Run the example (Hand Landmarks)  
```
python3 landmarks.py
```

### Run the example (Gesture)
```
python3 gesture.py
```
*   You can optionally specify the `model` parameter to set the task file to be used:
    *   The default value is `gesture_recognizer.task`
    *   TensorFlow Lite gesture recognizer models **with metadata**  
        * Models from [MediaPipe Models](https://developers.google.com/mediapipe/solutions/vision/gesture_recognizer#models)
        * Custom models trained with [MediaPipe Model Maker](https://developers.google.com/mediapipe/solutions/vision/gesture_recognizer#custom_models) are supported.
*   You can optionally specify the `numHands` parameter to the maximum 
    number of hands that can be detected by the recognizer:
    *   Supported value: A positive integer (1-2)
    *   Default value: `1`
*   You can optionally specify the `minHandDetectionConfidence` parameter to adjust the
    minimum confidence score for hand detection to be considered successful:
    *   Supported value: A floating-point number.
    *   Default value: `0.5`
*   You can optionally specify the `minHandPresenceConfidence` parameter to adjust the 
    minimum confidence score of hand presence score in the hand landmark detection:
    *   Supported value: A floating-point number.
    *   Default value: `0.5`
*   You can optionally specify the `minTrackingConfidence` parameter to adjust the 
    minimum confidence score for the hand tracking to be considered successful:
    *   Supported value: A floating-point number.
    *   Default value: `0.5`
*   Example usage:
    ```
    python3 recognize.py \
      --model gesture_recognizer.task \
      --numHands 2 \
      --minHandDetectionConfidence 0.5
    ```