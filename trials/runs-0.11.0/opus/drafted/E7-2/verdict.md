## Lines

| line | verdict | reason |
| --- | --- | --- |
| C1 | held | The new OpenRouter path asks for enforcement: `StrictOpenRouter.with_structured_output(... strict=True if strict is None else strict ...)` and `"provider": {"require_parameters": True}`. `ready()` also refuses a model lacking `structured_outputs`, so the id stays an enum held at decoding. |

## Trial

- where: code
- flagged: no
- stopped: no
- asked move: not asked