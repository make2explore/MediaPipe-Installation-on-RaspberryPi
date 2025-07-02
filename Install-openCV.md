# How to Install OpenCV on Raspberry Pi  
  
OpenCV **(Open Source Computer Vision Library)** is a powerful tool for computer vision projects, and installing it on a Raspberry Pi allows you to create exciting applications like image processing, object detection, and more. This guide walks you through the steps to install OpenCV on a Raspberry Pi running Raspberry Pi OS (based on Debian). The process is optimized for simplicity and compatibility with Raspberry Pi 4, but it works on other models like Raspberry Pi 3 with minor adjustments.  
  
## Prerequisites 🧰
- Raspberry Pi running Raspberry Pi OS (32-bit or 64-bit, preferably the latest version).
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
  
By following the simple steps in our [Guide](https://github.com/make2explore/MediaPipe-Installation-on-RaspberryPi/blob/main/SWAP-memory.md), you can easily implement ZRAM and give your Raspberry Pi the memory boost it needs to tackle complex projects without hitting frustrating performance walls. Say goodbye to sluggishness and frequent crashes, and embrace a smoother, more efficient Raspberry Pi experience!  
[How to Increase Swap Memory on Raspberry Pi](https://github.com/make2explore/MediaPipe-Installation-on-RaspberryPi/blob/main/SWAP-memory.md)  
  
### Step 3: Installing OpenCV on Raspberry Pi with pip on Virtual Environment (Recommended)  
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
Create a virtual environment for this directory called ==myenv==. This must be the same directory where we’ll install the OpenCV library. Replace ==myenv== with the desired name for your virtual environment.