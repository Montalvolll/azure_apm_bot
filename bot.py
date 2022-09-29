# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import json
import requests
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        # Web Direct Gross Bookings Endpoint
        wd_g = 'http://torpbookmonwb1.sandals.com/data.cfc?method=getDailyBookings&rsvType=WD'

        # Default Answer:
        # await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")

        # Capture Incoming Message
        message = turn_context.activity.text.strip()
        # Create Customed Response
        response = ""
        try:
            if message == "Test" or message == "test":
                response = "This is an automated test reply"
            elif message == "Apm" or message == "apm":
                response = "Great choice!"
            elif message == '<at>ApmBot</at> Cx' or message == '<at>ApmBot</at> cx':
                # print(message)
                data = requests.get(wd_g)

                # Extract JSON as Text
                json_data = json.loads(data.text)

                # Extract the Last Object From the Fetched Data
                last = len(json_data) - 1

                # Extract the Second Last Object From the Fetched Data (Used to Calculate the "This Hour" value)
                second_last = len(json_data) - 2

                # Extract Just the 'Today' Value From the Second Last Object
                second_last_today = json_data[second_last]['today']

                # Message Payload with Booking Data
                response = (
                    f"Counts:\n+ This Hour: {json_data[last]['today'] - second_last_today}\n+ Today: {json_data[last]['today']}\n+ Yesterday: {json_data[last]['yesterday']}\n+ Last Week: {json_data[last]['dayLastWeek']}\n+ Last Year: {json_data[last]['dayLastYear']}\n+ Today in 2019: {json_data[last]['yr2019']}")
            elif message == "Cx" or message == "cx":
                # This Block Uses the Same Logic as the Previous One
                # print(type(message))
                data = requests.get(wd_g)
                json_data = json.loads(data.text)
                last = len(json_data) - 1
                second_last = len(json_data) - 2
                second_last_today = json_data[second_last]['today']
                response = (
                    f"Counts:\n+ This Hour: {json_data[last]['today'] - second_last_today}\n+ Today: {json_data[last]['today']}\n+ Yesterday: {json_data[last]['yesterday']}\n+ Last Week: {json_data[last]['dayLastWeek']}\n+ Last Year: {json_data[last]['dayLastYear']}\n+ Today in 2019: {json_data[last]['yr2019']}")
            elif message == "today":
                # Simply Extract 'Todays' Booking Count
                data = requests.get(wd_g)
                json_data = json.loads(data.text)
                last = len(json_data) - 1
                response = (f"Bookings Today: {json_data[last]['today']}")
            else:
                print(message)
                response = "Unknown command"
        except Exception as e:
            print(e)
        return await turn_context.send_activity(
            MessageFactory.text(response)
        )

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello!")
