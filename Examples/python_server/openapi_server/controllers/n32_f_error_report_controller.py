import connexion
import six

from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.n32f_error_info import N32fErrorInfo  # noqa: E501
from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.problem_details import ProblemDetails  # noqa: E501
from openapi_server import util


def post_n32f_error(n32f_error_info):  # noqa: E501
    """N32-f Error Reporting Procedure

     # noqa: E501

    :param n32f_error_info: Custom operation for n32-f error reporting procedure
    :type n32f_error_info: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        n32f_error_info = N32fErrorInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
