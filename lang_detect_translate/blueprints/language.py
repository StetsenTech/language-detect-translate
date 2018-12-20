"""Blueprint responsible for routing for language functionality"""
from flask import Blueprint, jsonify, request

from lang_detect_translate.components import Language

bp = Blueprint('translate_route',__name__,
    url_prefix='/translate'
)

LanguageClass = Language()

@bp.route('/', methods=['POST'], strict_slashes=False)
def index():
    """Base route for detects and translates input to english""" 
    content = request.get_json()
    translated_text = LanguageClass.translate_text(content['input'])

    return jsonify(translated_text)
