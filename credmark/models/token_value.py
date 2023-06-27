from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="TokenValue")


@attr.s(auto_attribs=True)
class TokenValue:
    """
    Attributes:
        token_address (str): Token address Example: 0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9.
        token_price (float): Token price in quoted currency. Example: 18990392.724937014.
        balance (float): Token balance scaled to token decimals Example: 248367.58266143446.
        value (float): Token value in quoted currency. Example: 18990392.724937014.
    """

    token_address: str
    token_price: float
    balance: float
    value: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token_address = self.token_address
        token_price = self.token_price
        balance = self.balance
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tokenAddress": token_address,
                "tokenPrice": token_price,
                "balance": balance,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token_address = d.pop("tokenAddress")

        token_price = d.pop("tokenPrice")

        balance = d.pop("balance")

        value = d.pop("value")

        token_value = cls(
            token_address=token_address,
            token_price=token_price,
            balance=balance,
            value=value,
        )

        token_value.additional_properties = d
        return token_value

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
