import threading
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def send_contact_email_async(name, sender_email, subject, message):
    def _send():
        owner = getattr(settings, "CONTACT_EMAIL", None) or getattr(settings, "DEFAULT_FROM_EMAIL", None)
        from_addr = getattr(settings, "DEFAULT_FROM_EMAIL", None)

        if not owner or not from_addr:
            print("CONTACT_EMAIL or DEFAULT_FROM_EMAIL not configured.")
            return

        # ✅ Clean up the sender email before using it
        sender_email_clean = str(sender_email).strip()
        try:
            validate_email(sender_email_clean)
        except ValidationError:
            print(f"Invalid sender email: {sender_email_clean}")
            return

        # --- Notify site owner ---
        owner_subject = f"[Contact] {subject}"
        owner_body = (
            f"You received a new message from your contact form.\n\n"
            f"From: {name} <{sender_email_clean}>\n"
            f"Subject: {subject}\n\n"
            f"Message:\n{message}\n\n"
            f"---\nThis message delivered asynchronously via thread."
        )

        owner_email = EmailMessage(
            subject=owner_subject,
            body=owner_body,
            from_email=from_addr,
            to=[owner],
            reply_to=[sender_email_clean]
        )
        owner_email.send(fail_silently=False)

        # --- Auto-reply ---
        reply_subject = "Thank You for Contacting Sarah Foundation"
        reply_body = (
            f"Dear {name},\n\n"
            "Thank you for reaching out to Sarah Foundation. We’ve received your message and truly appreciate your interest in our work.\n\n"
            "Here’s a quick summary of your message:\n\n"
            f"Subject: {subject}\n"
            f"Message: {message}\n\n"
            "Our team will review your message and respond as soon as possible. "
            "If your inquiry is urgent, kindly include 'URGENT' in the subject line when replying.\n\n"
            "Together, we can continue to spread hope and create lasting impact.\n\n"
            "Warm regards,\n"
            "— The Sarah Foundation Team"
        )

        acknowledgement = EmailMessage(
            subject=reply_subject,
            body=reply_body,
            from_email=from_addr,
            to=[sender_email_clean]
        )
        acknowledgement.send(fail_silently=False)

    threading.Thread(target=_send).start()
