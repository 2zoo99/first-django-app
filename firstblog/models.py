from django.db import models

from django.utils import timezone
from django.conf import settings
# from django.conf import global_settings 아닌가? 

# Create your models here.
class Post(models.Model):
    """
    Post 모델은 블로그 포스트를 나타냅니다.
    properties:
        author
        title
        text
        created_date
        published_date
    methods:
        publish
        __str__
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        # 다른 모델에 대한 외래키를 의미한다.
    title = models.CharField(max_length=200)
        # 글자수가 제한된 텍스트를 정의할때 사용한다.
    text = models.TextField()
        # 글자수 제한이 없는 텍스트를 정의할때 사용한다.
    created_date = models.DateTimeField(default=timezone.now)
        # 날짜와 시간을 의미한다. 
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
            # 포스트를 게시하는 메서드
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title