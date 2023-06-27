from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="TokenReturn")


@attr.s(auto_attribs=True)
class TokenReturn:
    """
    Attributes:
        token_address (str): Token address Example: 0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9.
        balance (float): Token balance scaled to token decimals Example: 248367.58266143446.
        value (float): Token value in quoted currency. Example: 18990392.724937014.
        return_ (float): Overall profit (+ve) or loss (-ve) returned by the token. Example: 1899.72.
    """

    token_address: str
    balance: float
    value: float
    return_: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token_address = self.token_address
        balance = self.balance
        value = self.value
        return_ = self.return_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tokenAddress": token_address,
                "balance": balance,
                "value": value,
                "return": return_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token_address = d.pop("tokenAddress")

        balance = d.pop("balance")

        value = d.pop("value")

        return_ = d.pop("return")

        token_return = cls(
            token_address=token_address,
            balance=balance,
            value=value,
            return_=return_,
        )

        token_return.additional_properties = d
        return token_return

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
