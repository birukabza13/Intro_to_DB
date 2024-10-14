USE alx_book_store;

SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM
    information_schemas.COLUMNS
WHERE
    TABLE_NAME = books
    and TABLE_SCHEMA = 'alx_book_store';