-- 코드를 입력하세요
SELECT round(avg(c1.daily_fee), 0)
FROM CAR_RENTAL_COMPANY_CAR as c1 
WHERE c1.car_type = 'SUV'
GROUP BY c1.car_type
