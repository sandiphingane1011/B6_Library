






class Command(BaseCommand):
    help = 'Display'
    def handle(self, *args, **kwargs):
        title = 'new new post'
        try:
            MyModel.objects.create(
            title=title,
            mytime= '???',
        )
        print('%s added' % (title,))
    except:
        print('error')