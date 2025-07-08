# How to Increase Swap Memory on Raspberry Pi

Swap memory serves as virtual memory when a Raspberry Pi's physical RAM is insufficient, helping to prevent system crashes during memory-intensive tasks. This guide explains how to increase swap memory on any Raspberry Pi running Raspberry Pi OS, with **ZRAM** as the preferred method due to its performance and storage-friendly benefits. We’ll also cover the traditional swap file method for comparison, suitable for scenarios where ZRAM may not be ideal.

## Why Increase Swap Memory?

Raspberry Pi devices, especially those with limited RAM, can run out of memory when handling demanding applications like web servers, databases, or multitasking. Swap memory allows the system to use part of the storage (SD card, SSD, or USB drive) or compressed RAM as temporary memory. Increasing swap memory improves system stability but comes with trade-offs, such as performance impacts or storage wear, depending on the method used.

**ZRAM** is recommended for most Raspberry Pi setups because it creates a compressed swap space in RAM, offering faster performance and protecting storage devices like SD cards from excessive wear. The traditional swap file method, while simpler, is slower and can degrade SD cards due to frequent writes.

---

## Using ZRAM to Increase Swap Memory (Preferred Method)

ZRAM is a Linux kernel module that creates a compressed swap space in RAM using algorithms like LZ4 or ZSTD. It’s ideal for Raspberry Pi due to its speed (RAM-based I/O vs. slow SD card I/O) and reduced wear on storage devices. Below is a step-by-step guide to set up ZRAM using the `foundObjects/zram-swap` script, which simplifies configuration for all Raspberry Pi models.

### Prerequisites 🧰
- Raspberry Pi running Raspberry Pi OS (32-bit or 64-bit, preferably the latest version).
- SD card or storage device with sufficient free space (~10–20% of total capacity recommended).
- Internet access for package downloads.
- Terminal access (via SSH, local terminal, or keyboard/monitor).
- Backup your data before modifying system settings.
  
### Step-by-Step Installation Guide  🚀
  
### Step 1: Update the System
Ensure your Raspberry Pi OS is up to date to avoid compatibility issues.

1. Open a terminal.
2. Run:
   ```
   sudo apt update
   sudo apt full-upgrade
   sudo reboot
   ```

### Step 2: Install Git (If not avaialble on your Pi)
Install `git` to download the ZRAM script:
   ```
   sudo apt install git
   ```

### Step 3: Download and Install the ZRAM Script
Use the `foundObjects/zram-swap` script for easy ZRAM setup.

1. Clone the repository:
   ```
   git clone https://github.com/foundObjects/zram-swap
   cd zram-swap
   ```

2. Run the installation script:
   ```
   sudo ./install.sh
   ```
   - This sets up a ZRAM swap device, creates a systemd service for persistence, and prioritizes ZRAM over traditional swap.
   - Default: Allocates 50% of RAM as ZRAM swap with LZ4 compression and a swap priority of 15.

### Step 4: Configure ZRAM
Customize ZRAM settings based on your Raspberry Pi’s RAM and workload.

1. Edit the configuration file:
   ```
   sudo nano /etc/default/zram-swap
   ```

2. Adjust parameters:
   - `_zram_algorithm`: Set the compression algorithm. Use `lz4` for low CPU overhead and good speed, or `zstd` for better compression but higher CPU usage. Check available algorithms with `cat /sys/block/zram0/comp_algorithm`.
   - `_zram_size`: Set the ZRAM size in bytes or with suffixes (e.g., `512M` for 512MB, `1G` for 1GB). A common choice is 50% of total RAM (e.g., 512MB for 1GB RAM, 1GB for 2GB RAM).
   - `_zram_swap_debugging`: Set to `1` to enable debugging output for troubleshooting, or `0` to disable (recommended for normal use).
   - Example:
     ```
     _zram_algorithm=lz4
     _zram_size=512M
     _zram_swap_debugging=0
     ```
   - **Note**: The script does not support a `PRIORITY` option. It sets a default swap priority of 15, which prioritizes ZRAM over traditional swap (typically -2 or -1). This is sufficient for most setups.
   - Save and exit (Ctrl+O, Enter, Ctrl+X).

3. Apply changes:
   ```
   sudo reboot
   ```

### Step 5: Disable Traditional Swap (Optional)
To reduce wear on SD cards, disable the default swap file:

1. Stop and disable the swap service:
   ```
   sudo systemctl disable dphys-swapfile
   sudo dphys-swapfile swapoff
   ```

2. Remove the swap file:
   ```
   sudo rm /var/swap
   ```

### Step 6: Optimize Kernel Parameters
Tune the system for efficient ZRAM usage.

1. Edit `/etc/sysctl.conf`:
   ```
   sudo nano /etc/sysctl.conf
   ```

2. Add:
   ```
   vm.swappiness=80
   vm.vfs_cache_pressure=200
   vm.dirty_background_ratio=5
   vm.dirty_ratio=20
   ```
   - `swappiness=80`: Encourages moderate ZRAM usage to balance performance and memory availability.
   - Others optimize memory management for typical workloads.

3. Apply changes:
   ```
   sudo sysctl -p
   ```

### Step 7: Verify ZRAM
Confirm ZRAM is active and correctly configured.

1. Check swap status:
   ```
   cat /proc/swaps
   ```
   - Example output:
     ```
     Filename           Type       Size    Used    Priority
     /dev/zram0         partition  524288  0       15
     ```
     - `/dev/zram0` shows the configured ZRAM size (e.g., 512MB) and priority (15).

