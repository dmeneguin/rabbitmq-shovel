import requests

RABBITMQ_USER='guest'
RABBITMQ_PASS='guest'

payload={"component":"shovel","vhost":"/","name":"asdd","value":{"src-uri":"amqp://","dest-uri":"amqp://guest:guest@rabbitmq_downstream:5673","ack-mode":"on-confirm","src-protocol":"amqp091","dest-protocol":"amqp091","src-queue":"demo_queue","src-delete-after":"never","dest-queue":"demo_queue_2","dest-add-forward-headers":False}}

client_auth = requests.auth.HTTPBasicAuth(RABBITMQ_USER,RABBITMQ_PASS)

response = requests.put("http://localhost:15672/api/parameters/shovel/%2F/demo_shovel",auth=client_auth,json=payload)

print(response)