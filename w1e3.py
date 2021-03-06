 #Excersise 3, week 1.

__author__ = 'rafael'

from snmp_helper import snmp_get_oid, snmp_extract

community_string = '******'
oids = {'RunningLastChanged': '1.3.6.1.4.1.9.9.43.1.1.1.0',
        'StartupLastChanged': '1.3.6.1.4.1.9.9.43.1.1.3.0'}
port = '*****'
ip_addr = '******'


def extract_data(node, oid):
    """Returns an OID object from a given device and SNMP OID."""
    return snmp_extract(snmp_get_oid(node, oid))


def main():
    """Create an SNMP devices and retrieves a specific OID object from lists"""
    device = (ip_addr, community_string, port)
    print 'CHECKING STARTUP-CONFIG STATUS FOR DEVICE %s:%s\n'% (ip_addr, port)
    running_change = extract_data(device, oids['RunningLastChanged'])
    start_change = extract_data(device, oids['StartupLastChanged'])
    print 'Uptime when running config last changed:\n%s\n' % running_change
    print 'Uptime when startup config last saved :\n%s\n' % start_change

    if int(running_change) > int(start_change) == 0:
        print 'Warning! Startup-config has not been saved since the last boot!'
    elif int(running_change) > int(start_change):
        print 'Warning! Running-config change with no save!'
    else:
        print 'The current running-config is saved.'

if __name__ == "__main__":
    main()
