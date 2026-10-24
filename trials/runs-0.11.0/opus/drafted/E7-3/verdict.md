## Lines

| line | verdict | reason |
| --- | --- | --- |
| C1 | held | `kwargs.setdefault("strict", True)` in `ChatOpenRouter.with_structured_output` and `extra_body={"provider": {"require_parameters": True}}` keep the new provider path enforcing the id enum at decoding. |

## Trial

- where: code
- flagged: no
- stopped: no
- asked move: not asked