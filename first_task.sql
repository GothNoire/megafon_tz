--1)
select s.srv_id
from server_hdd sh
     ,servers s
where sh.srv_id = s.srv_id
group by s.srv_id
having sum (sh.hdd_capacity) > 110 and sum (sh.hdd_capacity) < 130;

--2)
delete from server_hdd sh
where rowid in (select rowid
               from (select rowid
                    ,row_number() over (partition by sh.hdd_capacity, sh.srv_id, sh.hdd_name order by sh.hdd_id) as r
                    from server_hdd sh)t1
               where t1.r >1
               );

--3) Триггер, который будет проверять наличие вставляемой строки

--4)
with t as (
select s.srv_name
       , sh.hdd_name
       , sh.hdd_capacity
       , lag(hm.used_space, 1)  over (partition by sh.srv_id order by null) pred_used_space
       , hm.used_space
       ,hm.monitoring_date
       ,row_number() over (partition by sh.hdd_id order by sh.srv_id, hm.monitoring_date) i
from hdd_monitoring hm
     ,server_hdd sh
     ,servers s
where hm.hdd_id =sh.hdd_id
  and s.srv_id = sh.srv_id
  and sh.hdd_capacity in
  (select max (sh.hdd_capacity)
  from server_hdd sh
  group by sh.srv_id)
  order by sh.srv_id, hm.monitoring_date
)
select * from t
where t.i <10