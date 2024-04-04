from producer_interface import mqProducerInterface
import pika
import os


class mqProducer(mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        # Save parameters to class variables
        self.routing_key = routing_key
        self.exchange_name = exchange_name

        # Call setupRMQConnection
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
    
        # Establish Channel
        self.channel = connection.channel()

        # Create the exchange if not already present
        self.channel.exchange_declare(self.exchange_name) #self.exchange_name ??


    def publishOrder(self, message: str) -> None:
        # Basic Publish to Exchange
        self.channel.basic_publish(message)

        # Close Channel
        self.channel.close()

        # Close Connection
        self.connection.close()