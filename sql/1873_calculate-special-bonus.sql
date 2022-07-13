select 
    employee_id
    , case when 
        upper(left(name, 1)) <> "M" and (employee_id mod 2) = 1 then salary 
        else 0 
        end as bonus
    from employees
    order by employee_id