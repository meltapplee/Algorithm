SELECT AO.animal_id, AO.name
FROM ANIMAL_OUTS AS AO
	LEFT JOIN ANIMAL_INS AS AI
	ON AO.animal_id = AI.animal_id
WHERE AI.animal_id IS NULL;