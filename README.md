## How to Install MediaPipe framework on a Raspberry Pi  
  
MediaPipe is a versatile open-source framework by Google, ideal for building machine learning pipelines for tasks like hand tracking, face detection, and pose estimation. Installing it on a Raspberry Pi can be a great way to leverage its capabilities for real-time computer vision projects on a compact, low-power device. This guide walks you through the steps to set up MediaPipe on a Raspberry Pi running a compatible operating system, such as Raspberry Pi OS (based on Debian).  
  
### Prerequisites 🧰
  
Before you begin, ensure you have:  

- A Raspberry Pi (preferably 4 or latest varient for better performance). with Raspberry Pi OS (32-bit or 64-bit) installed. A Raspberry Pi 4 or 5 is highly recommended for better performance. While older models (like Pi 3) might work for simpler tasks, they will likely struggle with real-time applications.  
- An active internet connection.  
- A terminal or SSH access to your Raspberry Pi.  
- At least 10GB of free storage (preferably on a microSD card or external drive). MediaPipe and its dependencies can take up a fair amount of space, so ensure your SD card has enough free storage.  
- A USB webcam or Raspberry Pi Camera Module (optional, for testing MediaPipe applications).  
  
### Step-by-Step Installation Guide 🚀  
  
#### Step 1: Update Your System  
Open the terminal and ensure your Pi is up to date:  
```
sudo apt update && sudo apt upgrade -y
```

#### Step 2: Increase Swap Memory  
When it comes to optimizing memory on your Raspberry Pi, especially for demanding tasks like running MediaPipe and OpenCV for vision applications, ZRAM is the hands-down winner. It effectively transforms the crippling I/O bottleneck of traditional SD card swap into a manageable CPU overhead, resulting in a significantly more responsive, stable, and performant system.  
  
By following the simple steps in our [Guide](https://github.com/make2explore/MediaPipe-Installation-on-RaspberryPi/tree/main/Enlarge-Swap), you can easily implement ZRAM and give your Raspberry Pi the memory boost it needs to tackle complex projects without hitting frustrating performance walls. Say goodbye to sluggishness and frequent crashes, and embrace a smoother, more efficient Raspberry Pi experience!  
[How to Increase Swap Memory on Raspberry Pi](https://github.com/make2explore/MediaPipe-Installation-on-RaspberryPi/tree/main/Enlarge-Swap)  
  

#### Step 3: Install OpenCV  
You should have OpenCV installed on your Raspberry Pi. If not, you can follow our [guide](https://github.com/make2explore/MediaPipe-Installation-on-RaspberryPi/tree/main/Install-OpenCV) to install it  
[How to Install OpenCV on Raspberry Pi](https://github.com/make2explore/MediaPipe-Installation-on-RaspberryPi/tree/main/Install-OpenCV)  
  
### Step 4: Preparing Virtual Environment (Recommended)  
So, if you followed our previous step of installing openCV, you must have installed virtual environmnet for your projects. Now we have to activate it. We’ll install the MediaPipe framework package in a virtual environment. Creating a virtual environment will isolate the Python libraries we’re using, in this case, the MediaPipe and OpenCV library, from the rest of the system. We’ll create our virtual environment on a directory on our Desktop. Enter the following command on a Terminal window to move to the Desktop. Run follwoing command in new terminal to change the directory and Enter into our Projects folder:  
   ```
   cd ~/Desktop/projects
   ```
Then next step is to Activate the virtual environment:  
   ```
   source projects-env/bin/activate
   ```
Your terminal prompt should change to indicate that you are now in the virtual environment.  
  
### Step 5: Installing the MediaPipe Library  
Now that we are in our virtual environment, we can install the MediaPipe library. Run the following command:  
   ```
   pip3 install mediapipe
   ```

It will take time. so have a patience and wait for the command to complete.