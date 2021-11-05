import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
# To install this module, run:
# python -m pip install Pillow
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person

# This key will serve all examples in this document.
KEY = "245f37d21cbc451c9bfc6e01f4f8e6bf"

# This endpoint will be used in all examples in this quickstart.
ENDPOINT = "https://face-api-python-so.cognitiveservices.azure.com/"