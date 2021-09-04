from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .validators import year_validation


class User(AbstractUser):
    _USER = 'user'
    _MODERATOR = 'moderator'
    _ADMIN = 'admin'
    USER_ROLES = [
        (_USER, 'user'),
        (_MODERATOR, 'moderator'),
        (_ADMIN, 'admin'),
    ]
    username = models.CharField(
        max_length=30,
        unique=True,
        blank=True,
    )
    email = models.EmailField(
        unique=True,
    )
    confirmation_code = models.CharField(
        max_length=40,
        blank=True,
    )
    bio = models.TextField(
        blank=True,
    )
    role = models.CharField(
        max_length=10,
        choices=USER_ROLES,
        default=_USER,
    )
    password = models.CharField(
        max_length=128,
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'password',
    ]

    class Meta:
        ordering = ['email']

    @property
    def is_admin(self):
        return self.role == self._ADMIN or self.is_staff

    @property
    def is_moderator(self):
        return self.role == self._MODERATOR

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Catgory's name")
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Catgory's name"
        verbose_name_plural = "Categories' names"

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200, verbose_name="Genre's name")
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Genre's name"
        verbose_name_plural = "Genres' names"

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[year_validation],
        verbose_name="Year"
    )
    description = models.TextField(blank=True, null=True)
    genre = models.ManyToManyField(
        Genre, blank=True, related_name='titles'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        blank=True,
        related_name='titles'
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    title = models.ForeignKey(
        'Title', on_delete=models.CASCADE, related_name='reviews'
    )
    score = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(
                1, message='Please enter an integer in the range from 1 to 10'
            ),
            MaxValueValidator(
                10, message='Please enter an integer in the range from 1 to 10'
            )
        ],
    )

    class Meta:
        ordering = ['-pub_date']
        constraints = [
            models.UniqueConstraint(fields=['author', 'title'],
                                    name='unique_review')
        ]

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    review = models.ForeignKey(
        'Review', on_delete=models.CASCADE, related_name='comments'
    )

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.text
