# Plane Mail Management Initial Documentation

### Onboarding Instructions for Testing on Windows

1. Go to "Turn Windows features on or off" in the control panel

2. Enable "Windows Subsystem for Linux" checkbox. You may have to restart your computer for changes to take effect

3. Install Ubuntu (It's on Microsoft Store).

4. Choose a location and create a folder to store the content for Plane Mail. You can use cd ~ to create the folder in a separate file system from your local drive.

5. Install python 3 and pip if you have not already done so. You can run "sudo apt update" and "sudo apt install python3-pip"

6. Create a virtual environment by running: "python3 -m venv {name}"

7. Activate environment by running: "source {name}/bin/activate"

8. Git clone the repository in the environment you have created (git clone https://github.com/ScottyLabs/plane.git). Move into the new branch you are editing on.

9. Install requirement files by running: "python3 -m pip install -r requirements.txt"

10. cd into the "plane" folder and transfer the file secrets.py into the "plane" folder. You can do this in Command Prompt with "mv ~/(PATH_TO_SECRETS.PY_HERE)/secrets.py ~/(PATH_TO_YOUR_PLANE_DIRECTORY_HERE)/secrets.py". 

11. Run plane.py for testing (You can do this in the plane directory with all the .py files by doing "python3 plane.py" in your Terminal).

12. You've finished the setup! Whenever you want to access your environment do step 4, then you can cd into your plane folder and run the python files from there.

### Onboarding Instructions for Testing on Mac

1. Create a new folder to store the contents of the Plane Mail Management repository. 

2. In Terminal, cd into the folder you have just created

3. Create a virtual environment by running: "python3 -m venv {name}"

4. Activate environment by running: "source {name}/bin/activate"

5. Git clone the repository in the environment you have created (git clone https://github.com/ScottyLabs/plane.git). Move into the new branch you are editing on

6. Install requirement files by running: "python3 -m pip install -r requirements.txt"

7. cd into the "plane" folder and transfer the file secrets.py into the "plane" folder. You can do this in Terminal with "mv ~/Downloads/secrets.py ~/(PATH_TO_YOUR_PLANE_DIRECTORY_HERE)/secrets.py". 

8. Run plane.py for testing (You can do this in the plane directory with all the .py files by doing "python3 plane.py" in your Terminal).

9. You've finished the setup! Whenever you want to access your environment do step 4, then you can cd into your plane folder and run the python files from there.