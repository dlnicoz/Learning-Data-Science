select * 
from world_layoff.layoffs_staging2;

select max(total_laid_off),min(total_laid_off)
from world_layoff.layoffs_staging2;

select min(percentage_laid_off)as mp, max(percentage_laid_off) 
,avg(percentage_laid_off);

select * 
from layoffs_staging2 
where percentage_laid_off
;
select *
from layoffs_staging2
where country = "India"
order by total_laid_off desc;
;

select company , total_laid_off
from layoffs_staging2
where percentage_laid_off = 1
order by 2 desc 
limit 5;

select company , sum(total_laid_off)
from layoffs_staging2
group by company
order by 2 desc 
limit 10;

select location , sum(total_laid_off)
from layoffs_staging2
group by location
order by 2 desc
limit 10
;

select stage , sum(total_laid_off)
from layoffs_staging2
group by stage
order by 2 desc;


select country , sum(total_laid_off)
from layoffs_staging2
group by country
order by 2 desc
limit 10
;

select year(date) as dat , sum(total_laid_off)
from layoffs_staging2
group by year(date)
order by 1 asc;

SELECT company, YEAR(date) AS years, SUM(total_laid_off) AS total_laid_off
  FROM layoffs_staging2
  GROUP BY company, YEAR(date);

WITH Company_Year AS 
(
  SELECT company, YEAR(date) AS years, SUM(total_laid_off) AS total_laid_off
  FROM layoffs_staging2
  GROUP BY company, YEAR(date)
)
, Company_Year_Rank AS (
  SELECT company, years, total_laid_off, DENSE_RANK() OVER (PARTITION BY years ORDER BY total_laid_off DESC) AS ranking
  FROM Company_Year
)
SELECT company, years, total_laid_off, ranking
FROM Company_Year_Rank
WHERE ranking <= 3
AND years IS NOT NULL
ORDER BY years ASC, total_laid_off DESC;



with company_year as
(
select company , year(date) years , sum(total_laid_off) as total_laid_off
from layoffs_staging2
group by company , year(date)
), company_year_rank as
(
select company , years , total_laid_off, dense_rank() over(partition by years order by total_laid_off desc) as ranking
from company_year
)
select company , years , total_laid_off , ranking
from company_year_rank
where ranking <= 3
and years is not null
order by years asc , total_laid_off desc
;

SELECT substring(date,1,7) as dates, SUM(total_laid_off) AS total_laid_off
FROM layoffs_staging2
where date is not null
GROUP BY dates
ORDER BY dates ASC;

WITH DATE_CTE AS 
(
SELECT SUBSTRING(date,1,7) as dates, SUM(total_laid_off) AS total_laid_off
FROM layoffs_staging2

GROUP BY dates
ORDER BY dates ASC
)
SELECT dates, SUM(total_laid_off) OVER (ORDER BY dates ASC) as rolling_total_layoffs
FROM DATE_CTE
where dates is not null
ORDER BY dates ASC;




