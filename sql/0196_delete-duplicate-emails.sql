delete p1
    from person p1
    where 
        p1.id not in 
            (select id from 
                (select min(id) id from person group by email) p)
