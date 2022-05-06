import csv

def add_schedule_to_csv(date, content):
    with open("src/data/schedule.csv", 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["date", "content"])
        writer.writerow({"date":date, "content": content})
