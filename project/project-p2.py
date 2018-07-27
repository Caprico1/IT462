from pysnmp.entity.rfc3413.oneliner import cmdgen


'''
Queries all varibles and prints them out to a file if a file name is specified

usage: python project-p2.py 

to save to file:

python project-p2.py > [filename]
'''

cg = cmdgen.CommandGenerator()
comm_data = cmdgen.CommunityData('my-manager', 'public')
transport = cmdgen.UdpTransportTarget(('127.0.0.1', 161))
variables = (1, 3, 6, 1, 2, 1)
errIndication, errStatus, errIndex, result = cg.nextCmd(comm_data, transport, variables)

if errIndication:
    print(errIndication)
    print(errIndex)
    print(errStatus)
else:
    for object in result:
        for i in range(len(object)):
            print(object[i])