-- Write your query below
WITH exam_results_highest AS (
    SELECT *, ROW_NUMBER() OVER(PARTITION BY student_id ORDER BY score DESC, exam_id) AS row_num
    FROM exam_results
)

SELECT student_id, exam_id, score
FROM exam_results_highest
WHERE row_num = 1
ORDER BY student_id