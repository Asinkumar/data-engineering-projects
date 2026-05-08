SELECT
    DATE(invoice_date)              AS sale_date,
    EXTRACT(MONTH FROM invoice_date) AS sale_month,
    EXTRACT(YEAR FROM invoice_date)  AS sale_year,
    country,
    COUNT(DISTINCT InvoiceNo)        AS total_orders,
    COUNT(DISTINCT customer_id)      AS unique_customers,
    SUM(Quantity)                    AS total_items_sold,
    ROUND(SUM(revenue), 2)           AS total_revenue,
    ROUND(AVG(revenue), 2)           AS avg_order_value
FROM {{ ref('stg_ecommerce') }}
GROUP BY
    sale_date,
    sale_month,
    sale_year,
    country
ORDER BY
    sale_date DESC