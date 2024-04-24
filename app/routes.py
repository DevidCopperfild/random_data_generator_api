from flask import Blueprint, jsonify, request
from .utils import generate_random_data

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/generate", methods=["POST"])
def generate():
    data_type = request.json.get("type")
    count = int(request.json.get("count"))
    data = generate_random_data(data_type, count)
    return jsonify(data)