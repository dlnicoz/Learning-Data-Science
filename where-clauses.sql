select * from employee_salary
where first_name = 'ron';

select age ,
first_name
 from employee_demographics
where gender = 'male';

select * 
from employee_salary
where salary > 40000
;

select * 
from employee_demographics 
where gender = 'female'

;

select *
from employee_demographics 
where (first_name = 'chris') or age > 34
;

#like statement
select *
from employee_demographics 
where first_name like '%y'
;



