# Huawei Router Python Configuration

This Python script automates the configuration of Huawei routers (works for models AX2, AX2S, and AX3) using Selenium. It sets up the Wi-Fi network SSID, passwords and remote access settings.


## Requirements

* Python and the necessary packages installed (use `pip install [...]` to install them)
* You must have one of the router LAN ports connected to the computer
 * Ensure to replace placeholders like `YOUR_PORT` or `SELECTED_IP`  with appropriate values in the script.

## Tips

* The URL asked at the beggining of the code is the router default IP adress (usually http://192.168.31)
  * If you don't know the correct adress just use `ipconfig` command at your cmd

* Issues with the 'chromedriver.exe' file are probably related with its version, you can search for different versions at https://googlechromelabs.github.io/chrome-for-testing/

### Warning: Automating router configurations can potentially disrupt your network if not done correctly. Ensure you understand the script and its implications before running it!

