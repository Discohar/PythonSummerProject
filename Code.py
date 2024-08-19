import smtplib
import requests
from bs4 import BeautifulSoup
import geocoder
import pyttsx3
import os
import time
from twilio.rest import Client
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pywhatkit as kit
import googlesearch
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

# Replace with your Twilio credentials
TWILIO_ACCOUNT_SID = 'ACfc04a4adafe17fa9e6ae75a36d64ddf2'
TWILIO_AUTH_TOKEN = 'e0bb7a7106a21a34d8718283656cf504'
TWILIO_PHONE_NUMBER = '+15075745698'
TO_PHONE_NUMBER = '+918591872242'

# Email credentials
EMAIL_USER = 'harishgupta3514@gmail.com'
EMAIL_PASS = 'rjjy lznx tmlv wlsu'
TO_EMAIL = 'harishgupta3514@gmail.com'

# For bulk emails, define a list of email addresses
EMAIL_LIST = ['harishgupta3514@gmail.com', 'harishgupta4153@gmail.com' , 'harishgupta3154@gmail.com']

def send_email():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        message = 'Subject: {}\n\n{}'.format('Test Subject', 'Test Message')
        server.sendmail(EMAIL_USER, TO_EMAIL, message)
        server.quit()
        print('Email sent!')
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

def send_bulk_email():
    for email in EMAIL_LIST:
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            message = 'Subject: {}\n\n{}'.format('Bulk Email Subject', 'This is a bulk email.')
            server.sendmail(EMAIL_USER, email, message)
            server.quit()
            print(f'Email sent to {email}!')
        except Exception as e:
            print(f"Failed to send email to {email}: {str(e)}")

def send_sms():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="This is a test SMS.",
        from_=TWILIO_PHONE_NUMBER,
        to=TO_PHONE_NUMBER
    )
    print(f"SMS sent! Message SID: {message.sid}")

def google_search():
    query = input('Enter your query: ')
    try:
        for i in googlesearch.search(query, num_results=5):
            print(i)
    except Exception as e:
        print(f"Error: {e}")

def get_geo_coordinates():
    g = geocoder.ip('me')
    print(f"Your current location: {g.latlng}")

def text_to_audio():
    text = input("Enter text for speech conversion: ")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def control_volume_with_hand():
    cap = cv2.VideoCapture(0)
    detector = HandDetector(detectionCon=0.7, maxHands=1)

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    while True:
        success, img = cap.read()
        hands, img = detector.findHands(img)

        if hands:
            hand = hands[0]
            lmList = hand['lmList']
            # Get the coordinates of the index finger tip and thumb tip
            x1, y1 = lmList[8][:2]  # Index finger tip
            x2, y2 = lmList[4][:2]  # Thumb tip

            # Get the distance between the index finger tip and thumb tip
            length, info, img = detector.findDistance((x1, y1), (x2, y2), img)

            # Convert the distance to a volume level
            vol = np.interp(length, [30, 300], [volume.GetVolumeRange()[0], volume.GetVolumeRange()[1]])

            # Set the volume level
            volume.SetMasterVolumeLevel(vol, None)

            # Display the volume level on the screen
            vol_percent = np.interp(vol, [volume.GetVolumeRange()[0], volume.GetVolumeRange()[1]], [0, 100])
            cv2.putText(img, f'Volume: {int(vol_percent)}%', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def send_sms_mobile():
    kit.sendwhatmsg_instantly("+91 8591872242", "Sita Ram.")

def main():
    while True:
        print("\nSelect a task to run:")
        print("1. Send Email")
        print("2. Send SMS")
        print("3. Scrape Google")
        print("4. Get Geo Coordinates")
        print("5. Text to Audio")
        print("6. Control Volume with Hand Gestures")
        print("7. Send SMS via Mobile")
        print("8. Send Bulk Email")
        print("9. Exit")
        
        choice = int(input("Enter the task number: "))
        
        if choice == 1:
            send_email()
        elif choice == 2:
            send_sms()
        elif choice == 3:
            google_search()
        elif choice == 4:
            get_geo_coordinates()
        elif choice == 5:
            text_to_audio()
        elif choice == 6:
            control_volume_with_hand()
        elif choice == 7:
            send_sms_mobile()
        elif choice == 8:
            send_bulk_email()
        elif choice == 9:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
