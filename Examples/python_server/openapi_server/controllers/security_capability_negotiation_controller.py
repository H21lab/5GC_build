import connexion
import six

from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.problem_details import ProblemDetails  # noqa: E501
from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.sec_negotiate_req_data import SecNegotiateReqData  # noqa: E501
from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.sec_negotiate_rsp_data import SecNegotiateRspData  # noqa: E501
from openapi_server import util


def post_exchange_capability(body):  # noqa: E501
    """Security Capability Negotiation

     # noqa: E501

    :param sec_negotiate_req_data: Custom operation for security capability negotiation
    :type sec_negotiate_req_data: dict | bytes

    :rtype: SecNegotiateRspData
    """
    if connexion.request.is_json:
        sec_negotiate_req_data = SecNegotiateReqData.from_dict(connexion.request.get_json())  # noqa: E501
    #return 'do some magic!'
    return SecNegotiateRspData(sender="127.0.0.1", selected_sec_capability="TLS")
