# get_next_line

## Subject

Write a function named `get_next_line` that reads one line at a time from a file descriptor.

### Prototype

```python
def get_next_line(fd, buffer_size=42) -> str | None:
```

### Description

- Returns the next line from the file descriptor `fd`, **including** the trailing `\n` if present.
- Returns the remaining content (without `\n`) when the end of file is reached on a line that has no newline.
- Returns `None` when there is nothing left to read (EOF and buffer is empty).
- Uses an internal per-fd buffer so successive calls correctly advance through the file.
- The optional `buffer_size` parameter controls the number of bytes read per OS call (default: 42).

### Return value

| Condition | Return value |
|-----------|-------------|
| Line with newline | `"line content\n"` |
| Last line without newline | `"line content"` |
| End of file / error | `None` |

## Usage

```python
import os
from get_next_line import get_next_line

fd = os.open("file.txt", os.O_RDONLY)
line = get_next_line(fd)
while line is not None:
    print(repr(line))
    line = get_next_line(fd)
os.close(fd)
```

## Files

- `get_next_line.py` — implementation
