from django.core.mail import send_mail


def send_confirmation_email(user):
    code = user.activation_code
    full_link = f'http://34.89.166.252/api/v1/accounts/activate/{code}'
    to_email = user.email
    send_mail(
        'Subject here',
        full_link,
        'from @example.com',
        [to_email],
        fail_silently=False,
    )