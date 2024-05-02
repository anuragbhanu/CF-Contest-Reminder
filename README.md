
# Codeforces Contest Reminder

This Python script fetches upcoming Codeforces contests and sends SMS reminders using Twilio.


## Installation

- To Run and Test Locally on Your System :-

    - Make sure you have Python 3 installed on your system.

    - Install required packages:

        ```bash
        pip install requests pytz twilio
        ```
    
## Setup
- Sign up for a **Free Twilio account** at [Twilio](https://www.twilio.com/en-us).
- Verify and Obtain your Twilio Account SID, Auth Token, and Twilio phone number from the Twilio Console.
- Replace the following placeholders in main.py with your actual **Twilio credentials** and Phone numbers:
    - "Your Twilio Account SID" with your Twilio     Account SID.
    - "Your Twilio Auth Token" with your Twilio Auth Token.
    - "Your Twilio phone number" with your Twilio phone number.
    - "Your Phone Number with Country Code" with your phone number.

- Customize the Message Body as per Your Convience


##  Automating on PythonAnywhere
- Sign up for a Free account at [PythonAnywhere](https://www.pythonanywhere.com/).
- Activate and Upload your Python script (`main.py`) to your PythonAnywhere account's "Files" Tab.
- Go to the "Tasks" tab in PythonAnywhere and create a new scheduled task.

    - Add the UTC Format time (3:30 AM -> equivalent to 9 AM , IST)

    - Add the Given Command and Press "Create" to Finally Save it to Run daily Once.
    ```bash
        python3 main.py
    ```

    - Monitor its execution logs for any issues.
## Demo

![1](https://github.com/anuragbhanu/CF-Contest-Remainder/assets/130905151/48a12738-9751-4297-a166-1927e14d11d7)
![2](https://github.com/anuragbhanu/CF-Contest-Remainder/assets/130905151/43d6dce7-c325-4898-b67b-5e0922569bce)


