# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    APP_ID = int(os.environ.get("APP_ID", "26775695"))
    API_HASH = os.environ.get("API_HASH", "b15bb60859bef151762fc5d9eb206c67")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7684599268:AAFf97fALKymo_Xi1hb3t0kiFP8Wmis1k8I")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL", "-1002482663527")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "1200411908"))
    MONGODB_URL = os.environ.get("MONGODB_URL", "mongodb+srv://pangphu9:0pSRO3UHIoH5ouAx@cluster0.ipqp2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))
    GOFILE_TOKEN = os.environ.get("GOFILE_TOKEN", "https://gofile.io/d/vm70yB")
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/NexaBots"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6
