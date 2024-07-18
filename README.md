# str_uuid

Written for a pydantic factory, used many times in many places.

Yes, this could be written in each server. Yes, I am lazy enough to publish this so that I save 4 seconds each time I make new infrastructure.

```python
from str_uuid import str_uuid4
its_a_string: str = str_uuid4()
```

Thanks for reading.
