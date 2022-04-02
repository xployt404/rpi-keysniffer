NULL =  0x00
ENTER = 0x28
SHIFT = 0x02

# layout format: (keycode, modifier)
# US keyboard layout
US = {
    'a':  (0x04, NULL), 'A':  (0x04, SHIFT),
    'b':  (0x05, NULL), 'B':  (0x05, SHIFT), 
    'c':  (0x06, NULL), 'C':  (0x06, SHIFT),
    'd':  (0x07, NULL), 'D':  (0x07, SHIFT),
    'e':  (0x08, NULL), 'E':  (0x08, SHIFT),
    'f':  (0x09, NULL), 'F':  (0x09, SHIFT),
    'g':  (0x0a, NULL), 'G':  (0x0a, SHIFT),
    'h':  (0x0b, NULL), 'H':  (0x0b, SHIFT),
    'i':  (0x0c, NULL), 'I':  (0x0c, SHIFT),
    'j':  (0x0d, NULL), 'J':  (0x0d, SHIFT),
    'k':  (0x0e, NULL), 'K':  (0x0e, SHIFT),
    'l':  (0x0f, NULL), 'L':  (0x0f, SHIFT),
    'm':  (0x10, NULL), 'M':  (0x10, SHIFT),
    'n':  (0x11, NULL), 'N':  (0x11, SHIFT),
    'o':  (0x12, NULL), 'O':  (0x12, SHIFT),
    'p':  (0x13, NULL), 'P':  (0x13, SHIFT),
    'q':  (0x14, NULL), 'Q':  (0x14, SHIFT),
    'r':  (0x15, NULL), 'R':  (0x15, SHIFT),
    's':  (0x16, NULL), 'S':  (0x16, SHIFT),
    't':  (0x17, NULL), 'T':  (0x17, SHIFT),
    'u':  (0x18, NULL), 'U':  (0x18, SHIFT),
    'v':  (0x19, NULL), 'V':  (0x19, SHIFT),
    'w':  (0x1a, NULL), 'W':  (0x1a, SHIFT),
    'x':  (0x1b, NULL), 'X':  (0x1b, SHIFT),
    'y':  (0x1c, NULL), 'Y':  (0x1c, SHIFT),
    'z':  (0x1d, NULL), 'Z':  (0x1d, SHIFT),
    '1':  (0x1e, NULL), '!':  (0x1e, SHIFT),
    '2':  (0x1f, NULL), '@':  (0x1f, SHIFT),
    '3':  (0x20, NULL), '#':  (0x20, SHIFT),
    '4':  (0x21, NULL), '$':  (0x21, SHIFT),
    '5':  (0x22, NULL), '%':  (0x22, SHIFT),
    '6':  (0x23, NULL), '^':  (0x23, SHIFT),
    '7':  (0x24, NULL), '&':  (0x24, SHIFT),
    '8':  (0x25, NULL), '*':  (0x25, SHIFT),
    '9':  (0x26, NULL), '(':  (0x26, SHIFT),
    '0':  (0x27, NULL), ')':  (0x27, SHIFT),
    ' ':  (0x2c, NULL),
    '-':  (0x2d, NULL), '_':  (0x2d, SHIFT),
    '=':  (0x2e, NULL), '+':  (0x2e, SHIFT),
    '[':  (0x2f, NULL), '{':  (0x2f, SHIFT),
    ']':  (0x30, NULL), '}':  (0x30, SHIFT),
    '\\': (0x31, NULL), '|':  (0x31, SHIFT),
    ';':  (0x33, NULL), ':':  (0x33, SHIFT),
    '\'': (0x34, NULL), '"':  (0x34, SHIFT),
    '`':  (0x35, NULL), '~':  (0x35, SHIFT),
    ',':  (0x36, NULL), '<':  (0x36, SHIFT),
    '.':  (0x37, NULL), '>':  (0x37, SHIFT),
    '/':  (0x38, NULL), '?':  (0x38, SHIFT)
}

