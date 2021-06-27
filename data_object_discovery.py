import sys
import pandas

import pm4py.objects.log.importer.xes

log = pm4py.objects.log.importer.xes.importer.apply('Road.xes')
print(log)



def find_first_non_empty_event(case):
    for event in case:
        if not event["vehicleClass"].startswith("User"):
            return event
            break
    return None

file = open('vehicleClass.csv', 'a')
sys.stdout = file
for case in log:
    if len(case) < 2:
        continue
    old_event = find_first_non_empty_event(case)
    if old_event is None:
        continue
    print(case.attributes["concept:name"], ",", old_event["time:timestamp"], ",", old_event["concept:name"],
          ",", old_event["vehicleClass"])
    for event in case:
        if event["vehicleClass"] != old_event["vehicleClass"] and not event["vehicleClass"].startswith("User"):

            print(case.attributes["concept:name"], ",", event["time:timestamp"], ",", event["concept:name"], ",", event["vehicleClass"])

            old_event = event
            break
file.close()
