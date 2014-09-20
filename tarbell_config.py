# -*- coding: utf-8 -*-
import markdown as Markdown
import os

from flask import Blueprint
from jinja2 import Markup

"""
Tarbell project configuration
"""

# Google spreadsheet key
CONTEXT_SOURCE_FILE = "_slides.xlsx"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt", "slides/*"]

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# S3 bucket configuration
S3_BUCKETS = {
    "production": "recoveredfactory.net/data-workflow",
    "staging": "recoveredfactory.net/data-workflow-draft",
}

# Default template variables
DEFAULT_CONTEXT = {
    'name': 'data-workflow',
    'title': 'Reusable data processing workflows'
}

blueprint = Blueprint('data_workflow', __name__)


def read_file(path, absolute=False):
    """
    Read the file at `path`. If `absolute` is True, use absolute path,
    otherwise path is assumed to be relative to Tarbell template root dir.
    """
    if not absolute:
        path = os.path.join(os.path.dirname(__file__), path)

    try:
        return open(path, 'r').read()
    except IOError:
        return None


@blueprint.app_context_processor
def context_processor():
    """
    Add helper functions to context for all projects.
    """
    return {
        'read_file': read_file,
    }


@blueprint.app_template_filter()
def markdown(value):
    """Run text through markdown process"""
    if value:
        return Markup(Markdown.markdown(value))
    return value
