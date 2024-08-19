
This Python script provides a menu-based interface for executing a variety of automated tasks. Designed to run on Windows, it integrates functionalities for email and SMS communication, web searching, geographical data retrieval, text-to-speech conversion, and audio volume control through hand gestures. The script utilizes a range of Python libraries and APIs to achieve these tasks efficiently.

Features

1. **Send Email**:
   - **Single Email**: Sends a test email to a specified recipient using Gmail's SMTP server.
   - **Bulk Email**: Sends emails to multiple recipients from a predefined list.

2. **Send SMS**:
   - Sends a test SMS message using the Twilio API to a specified phone number.

3. **Google Search**:
   - Performs a Google search based on user input and displays the top 5 search result URLs.

4. **Get Geo Coordinates**:
   - Retrieves and displays your current geographical coordinates based on your IP address.

5. **Text to Audio**:
   - Converts user-provided text into spoken words using the `pyttsx3` library for offline text-to-speech conversion.

6. **Control Volume with Hand Gestures**:
   - Adjusts your system’s audio volume based on hand gestures detected via webcam. The volume is controlled using the `pycaw` library.

7. **Send SMS via Mobile**:
   - Sends instant WhatsApp messages using the `pywhatkit` library.

## How to Use

1. **Run the Script**:
   - Execute the script using Python. A menu will be displayed, prompting you to select a task.

2. **Select a Task**:
   - Input the number corresponding to the task you want to perform.

3. **Follow Prompts**:
   - Depending on the selected task, you may be asked to provide additional input (e.g., email addresses, search queries).

4. **Exit**:
   - Select the exit option from the menu to terminate the program.

## Requirements

- Python 3.x
- Libraries:
  - `smtplib`
  - `requests`
  - `beautifulsoup4`
  - `geocoder`
  - `pyttsx3`
  - `twilio`
  - `pycaw`
  - `pywhatkit`
  - `googlesearch-python`
  - `cvzone`
  - `opencv-python`
  - `numpy`
  - `comtypes` (for volume control)

## Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/your-username/multi-function-automation-script.git
   ```
2. **Navigate to the Project Directory**:
   ```sh
   cd multi-function-automation-script
   ```
3. **Install Required Libraries**:
   ```sh
   pip install -r requirements.txt
   ```
   Alternatively, install libraries individually:
   ```sh
   pip install smtplib requests beautifulsoup4 geocoder pyttsx3 twilio pycaw pywhatkit googlesearch-python cvzone opencv-python numpy comtypes
   ```

## Usage Example

1. **Start the Program**:
   ```sh
   python script_name.py
   ```
2. **Menu Options**:
   - **1**: Send Email
   - **2**: Send SMS
   - **3**: Google Search
   - **4**: Get Geo Coordinates
   - **5**: Text to Audio
   - **6**: Control Volume with Hand Gestures
   - **7**: Send SMS via Mobile
   - **8**: Send Bulk Email
   - **9**: Exit


Feel free to adjust any details to better fit your project’s specifics or your personal preferences.
