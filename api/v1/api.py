import requests
from cerberus import Validator
from flask import Blueprint, request, jsonify

# Create blueprint for `v1` API
api_v1 = Blueprint('api_v1', __name__)

GITHUB_API_URL = "https://api.github.com"
GITHUB_SEARCH_CODE_URL = GITHUB_API_URL + "/search/code"


@api_v1.route('/search', methods=['GET'])
def search():
    """Search handler searches for a given query in a given language and
    repository on Github."""

    # Validate the search query
    v = search_validator()
    if not v.validate(request.args):
        return jsonify(v.errors), 400

    try:
        search = request.args.get('search')
        lang = request.args.get('language')
        repo = request.args.get('repository')

        # Make a request to the GitHub API
        r = requests.get(
            f'{GITHUB_SEARCH_CODE_URL}?q={search}+in:file+language:{lang}+repo:{repo}',
        )

        if r.status_code == 200:
            json_items = r.json()['items']
            
            # Filter the items to only include the keys that we expect
            items = [{k: item[k] for k in search_response_keys()} for item in json_items]

            return jsonify({'items': items}), 200
        else:
            return jsonify({'error': 'Something went wrong!'}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def search_validator():
    """
    Validates the search query.
    """
    search_schema = {
        "search": {
            "type": "string",
            "required": True,
            "empty": False
        },
        "language": {
            "type": "string",
            "required": True,
            "empty": False
        },
        "repository": {
            "type": "string",
            "required": True,
            "empty": False
        }
    }
    return Validator(search_schema)


def search_response_keys():
    """Returns the keys that are expected in the search response."""
    keys = ["name", "path", "html_url", "url"]
    return keys

