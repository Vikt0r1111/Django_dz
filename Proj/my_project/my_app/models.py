from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=[('Техніка', 'Техніка'), ('Подорожі', 'Подорожі'), ('Спорт', 'Спорт')])

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)  # Assuming no authentication system
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name