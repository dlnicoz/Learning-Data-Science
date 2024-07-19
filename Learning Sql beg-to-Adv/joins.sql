select * 
from employee_demographics
;

select  *
from employee_salary ,parks_departments
;
select * 
from employee_demographics 
cross join employee_salary sal
   on employee_demographics.employee_id = sal.dept_id
   ;
   
select *
from employee_demographics as demo
cross join employee_salary as sal
on demo.employee_id = sal.employee_id
;
