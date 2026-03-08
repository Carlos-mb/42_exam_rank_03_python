# 42_exam_rank_03_python

42 school — Possible rank\_03 Python solutions.

> **Note:** The rank 03 exam for Python is not officially published. This repository contains educated guesses at what the exercises might look like, adapted from the well-known C versions of the exam.

---

## Exercises

### Exercise 00 — ft\_printf

Implement a subset of `printf` in Python.

- Directory: [`ft_printf/`](ft_printf/)
- File: `ft_printf.py`
- Prototype: `def ft_printf(format_string, *args) -> int`

Supported conversions: `%c`, `%s`, `%d`, `%i`, `%u`, `%x`, `%X`, `%o`, `%p`, `%%`

See [`ft_printf/README.md`](ft_printf/README.md) for full details.

---

### Exercise 01 — get\_next\_line

Read one line at a time from a file descriptor.

- Directory: [`get_next_line/`](get_next_line/)
- File: `get_next_line.py`
- Prototype: `def get_next_line(fd, buffer_size=42) -> str | None`

See [`get_next_line/README.md`](get_next_line/README.md) for full details.

---

## Quick start

```bash
# ft_printf
python3 -c "
from ft_printf.ft_printf import ft_printf
ft_printf('Hello, %s! Value: %d\n', 'world', 42)
"

# get_next_line
python3 -c "
import os
from get_next_line.get_next_line import get_next_line
fd = os.open('/etc/hostname', os.O_RDONLY)
print(get_next_line(fd))
os.close(fd)
"
```
