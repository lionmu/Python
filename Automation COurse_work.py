from ncclient import manager
import json
import xmltodict

#Device Configuration details
device_info = {
    "host": "192.168.0.118",
    "port": 830,
    "username": "lionel", 
    "password": "M@!f@mily2ree",
    "hostkey_verify": False,
    "device_params": {"name": "csr"}
}

try:
#Enabling connection to the switch to unpack the device configuration dictionary
 with manager.connect(**device_info) as connection:
        print("✅ Connected Successfully")

     #Models for both Hostname,interface and Retrieving Device information. 
     # Note: most functionalities like routing, Vlan Operations,DHCP operations have differnt 
     # models  
        Device_config = """
<filter>
<device-hardware-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-device-hardware-oper"/>

    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname/>
    <interface/>
    </native> 
         
</filter>
"""
        # the Device_reply variable storing the Get remote procedure call from the connection made. 
        # to the switch using the models above in the Device_config list
        Device_reply = connection.get(filter=Device_config)
        #The data from the Device_reply.xml stored in a variable dictionary_data converted from
        #xml format to dictionary format which is the output format for Json
        dictionary_data = xmltodict.parse(Device_reply.xml)
        Final_out = json.dumps(dictionary_data, indent=2)
        print("Configuration_Status:")
    
        print(Final_out)
        #error handling if there is a connection error
except manager.transport.SSHError:
    print("❌ SSH connection failed - device may be unreachable")
