This Python script uses the psutil library to gather system and process information. It performs three primary functions:

1. Listing Recently Installed and Uninstalled Programs
2. Listing Running Processes and Their Uptime
3. Listing Open Files and Folders

The project is primarily aimed at monitoring and retrieving key system information, such as installed software, running processes, and open files on a Windows system.

Requirements

To run this project you need to install the following Python library:
psutil: A cross-platform library for accessing system and process information.
Before running the script, you can install psutil using the following command: pip install psutil

Features
This script provides three key functionalities:

1. Listing Recently Installed and Uninstalled Programs
This function retrieves a list of installed programs on a Windows machine by querying the Windows Registry. It specifically accesses the key HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall, where details about installed applications are stored.

2. Listing Running Processes and Their Uptime
The script fetches a list of currently running processes on the system, displaying the process name, Process ID (PID), and how long each process has been running since its creation time. The uptime is calculated by comparing the process's creation time with the current time.

3. Listing Open Files and Folders
This functionality queries each running process to retrieve a list of files that the process has opened, including documents, executables, and system files. This is useful for understanding which files are currently being accessed on your system.

How to Run
To run the script, simply execute the Python file in your terminal or IDE: python system_info.py

Ensure that you have psutil installed, and the script will output the relevant information about installed programs, running processes, and open files.

Notes
Windows Only: This script is currently designed to work only on Windows operating systems.
Permissions: Some processes or files may require elevated permissions to access. You may encounter access-related errors for certain system processes or files.
Psutil Library: psutil is a powerful library for system and process information retrieval. Be aware that querying system processes and files can return a large amount of data.
