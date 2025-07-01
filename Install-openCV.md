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