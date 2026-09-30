from django.db import models

class ContactMessage(models.Model):
    name = models.CharField("Nom complet", max_length=150)
    email = models.EmailField("Adresse email")
    phone = models.CharField("Numéro de téléphone", max_length=50, blank=True)
    subject = models.CharField("Sujet", max_length=200)
    message = models.TextField("Message")
    is_read = models.BooleanField("Message traité / lu", default=False)
    created_at = models.DateTimeField("Reçu le", auto_now_add=True)

    class Meta:
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.subject} - {self.name}"
