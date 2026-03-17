import sys

_UINT32_MAX = 2 ** 32
_UINT32_MASK = 0xFFFFFFFF


def ft_printf(format_string, *args):
    """
    A Python equivalent of the C ft_printf function.

    Handles the following conversion specifiers:
        %c  - character
        %s  - string (None is printed as "(null)")
        %d  - signed decimal integer
        %i  - signed decimal integer (same as %d)
        %u  - unsigned decimal integer
        %x  - unsigned hexadecimal integer (lowercase)
        %X  - unsigned hexadecimal integer (uppercase)
        %o  - unsigned octal integer
        %p  - pointer address (hex)
        %%  - literal percent sign

    Returns the total number of characters written to stdout.
    """
    result = []
    arg_idx = 0
    i = 0

    while i < len(format_string):
        if format_string[i] == '%' and i + 1 < len(format_string):
            i += 1
            spec = format_string[i]

            if spec == 's':
                s = str(args[arg_idx]) if args[arg_idx] is not None else '(null)'
                result.append(s)
                arg_idx += 1
            elif spec in ('d', 'i'):
                result.append(str(int(args[arg_idx])))
                arg_idx += 1
            elif spec == 'u':
                val = int(args[arg_idx])
                if val < 0:
                    val = val + _UINT32_MAX
                result.append(str(val))
                arg_idx += 1
            elif spec == 'x':
                result.append(format(int(args[arg_idx]) & _UINT32_MASK, 'x'))
                arg_idx += 1
            elif spec == 'X':
                result.append(format(int(args[arg_idx]) & _UINT32_MASK, 'X'))
                arg_idx += 1
            elif spec == 'o':
                result.append(format(int(args[arg_idx]) & _UINT32_MASK, 'o'))
                arg_idx += 1
            elif spec == 'c':
                ch = args[arg_idx]
                result.append(chr(ch) if isinstance(ch, int) else str(ch))
                arg_idx += 1
            elif spec == 'p':
                result.append(hex(id(args[arg_idx])))
                arg_idx += 1
            elif spec == '%':
                result.append('%')
            else:
                result.append('%')
                result.append(spec)
        else:
            result.append(format_string[i])
        i += 1

    output = ''.join(result)
    sys.stdout.write(output)
    return len(output)
