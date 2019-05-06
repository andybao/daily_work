import json

json_string = '{"0":{"aim":"00124B0006127618 (asset pnubdmdv)","event_type":"Temperature","timestampUrl":"http://iot.d.chainvu.com/admin/aim/aimlogentry/376422/change/","timestamp":"2019-05-03 08:55:29"},"1":{"aim":"00124B0006127618 (asset pnubdmdv)","event_type":"Temperature","timestampUrl":"http://iot.d.chainvu.com/admin/aim/aimlogentry/376421/change/","timestamp":"2019-05-03 08:17:04"},"2":{"aim":"00124B0006127618 (asset pnubdmdv)","event_type":"Temperature","timestampUrl":"http://iot.d.chainvu.com/admin/aim/aimlogentry/376420/change/","timestamp":"2019-05-02 11:58:32"},"3":{"aim":"00124B0006127618 (asset pnubdmdv)","event_type":"Temperature","timestampUrl":"http://iot.d.chainvu.com/admin/aim/aimlogentry/376419/change/","timestamp":"2019-05-01 12:42:13"},"4":{"aim":"00124B0006127618 (asset pnubdmdv)","event_type":"Temperature","timestampUrl":"http://iot.d.chainvu.com/admin/aim/aimlogentry/376418/change/","timestamp":"2019-05-01 12:13:17"},"5":{"aim":"00124B0006127618 (asset pnubdmdv)","event_type":"Temperature","timestampUrl":"http://iot.d.chainvu.com/admin/aim/aimlogentry/376417/change/","timestamp":"2019-05-01 12:13:14"},"end":"Avengers"}'

json_dict = json.loads(json_string)

print(type(json_dict['0']))
print(json_dict['0']['timestamp'])