# ft_printf

## Subject

Write a function named `ft_printf` that behaves similarly to the C `printf` function.

### Prototype

```python
def ft_printf(format_string, *args) -> int:
```

### Supported conversions

| Specifier | Description |
|-----------|-------------|
| `%c`      | Print a single character |
| `%s`      | Print a string (`None` is printed as `(null)`) |
| `%d`      | Print a signed decimal integer |
| `%i`      | Print a signed decimal integer |
| `%u`      | Print an unsigned decimal integer |
| `%x`      | Print an unsigned hexadecimal integer (lowercase) |
| `%X`      | Print an unsigned hexadecimal integer (uppercase) |
| `%o`      | Print an unsigned octal integer |
| `%p`      | Print a pointer address |
| `%%`      | Print a literal percent sign |

### Return value

Returns the total number of characters written to stdout.

## Usage

```python
from ft_printf import ft_printf

n = ft_printf("Hello, %s! You are %d years old.\n", "Alice", 30)
# Output: Hello, Alice! You are 30 years old.
# n == 38

ft_printf("Hex: %x  Oct: %o  Unsigned: %u\n", 255, 255, 255)
# Output: Hex: ff  Oct: 377  Unsigned: 255
```

## Files

- `ft_printf.py` — implementation
