# Credmark

A client library for accessing Credmark Gateway

## Installation

Install using pip:

```bash
pip install credmark
```

## Usage

First, create an instance of `Credmark` client. In order to access the API, you will need a key. Information about getting a key is available in our [API setup guide](https://docs.credmark.com/api-how-to-guide/).

```python
from credmark import Credmark

client = Credmark(api_key="<Your API Key>")
```

Now call your endpoint by tag and use your models:

```python
from credmark.models import TokenMetadataResponse

metadata: TokenMetadataResponse = client.token_api.get_token_metadata(1, "0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9")
```

Or do the same thing with an async version:

```python
from credmark.models import TokenMetadataResponse

metadata: TokenMetadataResponse = await client.token_api.get_token_metadata_async(1, "0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9")
```

## Run a model

You can run a model using DeFi API:

```python
from credmark.defi_api import run_model
from credmark.models import RunModelDto

async def run_model_example():
    price_data = await client.defi_api.run_model_async(
        json_body=RunModelDto(
            chain_id=1, 
            block_number="latest", 
            slug="price.quote", 
            input={"base": {"symbol": "AAVE"}}
        ),
    )

    if price_data.error:
        print(price_data.error)
        return

    price = price_data.output['price']
    print(price)
```

## Available APIs

- [Token API](https://github.com/credmark/credmark-sdk-py/blob/main/credmark/docs/TokenAPI.md)
- [DeFi API](https://github.com/credmark/credmark-sdk-py/blob/main/credmark/docs/DeFiAPI.md)
- [Utilities API](https://github.com/credmark/credmark-sdk-py/blob/main/credmark/docs/Utilities.md)

## Things to know

1. Every path/method combo has four functions:
    1. default: Blocking request that returns parsed data (if successful) or `None`
    2. `async`: Like default but async instead of blocking

2. All path/query params, and bodies become method arguments.

## Advanced Usage

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = Credmark(
    base_url="https://internal_api.example.com", 
    api_key="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = Credmark(
    base_url="https://internal_api.example.com", 
    api_key="SuperSecretToken", 
    verify_ssl=False
)
```

There are more settings on the generated `Credmark` class which let you control more runtime behavior, check out the docstring on that class for more info.
