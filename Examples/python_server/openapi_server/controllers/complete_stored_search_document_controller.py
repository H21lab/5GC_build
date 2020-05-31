import connexion
import six

from openapi_server.com.h21lab.TS29510_Nnrf_NFDiscovery.handler.stored_search_result import StoredSearchResult  # noqa: E501
from openapi_server import util


def retrieve_complete_search(search_id, accept_encoding=None):  # noqa: E501
    """retrieve_complete_search

     # noqa: E501

    :param search_id: Id of a stored search
    :type search_id: str
    :param accept_encoding: Accept-Encoding, described in IETF RFC 7231
    :type accept_encoding: str

    :rtype: StoredSearchResult
    """
    return 'do some magic!'
