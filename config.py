#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "af159227-35b2-4d92-b8f5-e125644ca09c")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "9ZE8Q~3ThmvS~3empv3mOlJkcvY3~Ik0Z~wiwc67")
