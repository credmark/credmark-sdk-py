from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.token_balance_historical_item import TokenBalanceHistoricalItem


T = TypeVar("T", bound="TokenBalanceHistoricalResponse")


@attr.s(auto_attribs=True)
class TokenBalanceHistoricalResponse:
    """
    Attributes:
        chain_id (float): Chain ID. Example: 1.
        start_block_number (float): Start block number. Example: 15384120.
        end_block_number (float): End block number. Example: 15581908.
        start_timestamp (float): Start timestamp. Number of seconds since January 1, 1970. Example: 1661086905.
        end_timestamp (float): End timestamp. Number of seconds since January 1, 1970. Example: 1663765199.
        token_address (str): Token address for the price. Example: 0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9.
        scaled (bool): If the balance is scaled by token decimals. Example: True.
        quote_address (str): Quote address is the token/currency of the price units. Example:
            0x0000000000000000000000000000000000000348.
        data (List['TokenBalanceHistoricalItem']):
    """

    chain_id: float
    start_block_number: float
    end_block_number: float
    start_timestamp: float
    end_timestamp: float
    token_address: str
    scaled: bool
    quote_address: str
    data: List["TokenBalanceHistoricalItem"]

    def to_dict(self) -> Dict[str, Any]:
        chain_id = self.chain_id
        start_block_number = self.start_block_number
        end_block_number = self.end_block_number
        start_timestamp = self.start_timestamp
        end_timestamp = self.end_timestamp
        token_address = self.token_address
        scaled = self.scaled
        quote_address = self.quote_address
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()

            data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "chainId": chain_id,
                "startBlockNumber": start_block_number,
                "endBlockNumber": end_block_number,
                "startTimestamp": start_timestamp,
                "endTimestamp": end_timestamp,
                "tokenAddress": token_address,
                "scaled": scaled,
                "quoteAddress": quote_address,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.token_balance_historical_item import TokenBalanceHistoricalItem

        d = src_dict.copy()
        chain_id = d.pop("chainId")

        start_block_number = d.pop("startBlockNumber")

        end_block_number = d.pop("endBlockNumber")

        start_timestamp = d.pop("startTimestamp")

        end_timestamp = d.pop("endTimestamp")

        token_address = d.pop("tokenAddress")

        scaled = d.pop("scaled")

        quote_address = d.pop("quoteAddress")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = TokenBalanceHistoricalItem.from_dict(data_item_data)

            data.append(data_item)

        token_balance_historical_response = cls(
            chain_id=chain_id,
            start_block_number=start_block_number,
            end_block_number=end_block_number,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            token_address=token_address,
            scaled=scaled,
            quote_address=quote_address,
            data=data,
        )

        return token_balance_historical_response
