select *
from world_layoff.layoffs_staging;

select company , location , industry , total_laid_off , `date` , country , stage 
, row_number() over(partition by company , location , industry ,total_laid_off , `date` , country , funds_raised_millions) as row_num
from world_layoff.layoffs_staging;

select *
from (
select company , location , industry , total_laid_off , `date` , country , stage , funds_raised_millions
, row_number() over(partition by company , location , industry ,total_laid_off , `date` , country , funds_raised_millions) as row_num
from world_layoff.layoffs_staging

)  duplicates
where
  row_num > 1;
  
  
  select distinct *  from world_layoff.layoffs_staging where company = "oda" ;
  
  create table world_layoff.layoffs_staging2(
  company text,
  location text,
  industry text,
  total_laid_off int,
  percentage_laid_off text,
  `date` text,
  stage text,
  country text,
  funds_raised_millions int,
  row_num int 
  );
  
  insert into world_layoff.layoffs_staging2 (
   company ,
  location ,
  industry ,
  total_laid_off ,
  percentage_laid_off ,
  `date` ,
  stage ,
  country ,
  funds_raised_millions ,
  row_num  
  )
  select
   company ,
  location ,
  industry ,
  total_laid_off ,
  percentage_laid_off ,
  `date` ,
  stage ,
  country ,
  funds_raised_millions ,
  row_number() over(partition by company , location , industry ,total_laid_off,percentage_laid_off , `date` , country , funds_raised_millions) as row_num
    from world_layoff.layoffs_staging;
    
   drop table world_layoff.layoffs_staging2; 
    select * 
    from world_layoff.layoffs_staging2;
    
    
    
delete from world_layoff.layoffs_staging2
where row_num >= 2 ;
  
  select distinct industry
  from world_layoff.layoffs_staging2
  order by industry;
  
  select *
  from world_layoff.layoffs_staging2
  where industry is null
  or industry = ""
  order by industry;
  
  select * 
  from layoffs_staging2
  where company like "bally%"
  order by industry;
  
  update layoffs_staging2
  set industry = null
  where industry = "";
  
  update layoffs_staging2 t1
  join layoffs_staging2 t2
  set t1.industry = t2.industry
  where t1.industry is null 
  and t2.industry is not null;
  
  select * from layoffs_staging2;
  
  update layoffs_staging2
  set industry = "Crypto"
  where industry in ("CryptoCurrency" , "Crypto Currency");
 
 select distinct country from layoffs_staging2
 order by country;
 
 update layoffs_staging2
 set country = trim(trailing "." from country);
 
 update layoffs_staging2
 set `date` = str_to_date(`date` , '%m/%d/%y');
 
 UPDATE layoffs_staging2
SET `date` = STR_TO_DATE(`date`, '%m/%d/%Y');

alter table layoffs_staging2
modify column `date` date;

select * from layoffs_staging2;


delete from layoffs_staging2
where total_laid_off is null
and percentage_laid_off is null ;

alter table layoffs_staging2
drop column row_num;






  
  
  
  
  