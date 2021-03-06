from django.db import models

    
class List_of_regedit_buy(models.Model):
    TAGS_CHOICES = (
        ('ПО', 'ПО'),
        ('ПНР и ШМР', 'ПНР и ШМР'),
        ('СХД', 'СХД'),
        ('server', 'Серверное оборудование'),
        ('network', 'Сетевое оборудование'),
        ('support', 'Техническая поддержка'),
        ('ibp', 'ИБП'),
        ('consulting', 'Консалтинг')
        )
    date_of_completion = models.IntegerField("Год договора", blank=True)
    onec_code = models.CharField("Код в 1С", max_length=50, blank=True)
    name_of_buyer = models.TextField("Наименование покупателя", blank=True)
    theme_of_contract = models.TextField("Предмет договора", blank=True)
    number = models.TextField("Номер", blank=True)
    date_of_contract = models.TextField("Дата Договора", blank=True)
    expiration = models.TextField("Срок действия договора", blank=True)
    total = models.TextField("Сумма договора", blank=True)
    comments = models.TextField("Комментарии", blank=True)
    technical = models.TextField("ТехОписание", blank=True)
    #tags = models.TextField("Теги", blank=True)
    tags = models.CharField(
        max_length=1,
        choices=TAGS_CHOICES,
    )
    status = models.TextField("Статус", blank=True)
    subcontractor = models.TextField("Подрядчик", blank=True)
    check_number = models.TextField("№ договора с подрядчиком", blank=True)
