SELECT concat (NAME,'(', substr(OCCUPATION, 1, 1), ')' ) FROM OCCUPATIONS ORDER BY NAME;
SELECT concat('There are total ', count(OCCUPATION), ' ', lower(OCCUPATION) ) FROM OCCUPATIONS 
    GROUP BY OCCUPATION ORDER BY count(OCCUPATION), OCCUPATION;