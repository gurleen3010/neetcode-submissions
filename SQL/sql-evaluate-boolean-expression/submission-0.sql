SELECT
    e.left_operand,
    e.operator,
    e.right_operand,
    CASE
        WHEN e.operator = '>' THEN l.value > r.value
        WHEN e.operator = '<' THEN l.value < r.value
        ELSE l.value = r.value
    END AS value
FROM expressions e
LEFT JOIN variables l
    ON e.left_operand = l.name
LEFT JOIN variables r
    ON e.right_operand = r.name;