rabbitmqctl -n  set_parameter shovel demoo_shovel '{"src-protocol": "amqp091", "src-uri": "amqp://", "src-queue": "demo_queue", "dest-protocol": "amqp091", "dest-uri": "amqp://guest:guest@rabbitmq_downstream", "dest-queue": "demo_queue_2"}'
