import os

_buffers = {}


def get_next_line(fd, buffer_size=42):
    """
    A Python equivalent of the C get_next_line function.

    Reads the next line from the file descriptor `fd`.
    Returns the line including the newline character '\\n' if present,
    or the remaining content without '\\n' at end-of-file.
    Returns None when there is nothing left to read.

    Uses an internal per-fd buffer to handle partial reads correctly.
    The optional `buffer_size` controls how many bytes are read at a time
    (default: 42, matching the common 42-school BUFFER_SIZE).
    """
    global _buffers

    if fd not in _buffers:
        _buffers[fd] = ''

    while '\n' not in _buffers[fd]:
        try:
            chunk = os.read(fd, buffer_size)
        except OSError:
            break
        if not chunk:
            break
        _buffers[fd] += chunk.decode('utf-8', errors='replace')

    if not _buffers[fd]:
        return None

    if '\n' in _buffers[fd]:
        newline_pos = _buffers[fd].index('\n')
        line = _buffers[fd][:newline_pos + 1]
        _buffers[fd] = _buffers[fd][newline_pos + 1:]
    else:
        line = _buffers[fd]
        _buffers[fd] = ''

    return line