# DE keyboard layout
DE = {
    'a':  (0x04, NULL), 'A':  (0x04, SHIFT),
    'b':  (0x05, NULL), 'B':  (0x05, SHIFT), 
    'c':  (0x06, NULL), 'C':  (0x06, SHIFT),
    'd':  (0x07, NULL), 'D':  (0x07, SHIFT),
    'e':  (0x08, NULL), 'E':  (0x08, SHIFT),
    'f':  (0x09, NULL), 'F':  (0x09, SHIFT),
    'g':  (0x0a, NULL), 'G':  (0x0a, SHIFT),
    'h':  (0x0b, NULL), 'H':  (0x0b, SHIFT),
    'i':  (0x0c, NULL), 'I':  (0x0c, SHIFT),
    'j':  (0x0d, NULL), 'J':  (0x0d, SHIFT),
    'k':  (0x0e, NULL), 'K':  (0x0e, SHIFT),
    'l':  (0x0f, NULL), 'L':  (0x0f, SHIFT),
    'm':  (0x10, NULL), 'M':  (0x10, SHIFT),
    'n':  (0x11, NULL), 'N':  (0x11, SHIFT),
    'o':  (0x12, NULL), 'O':  (0x12, SHIFT),
    'p':  (0x13, NULL), 'P':  (0x13, SHIFT),
    'q':  (0x14, NULL), 'Q':  (0x14, SHIFT),
    'r':  (0x15, NULL), 'R':  (0x15, SHIFT),
    's':  (0x16, NULL), 'S':  (0x16, SHIFT),
    't':  (0x17, NULL), 'T':  (0x17, SHIFT),
    'u':  (0x18, NULL), 'U':  (0x18, SHIFT),
    'v':  (0x19, NULL), 'V':  (0x19, SHIFT),
    'w':  (0x1a, NULL), 'W':  (0x1a, SHIFT),
    'x':  (0x1b, NULL), 'X':  (0x1b, SHIFT),
    'z':  (0x1c, NULL), 'Z':  (0x1c, SHIFT),
    'y':  (0x1d, NULL), 'Y':  (0x1d, SHIFT),
    '1':  (0x1e, NULL), '!':  (0x1e, SHIFT),
    '2':  (0x1f, NULL), '"':  (0x1f, SHIFT),
    '3':  (0x20, NULL), '§':  (0x20, SHIFT),
    '4':  (0x21, NULL), '$':  (0x21, SHIFT),
    '5':  (0x22, NULL), '%':  (0x22, SHIFT),
    '6':  (0x23, NULL), '&':  (0x23, SHIFT),
    '7':  (0x24, NULL), '/':  (0x24, SHIFT),
    '8':  (0x25, NULL), '(':  (0x25, SHIFT),
    '9':  (0x26, NULL), ')':  (0x26, SHIFT),
    '0':  (0x27, NULL), '=':  (0x27, SHIFT),
'ENTER':  (0x28, NULL),
    ' ':  (0x2c, NULL),
    'ß':  (0x2d, NULL), '?':  (0x2d, SHIFT),
    '´':  (0x2e, NULL), '`':  (0x2e, SHIFT),
    'ü':  (0x2f, NULL), 'Ü':  (0x2f, SHIFT),
    '+':  (0x30, NULL), '*':  (0x30, SHIFT),
    '#':  (0x31, NULL), '\'': (0x31, SHIFT),
    'ö':  (0x33, NULL), 'Ö':  (0x33, SHIFT),
    'ä':  (0x34, NULL), 'Ä':  (0x34, SHIFT),
    '^':  (0x35, NULL), '°':  (0x35, SHIFT),
    ',':  (0x36, NULL), ';':  (0x36, SHIFT),
    '.':  (0x37, NULL), ':':  (0x37, SHIFT),
    '-':  (0x38, NULL), '_':  (0x38, SHIFT)
}
