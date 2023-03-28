from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ModelDeployment")


@attr.s(auto_attribs=True)
class ModelDeployment:
    """
    Attributes:
        name (str): Short identifying name for the model Example: var.
        version (str): The version of the model in this deployment Example: 1.0.0.
        location (str): The location of the model Example: credmark-models-py.
    """

    name: str
    version: str
    location: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        version = self.version
        location = self.location

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "version": version,
                "location": location,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        version = d.pop("version")

        location = d.pop("location")

        model_deployment = cls(
            name=name,
            version=version,
            location=location,
        )

        model_deployment.additional_properties = d
        return model_deployment

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
