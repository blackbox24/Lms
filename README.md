# Library Management System

## STEPS IN BUILDING THE APP
- [x] create a virtual environment and active it.
- [x] install `flask`
- [X] create requirements.txt file for packages
- [X] create a folder for APIs  `library`
- [X] use fake data
- [X] create automated tests
- [X] submit project

### How to run the project

- Windows
    - Create a virtual env. Open command prompt terminal or powershell terminal
        - Run `py -m venv flask-env` and hit enter
    - Change directory into the scripts directory in the virtual environment
        - Run `cd flask-env && cd Scripts`
    - Activate the virtual environment
        - Run `activate.bat` and hit enter in command prompt or `activate.ps1` in powershell
    - Move outside the virtual environment
        - Run `cd .. && cd ..` and hit enter
    - clone the repo from git into your current directory
        - In the command prompt or powershell terminal paste the following `git clone https://github.com/blackbox24/Lms.git ` and hit enter
    - Change directory into the project folder (library) and Run `py install -r requirements.txt` in your terminal to install necessary packages
    - Run `py api.py` in your terminal  to run server
    - Also to run test type `pytest tests/` in your terminal

- MacOS
    - Install Python and Pip
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```
    - Create a Virtual Environment
    ```bash
    sudo apt install python3-venv
    python3 -m venv myprojectenv
    source myprojectenv/bin/activate
    ```
    - Install Packages
    ```bash
    pip install -r requirements.txt
    ```
    - clone the repo from git into your current directory
        - In the terminal paste the following `git clone https://github.com/blackbox24/Lms.git ` and hit enter
    - Change directory into the project folder (library) and Run `python3 api.py` in your terminal.
    - Also to run test type `pytest tests/` in your terminal