2. Check memory usage:
   ```
   free -h
   ```
   - Example:
     ```
     total  used  free  shared  buff/cache  available
     Mem:   1.9Gi 500Mi 1.0Gi 100Mi   400Mi      1.2Gi
     Swap:  512Mi 0Mi   512Mi
     ```

3. Check ZRAM details:
   ```
   zramctl
   ```
   - Shows size, algorithm (e.g., LZ4), and compression stats.

4. Reboot to ensure persistence:
   ```
   sudo reboot
   ```

---

## Traditional Swap File Method (Alternative)
The traditional swap file method uses a file on the SD card or other storage as swap space. It’s simpler but slower and can wear out SD cards, making it less ideal for frequent or performance-sensitive workloads.

### Step 1: Check Current Swap
View current swap usage:
   ```
   free -h
   ls -lh /var/swap
   ```

### Step 2: Disable Current Swap
   ```
   sudo dphys-swapfile swapoff
   sudo systemctl stop dphys-swapfile
   ```

### Step 3: Modify Swap Size
1. Edit the configuration:
   ```
   sudo nano /etc/dphys-swapfile
   ```

2. Set the size in MiB (e.g., 512 for 512MB, 1024 for 1GB):
   ```
   CONF_SWAPSIZE=512
   ```
   - Choose a size based on available storage (e.g., 512MB–2GB, ensuring ~10–20% free space remains).

3. Save and exit.

### Step 4: Regenerate and Enable Swap
   ```
   sudo dphys-swapfile setup
   sudo dphys-swapfile swapon
   sudo systemctl start dphys-swapfile
   ```

### Step 5: Verify
   ```
   free -h
   ls -lh /var/swap
   ```

---

## Why ZRAM is Preferred
ZRAM is the recommended method for increasing swap memory on Raspberry Pi due to:
- **Performance**: RAM-based swap is 100–1000x faster than SD card I/O (~10MB/s), reducing lag in demanding tasks.
- **Storage Longevity**: Eliminates writes to SD cards, which have limited write cycles.
- **Memory Efficiency**: Compression (e.g., LZ4) allows 2–3x more data in the same RAM space (e.g., 512MB ZRAM can store 1–1.5GB).
- **Suitability**: Ideal for memory-intensive or real-time applications where low latency is critical.

**Traditional Swap Drawbacks**:
- **Slow I/O**: SD card swap causes performance bottlenecks, especially in tasks requiring frequent memory access.
- **Storage Wear**: Heavy swap usage can degrade SD cards within weeks or months.
- **Latency**: Disk-based swap increases delays, unsuitable for time-sensitive workloads.

**ZRAM Trade-offs**:
- **CPU Overhead**: Compression uses CPU cycles (5–20% per core, depending on the model and algorithm), which may impact CPU-intensive tasks.
- **RAM Usage**: ZRAM reserves part of RAM, reducing available memory for applications.

---

## Best Practices and Considerations
- **ZRAM Configuration**:
  - Set `_zram_algorithm=lz4` for low CPU overhead and good speed. Use `zstd` only if CPU resources are plentiful and higher compression is needed.
  - Set `_zram_size` to 50% of RAM (e.g., 512MB for 1GB RAM, 1GB for 2GB) to balance memory and CPU usage. Adjust based on workload.
  - Set `_zram_swap_debugging=0` for normal operation; use `1` only for troubleshooting.
- **Swap Priority**: The default priority of 15 is sufficient, ensuring ZRAM is used before traditional swap (typically -2 or -1). Adjust only if using multiple swap devices with similar priorities (requires manual configuration).
- **Storage**: Avoid traditional swap on SD cards to prevent wear. Use an external SSD for traditional swap if needed.
- **Monitoring**: Use `htop` or `top` to monitor RAM, swap, and CPU usage. Adjust ZRAM size or application settings if performance is impacted.
- **Backup**: Back up your system before modifying swap settings.
- **Hybrid Approach**: Combine ZRAM (primary, priority 15) with a small SSD-based swap (e.g., 512MB, priority -2) for rare memory spikes.

---

## Troubleshooting
- **ZRAM Not Active**: Check service status (`sudo systemctl status zramswap`) and ensure the ZRAM module is loaded (`lsmod | grep zram`).
- **Incorrect Configuration**: Verify `/etc/default/zram-swap` settings (`_zram_algorithm`, `_zram_size`). Restart the service after changes (`sudo systemctl restart zramswap`).
- **High CPU Usage**: Switch to `lz4` or reduce `_zram_size`. Optimize application settings to lower memory/CPU demands.
- **OOM Errors**: Increase `_zram_size` slightly or reduce application memory usage.
- **Script Issues**: Ensure `install.sh` is executable (`sudo chmod +x install.sh`).

---

## Conclusion
For most Raspberry Pi setups, **ZRAM** is the best method to increase swap memory, offering fast performance and protection for SD cards. Configure it using the `foundObjects/zram-swap` script by setting `_zram_algorithm=lz4`, `_zram_size` to 50% of RAM (e.g., 512MB for 1GB RAM), and `_zram_swap_debugging=0` in `/etc/default/zram-swap`. The default swap priority of 15 ensures ZRAM is used first, suitable for most scenarios. Disable traditional swap on SD cards to avoid wear, and monitor performance with `htop`. The traditional swap file method is a fallback but is slower and risks storage wear. For advanced configurations, refer to the `zram-swap` GitHub repository: [https://github.com/foundObjects/zram-swap](https://github.com/foundObjects/zram-swap).