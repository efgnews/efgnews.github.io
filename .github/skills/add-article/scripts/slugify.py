#!/usr/bin/env python3
"""Transliterate a Bulgarian title to a URL-safe slug for Hugo post filenames.

Usage:
    python3 slugify.py "Взривеният ликвидатор пречел на мощна групировка от София"
    # → vzriveniyat-likvidator-prechel-na-moshna-grupirovka-ot-sofiya

    python3 slugify.py "1995-05-08" "Взривеният ликвидатор..."
    # → 1995-05-08-vzriveniyat-likvidator-...
"""

import re
import sys

TRANSLIT = {
    'а': 'a',  'б': 'b',  'в': 'v',  'г': 'g',  'д': 'd',
    'е': 'e',  'ж': 'zh', 'з': 'z',  'и': 'i',  'й': 'j',
    'к': 'k',  'л': 'l',  'м': 'm',  'н': 'n',  'о': 'o',
    'п': 'p',  'р': 'r',  'с': 's',  'т': 't',  'у': 'u',
    'ф': 'f',  'х': 'h',  'ц': 'c',  'ч': 'ch', 'ш': 'sh',
    'щ': 'sht','ъ': 'u',  'ь': 'y',  'ю': 'yu', 'я': 'ya',
}


def slugify(title: str) -> str:
    result = []
    for ch in title.lower():
        if ch in TRANSLIT:
            result.append(TRANSLIT[ch])
        elif ch.isascii() and (ch.isalnum() or ch == '-'):
            result.append(ch)
        elif ch in (' ', '_'):
            result.append('-')
        # drop everything else (punctuation, quotes, etc.)
    slug = re.sub(r'-{2,}', '-', ''.join(result)).strip('-')
    return slug


if __name__ == '__main__':
    if len(sys.argv) == 3:
        date, title = sys.argv[1], sys.argv[2]
        print(f"{date}-{slugify(title)}")
    elif len(sys.argv) == 2:
        print(slugify(sys.argv[1]))
    else:
        print(__doc__)
        sys.exit(1)
