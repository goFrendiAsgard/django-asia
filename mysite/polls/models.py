from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    description = models.TextField(null=True)
    pub_date = models.DateTimeField('date published')

    def __repr__(self):
        '''
        representation of question
        '''
        return '<Question id: {}, question_text: {}>'.format(self.id, self.question_text)

    def __str__(self):
        return 'id: {}, question_text: {}'.format(self.id, self.question_text)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)