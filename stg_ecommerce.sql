SELECT
    InvoiceNo,
    StockCode,
    INITCAP(Description)           AS description,
    Quantity,
    CAST(InvoiceDate AS TIMESTAMP)  AS invoice_date,
    UnitPrice                       AS unit_price,
    CAST(CustomerID AS INT64)       AS customer_id,
    INITCAP(Country)                AS country,
    ROUND(Quantity * UnitPrice, 2)  AS revenue
FROM {{ source('E_commerce', 'raw_ecommerce') }}
WHERE
    CustomerID IS NOT NULL
    AND Quantity > 0
    AND UnitPrice > 0
    AND NOT STARTS_WITH(
        CAST(InvoiceNo AS STRING), 'C')