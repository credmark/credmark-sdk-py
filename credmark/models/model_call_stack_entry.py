from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelCallStackEntry")


@attr.s(auto_attribs=True)
class ModelCallStackEntry:
    """
    Attributes:
        slug (str): Short identifying name for the model Example: var.
        version (str): Version of the model Example: 1.0.
        chain_id (float): Context chain id
        block_number (float): Context block number
        trace (Union[Unset, None, str]): Human-readable message containing a trace of the code that generated the error
    """

    slug: str
    version: str
    chain_id: float
    block_number: float
    trace: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        slug = self.slug
        version = self.version
        chain_id = self.chain_id
        block_number = self.block_number
        trace = self.trace

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "version": version,
                "chainId": chain_id,
                "blockNumber": block_number,
            }
        )
        if trace is not UNSET:
            field_dict["trace"] = trace

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        slug = d.pop("slug")

        version = d.pop("version")

        chain_id = d.pop("chainId")

        block_number = d.pop("blockNumber")

        trace = d.pop("trace", UNSET)

        model_call_stack_entry = cls(
            slug=slug,
            version=version,
            chain_id=chain_id,
            block_number=block_number,
            trace=trace,
        )

        model_call_stack_entry.additional_properties = d
        return model_call_stack_entry

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
