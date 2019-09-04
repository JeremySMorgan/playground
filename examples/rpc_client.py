import a0
import time

tm = a0.TopicManager('''{
    "container": "bar",
    "rpc_client_maps": {
        "drive_in_circles": {
            "container": "stuff_doer",
            "topic": "navigate"
        }
    }
}''')

client = a0.RpcClient(tm.rpc_client_topic('drive_in_circles'))

def callback(pkt):
	print('Recieved reply:', pkt.payload)

print('Awaiting for 0.01 sec')
client.send('Please do!', callback)
time.sleep(0.01)
print('Done!')