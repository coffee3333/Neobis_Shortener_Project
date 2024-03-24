from django.db import models
import uuid
import base58

class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_id = models.CharField(max_length=22, unique=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_id:
            uuid_ = uuid.uuid4()
            self.short_id = base58.b58encode(uuid_.bytes).decode('utf-8')
        super(ShortenedURL, self).save(*args, **kwargs)