from django.db import models

class Book(models.Model):
    book_id = models.AutoField(primary_key=True, db_column='book_id')
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    section = models.CharField(max_length=50)
    year = models.IntegerField()
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    type = models.CharField(max_length=50)
    copies = models.IntegerField()
    max_days = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'books'


class Reader(models.Model):
    ticket_number = models.AutoField(primary_key=True, db_column='ticket_number')
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    course = models.IntegerField()
    group_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        db_table = 'readers'


class Issue(models.Model):
    issue_id = models.AutoField(primary_key=True, db_column='issue_id')
    issue_date = models.DateField()
    ticket_number = models.ForeignKey(
        Reader, on_delete=models.CASCADE, db_column='ticket_number'
    )
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, db_column='book_id'
    )

    def __str__(self):
        return f"Issue {self.issue_id}"

    class Meta:
        db_table = 'issues'
