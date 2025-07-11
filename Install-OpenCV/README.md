# How to Install OpenCV on Raspberry Pi  
  
OpenCV **(Open Source Computer Vision Library)** is a powerful tool for computer vision projects, and installing it on a Raspberry Pi allows you to create exciting applications like image processing, object detection, and more. This guide walks you through the steps to install OpenCV on a Raspberry Pi running Raspberry Pi OS (based on Debian). The process is optimized for simplicity and compatibility with Raspberry Pi 4, but it works on other models like Raspberry Pi 3 with minor adjustments.  
  
## Prerequisites 🧰
- Raspberry Pi 4 running Raspberry Pi OS (64-bit, preferably the latest version).
- SD card or storage device with sufficient free space (at least 16GB capacity recommended).
- Internet access for package downloads.
- Terminal access (via SSH, local terminal, or keyboard/monitor).
- Backup your data before modifying system settings.  
  
## Step-by-Step Installation Guide  🚀  
  
### Step 1: Update Your Raspberry Pi
Ensure your Raspberry Pi OS is up to date to avoid compatibility issues.

1. Open a terminal.
2. Run:
   ```
   sudo apt update
   sudo apt upgrade
   sudo reboot
   ```

### Step 2: Increase Swap Memory (If you have not done it already)  
When it comes to optimizing memory on your Raspberry Pi, especially for demanding tasks like running MediaPipe and OpenCV for vision applications, ZRAM is the hands-down winner. It effectively transforms the crippling I/O bottleneck of traditional SD card swap into a manageable CPU overhead, resulting in a significantly more responsive, stable, and performant system.  
  
By following the simple steps in our [Guide](https://github.com/make2explore/MediaPipe-Installation-on-RaspberryPi/tree/main/Enlarge-Swap), you can easily implement ZRAM and give your Raspberry Pi the memory boost it needs to tackle complex projects without hitting frustrating performance walls. Say goodbye to sluggishness and frequent crashes, and embrace a smoother, more efficient Raspberry Pi experience!  
[How to Increase Swap Memory on Raspberry Pi](https://github.com/make2explore/MediaPipe-Installation-on-RaspberryPi/tree/main/Enlarge-Swap)  
  
### Step 3: Installing and Preparing Virtual Environment (Recommended)  
Run the next command in your terminal to check Python version 3.X:  
   ```
   python --version
   ```
   
Install pip3 and Python 3 Virtual environment:  
   ```
   sudo apt install -y python3-pip python3-virtualenv
   ```
Create a Virtual Environment - We’ll install the OpenCV library in a virtual environment. Creating a virtual environment will isolate the Python libraries we’re using, in this case, the OpenCV library, from the rest of the system. We’ll create our virtual environment on a directory on our Desktop. Enter the following command on a Terminal window to move to the Desktop. Run follwoing command to change the directory
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
  
### Step 4: Installing the OpenCV Library (Option 1 - Using Pip)
So we will see **two methods of Installing OpenCV in Raspberry Pi**. First is using ***Pip Python package manager*** and other method is ***apt package manager***. Lets see first pip method. Now that we are in our virtual environment, we can install the OpenCV library. Run the following command:  
   ```
   pip3 install opencv-contrib-python
   ```
It will take time. so have a patience and wait for the command to complete.
  
### Installing OpenCV on Raspberry Pi with apt (Option 2 - Using apt)  
First we have to install some prerequisites, So run the next command to install all the required dependencies.  
   ```
   sudo apt install -y build-essential cmake pkg-config libjpeg-dev libtiff5-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5 python3-dev
   ```
Once above installation get complete, run next command to install openCV
   ```
   sudo apt install -y python3-opencv
   ```
This command can take time, so have patience and wait for the command to complete.
  
### Step 5: Testing OpenCV apt Installation  
Now to ensure that OpenCV has been installed successfully. In your terminal window, open Python prompt:  
   ```
   python
   ```
Then, in the Python prompt, import the OpenCV library.  
   ```
   import cv2
   ```
And finally, type the next command to check the OpenCV version that you installed. (Note there are two underscores before and after word version)  
   ```
   cv2.__version__
   ```
If everything has been done properly, it should return your OpenCV version.