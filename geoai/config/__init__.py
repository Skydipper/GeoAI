"""CONFIG MODULE"""
import os
from geoai.config import base, staging, prod


SETTINGS = base.SETTINGS

if os.getenv('ENVIRONMENT') == 'staging':
    SETTINGS.update(staging.SETTINGS)

if os.getenv('ENVIRONMENT') == 'prod':
    SETTINGS.update(prod.SETTINGS)
