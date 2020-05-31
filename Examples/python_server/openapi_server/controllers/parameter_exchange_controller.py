import connexion
import six

from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.problem_details import ProblemDetails  # noqa: E501
from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.sec_param_exch_req_data import SecParamExchReqData  # noqa: E501
from openapi_server.com.h21lab.TS29573_N32_Handshake.handler.sec_param_exch_rsp_data import SecParamExchRspData  # noqa: E501
from openapi_server import util


def post_exchange_params(sec_param_exch_req_data):  # noqa: E501
    """Parameter Exchange

     # noqa: E501

    :param sec_param_exch_req_data: Custom operation for parameter exchange
    :type sec_param_exch_req_data: dict | bytes

    :rtype: SecParamExchRspData
    """
    if connexion.request.is_json:
        sec_param_exch_req_data = SecParamExchReqData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
