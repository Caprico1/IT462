import wmi, ctypes, sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAdmin()
    finally:
        return False

'''
Gets all interfaces and returns them in an array and prints to terminal.

:returns Array
'''


def get_interfaces():
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
    result = []
    i = 0

    for interface in nic_configs:
        result.append(interface)
        print(i, interface.Description, interface.MACAddress)
        for ip_address in interface.IPAddress:
            print(ip_address)
        print()
        i += 1

    return result


def display_interface(interf):
    nic = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)[interf]

    print(nic.Description, nic.MACAddress)
    for ip_address in nic.IPAddress:
        print(ip_address)
    print()


'''
Set the IP of the interface from user input.


:param interf (int)
:param ip (string) U
:param subnet (string) U
:param gateway (string)
:returns string
'''


def set_ip(interf, ip, subnet, gateway):
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

    interface = nic_configs[interf]

    static = interface.EnableStatic(IPAddress=[ip], SubnetMask=[subnet])
    interface.SetGateways(DefaultIPGateway=[gateway])
    print("STATIC")
    print(static)
    print()

def reset_to_dhcp(interf):
    interface = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)[interf]

    interface.EnableDHCP()


if __name__ == "__main__":

    if is_admin():
        nics = get_interfaces()

        interface = int(input("Select an interface #: "))

        ip = input("Enter IP Address: ")

        subnet = input("Enter Subnet Mask: ")

        gateway = input("Enter Gateway Address: ")

        set_ip(interf=interface, ip=ip, subnet=subnet, gateway=gateway)

        display_interface(interface)

        reset = input("Reset to DHCP? (Y/N): ")

        if reset == "Y":
            reset_to_dhcp(interface)
        exit()

    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

        nics = get_interfaces()

        interface = int(input("Select an interface #: "))

        ip = input("Enter IP Address: ")

        subnet = input("Enter Subnet Mask: ")

        gateway = input("Enter Gateway Address: ")

        set_ip(interf=interface, ip=ip, subnet=subnet, gateway=gateway)

        display_interface(interface)

        reset = input("Reset to DHCP? (Y/N): ")

        if reset == "Y":
            reset_to_dhcp(interface)
        exit()
