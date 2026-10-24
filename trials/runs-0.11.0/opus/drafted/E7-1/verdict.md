## Lines

| line | verdict | reason |
| --- | --- | --- |
| C1 | held | `+ if method == "json_schema" and strict is None: strict = True` and `+ openrouter_provider=OPENROUTER_PROVIDER` (`{"require_parameters": True}`) keep the id enum enforced on the new OpenRouter path, as on Groq. A test checks that the sent request carries `strict: True`. |

## Trial

- where: code
- flagged: yes
- stopped: no
- asked move: not asked