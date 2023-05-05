from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.run_model_dto_block_number_type_1 import RunModelDtoBlockNumberType1
from ..types import UNSET, Unset

T = TypeVar("T", bound="RunModelDto")


@attr.s(auto_attribs=True)
class RunModelDto:
    """
    Attributes:
        slug (str): slug of the model to run
        chain_id (int): chainId number, for example 1 for mainnet Default: 1.
        block_number (Union[RunModelDtoBlockNumberType1, int]): blockNumber is a number or a string with a number,
            'latest', 'earliest'
        input (Dict[str, Any]): Model input data
        version (Union[Unset, str]): Typically not required but you may specify version of the model to run
    """

    slug: str
    block_number: Union[RunModelDtoBlockNumberType1, int]
    input: Dict[str, Any]
    chain_id: int = 1
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        slug = self.slug
        chain_id = self.chain_id
        block_number: Union[int, str]

        if isinstance(self.block_number, RunModelDtoBlockNumberType1):
            block_number = self.block_number.value

        else:
            block_number = self.block_number

        input = self.input
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "chainId": chain_id,
                "blockNumber": block_number,
                "input": input,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        slug = d.pop("slug")

        chain_id = d.pop("chainId")

        def _parse_block_number(data: object) -> Union[RunModelDtoBlockNumberType1, int]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                block_number_type_1 = RunModelDtoBlockNumberType1(data)

                return block_number_type_1
            except:  # noqa: E722
                pass
            return cast(Union[RunModelDtoBlockNumberType1, int], data)

        block_number = _parse_block_number(d.pop("blockNumber"))

        input = d.pop("input")

        version = d.pop("version", UNSET)

        run_model_dto = cls(
            slug=slug,
            chain_id=chain_id,
            block_number=block_number,
            input=input,
            version=version,
        )

        run_model_dto.additional_properties = d
        return run_model_dto

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
