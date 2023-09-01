from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Dict

import httpx

if TYPE_CHECKING:
    from ...client import Credmark

from typing import Dict

from ... import errors
from ...models.block_response import BlockResponse
from ...models.utilities_error_response import UtilitiesErrorResponse
from ...types import Response


def _get_kwargs(chain_id: int, client: "Credmark") -> Dict[str, Any]:
    url = "{}/v1/utilities/chains/{chainId}/block/latest".format(client.base_url, chainId=chain_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: "Credmark", response: httpx.Response) -> BlockResponse:
    if response.status_code == HTTPStatus.OK:
        response_200 = BlockResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = UtilitiesErrorResponse.from_dict(response.json())

        raise errors.CredmarkError(response.status_code, response.content, response_400)
    raise errors.CredmarkError(response.status_code, response.content)


def _build_response(*, client: "Credmark", response: httpx.Response) -> Response[BlockResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(chain_id: int, client: "Credmark") -> Response[BlockResponse]:
    """Get latest block.

     Returns latest block of the specified chain.

    Args:
        chain_id (int): Chain identifier. This endpoint supports the following chains

            `1` - Ethereum Mainnet
            `10` - Optimism
            `56` - BSC
            `137` - Polygon Mainnet
            `250` - Fantom Opera
            `42161` - Arbitrum One
            `43114` - Avalanche C-Chain

    Raises:
        errors.CredmarkError: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlockResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(chain_id: int, client: "Credmark") -> BlockResponse:
    """Get latest block.

     Returns latest block of the specified chain.

    Args:
        chain_id (int): Chain identifier. This endpoint supports the following chains

            `1` - Ethereum Mainnet
            `10` - Optimism
            `56` - BSC
            `137` - Polygon Mainnet
            `250` - Fantom Opera
            `42161` - Arbitrum One
            `43114` - Avalanche C-Chain

    Raises:
        errors.CredmarkError: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlockResponse]
    """

    return sync_detailed(
        chain_id=chain_id,
        client=client,
    ).parsed


async def asyncio_detailed(chain_id: int, client: "Credmark") -> Response[BlockResponse]:
    """Get latest block.

     Returns latest block of the specified chain.

    Args:
        chain_id (int): Chain identifier. This endpoint supports the following chains

            `1` - Ethereum Mainnet
            `10` - Optimism
            `56` - BSC
            `137` - Polygon Mainnet
            `250` - Fantom Opera
            `42161` - Arbitrum One
            `43114` - Avalanche C-Chain

    Raises:
        errors.CredmarkError: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlockResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(chain_id: int, client: "Credmark") -> BlockResponse:
    """Get latest block.

     Returns latest block of the specified chain.

    Args:
        chain_id (int): Chain identifier. This endpoint supports the following chains

            `1` - Ethereum Mainnet
            `10` - Optimism
            `56` - BSC
            `137` - Polygon Mainnet
            `250` - Fantom Opera
            `42161` - Arbitrum One
            `43114` - Avalanche C-Chain

    Raises:
        errors.CredmarkError: If the server returns a non 2xx status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlockResponse]
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            client=client,
        )
    ).parsed
