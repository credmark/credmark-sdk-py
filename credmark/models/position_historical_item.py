from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.position import Position


T = TypeVar("T", bound="PositionHistoricalItem")


@attr.s(auto_attribs=True)
class PositionHistoricalItem:
    """
    Attributes:
        block_number (float): Block number. Example: 15490034.
        block_timestamp (float): Block timestamp. Number of seconds since January 1, 1970. Example: 1662550007.
        positions (List['Position']):
    """

    block_number: float
    block_timestamp: float
    positions: List["Position"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        block_number = self.block_number
        block_timestamp = self.block_timestamp
        positions = []
        for positions_item_data in self.positions:
            positions_item = positions_item_data.to_dict()

            positions.append(positions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blockNumber": block_number,
                "blockTimestamp": block_timestamp,
                "positions": positions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.position import Position

        d = src_dict.copy()
        block_number = d.pop("blockNumber")

        block_timestamp = d.pop("blockTimestamp")

        positions = []
        _positions = d.pop("positions")
        for positions_item_data in _positions:
            positions_item = Position.from_dict(positions_item_data)

            positions.append(positions_item)

        position_historical_item = cls(
            block_number=block_number,
            block_timestamp=block_timestamp,
            positions=positions,
        )

        position_historical_item.additional_properties = d
        return position_historical_item

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
