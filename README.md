# Running the program after initial installation
1. In your terminal (Unix/macOS) or command prompt (Windows), cd into the plane folder
2. Run "source env/bin/activate" (Unix/macOs) or ".\env\Scripts\activate" (Windows). This will activate the virtual environment
3. Now, run "python3 plane.py" to begin the program. 
4. Use the arrow keys to move up and down between the available options at each prompt. 
5. Once you select which type of email you want to send, you will see the HTML template for the email in vim. To edit it directly, press "i".
6. Once you are done editing the file, press "esc" and type ":wq". This will save your changes and open up a preview of the email in your browser.
6. Go back to your terminal (Unix/macOS) or command prompt (Windows). To continue editing the file, type "n". To send out the email, enter "y".
    **NOTE**: entering "y" will automatically send out the email.
7. To exit the program at any time, simply press "control + c"
    **NOTE**: be sure to exit out of editing before pressing "control + c"
8. Be sure to deactivate the virtual environment at the end of your session by running "deactivate".