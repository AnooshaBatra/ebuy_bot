from core.models import EBUYRFQ
from django.db import connection

count= EBUYRFQ.objects.count()
inf_name=""
inf_source= ""
las_run= " "
table_count= ""
run_time= ""
statu= ""
current_statu= " "
log_err = " "
log= EBUYRFQ(
    info_name=inf_name,
    info_source=inf_source,
    last_run=las_run,
    tables_count=str(table_count),
    total_run_time=run_time,
    status= statu,
    current_status=current_statu,
    log_error=log_err,
    count = str(count),
    bot_name= "eb"
)



log.save(force_insert=True)
log= EBUYRFQ(
    info_name= "unknwon",
    info_source="unknown",
    last_run=las_run,
    tables_count= "9",
    total_run_time=" ",
    status= " unknown",
    current_status= "unknwon",
    log_error= "error",
    count = str(count)
)
