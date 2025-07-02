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

#### Step 2: Increase Swap Memory (If you have not done it already)  
When it comes to optimizing memory on your Raspberry Pi, especially for demanding tasks like running MediaPipe and OpenCV for vision applications, ZRAM is the hands-down winner. It effectively transforms the crippling I/O bottleneck of traditional SD card swap into a manageable CPU overhead, resulting in a significantly more responsive, stable, and performant system.  
  
By following the simple steps in our [Guide](https://github.com/make2explore/MediaPipe-Installation-on-RaspberryPi/blob/main/SWAP-memory.md), you can easily implement ZRAM and give your Raspberry Pi the memory boost it needs to tackle complex projects without hitting frustrating performance walls. Say goodbye to sluggishness and frequent crashes, and embrace a smoother, more efficient Raspberry Pi experience!  
[How to Increase Swap Memory on Raspberry Pi](https://github.com/make2explore/MediaPipe-Installation-on-RaspberryPi/blob/main/SWAP-memory.md)  