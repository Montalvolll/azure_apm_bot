# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount
import requests
import json

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        
        # await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")
        message = str(turn_context.activity.text)
        response = ""
        if message == "test":
            response = "This is an automated test reply"
        elif message == "APM":
            response = "Great choice"
        elif "cx" or "Cx" in message:
        # elif message == "cx" or message == "Cx" or message == "ApmBot Cx" or message == "ApmBot cx":
            wd_g = 'http://torpbookmonwb1.sandals.com/data.cfc?method=getDailyBookings&rsvType=WD'
            data = requests.get(wd_g)
            json_data = json.loads(data.text)
            last = len(json_data) - 1
            response = (f"Counts:\n+ Bookings Today: {json_data[last]['today']}\n+ Bookings Yesterday: {json_data[last]['yesterday']}\n+ Last Week: {json_data[last]['dayLastWeek']}\n+ Last Year: {json_data[last]['dayLastYear']}")
        elif message == "today":
            wd_g = 'http://torpbookmonwb1.sandals.com/data.cfc?method=getDailyBookings&rsvType=WD'
            data = requests.get(wd_g)
            json_data = json.loads(data.text)
            last = len(json_data) - 1
            response = (f"Bookings Today: {json_data[last]['today']}")
        else:
            print(message)
            response = "Unknown command"
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
