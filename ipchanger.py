#This is a python!!

f = open("/boot/config.txt", 'r')
a=f.readline()
a2 = a.replace("\n", "")
print(a2)

ethIndex = 0
def change_static_ip(ip_address):
    ethIndex = 0
    conf_file = '/etc/dhcpcd.conf'
       
    # Sanitize/validate params above
    with open(conf_file, 'r') as file:
        data = file.readlines()

    # Find if config exists
    ethFound = next((x for x in data if 'interface eth0' in x), None)

    if ethFound:
        ethIndex = data.index(ethFound)
        if data[ethIndex].startswith('#'):
            data[ethIndex].replace('#', '') # commented out by default, make active

    # If config is found, use index to edit the lines you need ( the next 3)
    if ethIndex:
        data[ethIndex+1] = f'static ip_address={ip_address}/24\n'

    with open(conf_file, 'w') as file:
        file.writelines( data )


        
change_static_ip(a2)