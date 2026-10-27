from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    """Return errors in a consistent {"success": false, "errors": ...} shape."""
    response = exception_handler(exc, context)
    if response is not None:
        return Response(
            {"success": False, "errors": response.data}, status=response.status_code
        )
    return response
