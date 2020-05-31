import connexion
import six

from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.n32f_context_info import N32fContextInfo  # noqa: E501
from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.problem_details import ProblemDetails  # noqa: E501
from openapi_server import util


def post_n32f_terminate(n32f_context_info):  # noqa: E501
    """N32-f Context Terminate

     # noqa: E501

    :param n32f_context_info: Custom operation for n32-f context termination
    :type n32f_context_info: dict | bytes

    :rtype: N32fContextInfo
    """
    if connexion.request.is_json:
        n32f_context_info = N32fContextInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
