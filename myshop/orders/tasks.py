from celery import task
from django.core.mail import send_mail, EmailMessage
from .models import Order

@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order no. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'
    mail_sent = EmailMessage(subject, message, 'pradhan.soman133@gmail.com', [order.email])
    return mail_sent