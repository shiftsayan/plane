# Plane Mail Management Initial Documentation

### Onboarding Instructions for Testing on Windows

1. Go to "Turn Windows features on or off" in the control panel

2. Enable "Windows Subsystem for Linux" checkbox. You may have to restart your computer for changes to take effect

3. Install Ubuntu

4. Choose a location and create a folder to store the content for Plane Mail. You can use cd ~ to create the folder in a separate file system from your local drive.

5. Install python 3 and pip if you have not already done so. You can run "sudo apt update" and "sudo apt install python3-pip"

6. Create a virtual environment by running: "python3 -m venv {name}"

7. Activate environment by running: "source {name}/bin/activate"

8. Install requirement files by running: "python3 -m pip install -r requirements.txt"

9. Git clone the repository in the environment you have created. Move into the new branch you are editing on.

10. cd into the "plane" folder and transfer the file secrets.py into the "plane" folder

11. Run plane.py for testing

