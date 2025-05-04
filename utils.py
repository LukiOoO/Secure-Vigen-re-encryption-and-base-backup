import sqlite3


def get_db(db_path: str) -> sqlite3.Connection:
    conn: sqlite3.Connection = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path: str) -> None:
    db = get_db(db_path)
    db.execute(
        '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
        '''
    )
    db.commit()


def vigenere_encrypt(plain: str, key: str) -> str:
    result_chars: list[str] = []
    key_upper: str = key.upper()
    key_index: int = 0
    for ch in plain:
        if ch.isalpha():
            base: str = 'A' if ch.isupper() else 'a'
            shift: int = (
                (ord(ch) - ord(base) +
                 (ord(key_upper[key_index % len(key_upper)]) - ord('A')))
                % 26
            )
            result_chars.append(chr(shift + ord(base)))
            key_index += 1
        else:
            result_chars.append(ch)
    return ''.join(result_chars)


def vigenere_decrypt(cipher: str, key: str) -> str:
    result_chars: list[str] = []
    key_upper: str = key.upper()
    key_index: int = 0
    for ch in cipher:
        if ch.isalpha():
            base: str = 'A' if ch.isupper() else 'a'
            shift: int = (
                (ord(ch) - ord(base) -
                 (ord(key_upper[key_index % len(key_upper)]) - ord('A')))
                % 26
            )
            result_chars.append(chr(shift + ord(base)))
            key_index += 1
        else:
            result_chars.append(ch)
    return ''.join(result_chars)
