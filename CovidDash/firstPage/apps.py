import app
import express
from django.apps import AppConfig


class FirstpageConfig(AppConfig):
    name = 'firstPage'
app.use(express.static('files')),