from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


from Calendar import Calendar
from Event import Event

# If modifying these scopes, delete the file token.json.    
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():

    creds = None
    # Auth flow
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    calList = []
    try:
        service = build('calendar', 'v3', credentials=creds)
        calendars = service.calendarList().list().execute()

        

        for cal in calendars['items']:
            ans = input("Track this calendar (y/n): {} \n".format(cal['summary']))

            if ans == "y":
                calList.append(Calendar(cal['summary'], cal['id'], cal['timeZone'], True))
            elif ans == "n":
                calList.append(Calendar(cal['summary'], cal['id'], cal['timeZone'], False))
            else:
                print("Invalid input, setting calendar to inactive")
                calList.append(Calendar(cal['summary'], cal['id'], cal['timeZone'], False))



        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        oneWeek = (datetime.datetime.utcnow() + datetime.timedelta(days=7)).isoformat() + 'Z'

        for cal in calList:
            eventList = []

            if cal.isActive:

                events = service.events().list(calendarId=cal.id, timeMin=now, timeMax=oneWeek, showDeleted=False).execute()
                Event(events['items'][0])
                for event in events['items']:
                    try:
                        e = Event(event)
                        eventList.append(e);

                    except:
                        continue

            cal.events = eventList

    except HttpError as error:
        print('An error occurred: %s' % error)

    for cal in calList:
        for event in cal.events:
            print(event)


if __name__ == '__main__':
    main()