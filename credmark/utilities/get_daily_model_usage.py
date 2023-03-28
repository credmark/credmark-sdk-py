from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from .. import errors
from ..client import AuthenticatedClient, Client
from ..types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    days: Union[Unset, None, float] = UNSET,
    group_by: Union[Unset, None, str] = UNSET,
    requester: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/usage/requests".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["days"] = days

    params["groupBy"] = group_by

    params["requester"] = requester

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[List[Dict[str, Any]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(List[Dict[str, Any]], response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[List[Dict[str, Any]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    days: Union[Unset, None, float] = UNSET,
    group_by: Union[Unset, None, str] = UNSET,
    requester: Union[Unset, None, str] = UNSET,
) -> Response[List[Dict[str, Any]]]:
    """Model Request statistics

     Returns a list of daily model request statistics, either for a specific requester or for everyone.

    Args:
        days (Union[Unset, None, float]):
        group_by (Union[Unset, None, str]):
        requester (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[Dict[str, Any]]]
    """

    kwargs = _get_kwargs(
        client=client,
        days=days,
        group_by=group_by,
        requester=requester,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    days: Union[Unset, None, float] = UNSET,
    group_by: Union[Unset, None, str] = UNSET,
    requester: Union[Unset, None, str] = UNSET,
) -> Optional[List[Dict[str, Any]]]:
    """Model Request statistics

     Returns a list of daily model request statistics, either for a specific requester or for everyone.

    Args:
        days (Union[Unset, None, float]):
        group_by (Union[Unset, None, str]):
        requester (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[Dict[str, Any]]]
    """

    return sync_detailed(
        client=client,
        days=days,
        group_by=group_by,
        requester=requester,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    days: Union[Unset, None, float] = UNSET,
    group_by: Union[Unset, None, str] = UNSET,
    requester: Union[Unset, None, str] = UNSET,
) -> Response[List[Dict[str, Any]]]:
    """Model Request statistics

     Returns a list of daily model request statistics, either for a specific requester or for everyone.

    Args:
        days (Union[Unset, None, float]):
        group_by (Union[Unset, None, str]):
        requester (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[Dict[str, Any]]]
    """

    kwargs = _get_kwargs(
        client=client,
        days=days,
        group_by=group_by,
        requester=requester,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    days: Union[Unset, None, float] = UNSET,
    group_by: Union[Unset, None, str] = UNSET,
    requester: Union[Unset, None, str] = UNSET,
) -> Optional[List[Dict[str, Any]]]:
    """Model Request statistics

     Returns a list of daily model request statistics, either for a specific requester or for everyone.

    Args:
        days (Union[Unset, None, float]):
        group_by (Union[Unset, None, str]):
        requester (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[Dict[str, Any]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            days=days,
            group_by=group_by,
            requester=requester,
        )
    ).parsed
