from flask import Blueprint, jsonify, request

from app.custom_exception.ti_automation_exception import TIAutpmationException
from app.utils.backend_query_request import backend_query_request
from app.utils.logger_helper import app_logger

record_filter_bp = Blueprint("record_filter", __name__)


@record_filter_bp.route("submit-filter-form", methods=["POST"])
def record_filter():
    """
    Function to filter records
    """
    app_logger.info(
        "Got request to filter the records from user: %s with request data: %s",
        request.remote_addr,
        request.json,
    )

    data = request.json

    start_date = data.get("startDate")
    end_date = data.get("endDate")
    field_name_value = data.get("fieldNameValue")
    field_value = data.get("fieldValue")

    app_logger.info("Preparing backend filter request for query: %s", data)

    backend_request = {"dateRange": f"{start_date} to {end_date}"}

    if field_name_value:
        backend_request[field_name_value] = field_value

    app_logger.info("Successfully prepared the backend request: %s", backend_request)

    filtered_records = {"result": []}

    try:
        filtered_records = backend_query_request(backend_request)
    except TIAutpmationException as exc:
        app_logger.error("Failed to filter records with error: %s", exc.message)

    return jsonify(filtered_records["result"])
