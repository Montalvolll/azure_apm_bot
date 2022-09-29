#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from pathlib import Path
from dotenv import load_dotenv


class DefaultConfig:
    """ Bot Configuration """

    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", os.environ['APP_ID_'])
    APP_PASSWORD = os.environ.get(
        "MicrosoftAppPassword", os.environ['APP_PASSWORD_'])
