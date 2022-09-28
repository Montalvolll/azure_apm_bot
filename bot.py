# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount
import requests

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        # await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")
        message = str(turn_context.activity.text).lower()
        response = ""
        if message == "test":
            response = "This is an automated test reply"
        elif message == "apm":
            response = "Great choice"
        else:
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
