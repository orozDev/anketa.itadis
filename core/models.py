from django.db import models


class TimeStampMixin(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата добавление')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    class Meta:
        abstract = True


class Types_of_input(TimeStampMixin):

    class Meta:
        verbose_name = 'типы полей'
        verbose_name_plural = 'тип поля'
    
    title = models.CharField(max_length=30, verbose_name='название')
    is_selectable = models.BooleanField(verbose_name='выборычный тип', default=False)

    def __str__(self):
        return f'{self.title}'


class ItemsOfInputs(TimeStampMixin):
    
    class Meta:
        verbose_name = 'спискок'
        verbose_name_plural = 'списки пунктов'

    title = models.TextField(verbose_name='значение')

    def __str__(self):
        return f'{self.title}'


class Inputs(TimeStampMixin):

    class Meta:
        verbose_name = 'поля'
        verbose_name_plural = 'поле'

    title = models.CharField(max_length=255, verbose_name='название поли')
    type_of_input = models.ForeignKey('Types_of_input', verbose_name='тип поля', on_delete=models.PROTECT)
    items = models.ManyToManyField('ItemsOfInputs', verbose_name='значении', blank=True)
    is_required = models.BooleanField(verbose_name='обязательность для заполнение', default=False)

    def __str__(self):
        return f'{self.title}'


class Forms(TimeStampMixin):

    class Meta:
        verbose_name = 'форма'
        verbose_name_plural = 'формы'

    title = models.CharField(max_length=255, verbose_name='название формы')
    inputs = models.ManyToManyField('Inputs', verbose_name='поля')
    is_published = models.BooleanField(default=True, verbose_name='опубликовать')

    def __str__(self):
        return f'{self.title}'


class Datas(TimeStampMixin):

    class Meta:
        verbose_name = 'данный'
        verbose_name_plural = 'данные'

    name = models.CharField(verbose_name='имя формы', max_length=255)
    form = models.ForeignKey('Forms', verbose_name='форма', on_delete=models.CASCADE)
    is_checked = models.BooleanField(verbose_name='проверено', default=False)

    def __str__(self):
        return f'{self.name}'



class DetailDatas(TimeStampMixin):

    class Meta:
        verbose_name = 'детальное данный'
        verbose_name_plural = 'детальные данные'

    
    item = models.TextField(verbose_name='запись', null=True)
    data = models.ForeignKey('Datas', verbose_name='данный', on_delete=models.CASCADE)
    input_type = models.ForeignKey('Inputs', verbose_name='тип поля', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.data.name} - {self.input_type.title}'

# Create your models here.