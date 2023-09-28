from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed successfully!')
    return HttpResponse('<h1>Welcome!</h1>\n'
                        '<p>This is my first Django website</p>')


def about(request):
    logger.info('About page accessed successfully!')
    return HttpResponse('<h1>About</h1>\n'
                        '<p>Sorry I didn\'t find anything to share :)  </p>')
