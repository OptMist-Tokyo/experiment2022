import csv,datetime,logging

def check_and_reg(msg):
    # msgが2022-05-06 14:24,messageのフォーマットに従う場合はそれをパースしてregisterを呼ぶ, そうでない場合は無視する

    msg = msg.split(',')
    if len(msg) != 2:
        return False
    
    ti,message = msg[0],msg[1]
    try:
        ti = datetime.datetime.strptime(ti,"%Y-%m-%d %H:%M")
    except ValueError:
        return False
    
    add_schedule_to_csv(ti.strftime("%Y-%m-%d %H:%M"),message)
    return True

def add_schedule_to_csv(date, content):
    with open("data/schedule.csv", 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["date", "content"])
        writer.writerow({"date":date, "content": content})

def timer(start_time,end_time):
    ret = []
    with open("data/schedule.csv", 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ti = datetime.datetime.strptime(row["date"],"%Y-%m-%d %H:%M")
            if start_time <= ti and ti <= end_time:
                ret.append(row["content"])
    return ret


            

