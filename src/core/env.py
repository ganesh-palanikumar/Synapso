import os
import yaml
import logging

logger = logging.getLogger(__name__)

CONFIG_ROOT = os.getenv('CONFIG_ROOT')
if not CONFIG_ROOT:
    raise ValueError('CONFIG_ROOT is not set')

CORTICES_CONFIG_PATH = os.getenv('CORTICES_CONFIG_PATH')
if not CORTICES_CONFIG_PATH:
    CORTICES_CONFIG_PATH = os.path.join(CONFIG_ROOT, 'cortex.yaml')
    if not os.path.exists(CORTICES_CONFIG_PATH):
        raise ValueError('CORTICES_CONFIG_PATH is not set. Checking in default location')

with open(CORTICES_CONFIG_PATH, 'r') as f:
    CORTICES_CONFIG = yaml.safe_load(f)
