"""
If "modified" date/time is not defined in article metadata, fall back to the "created" date.
"""
from datetime import datetime

from pelican import signals
from pelican.contents import Content, Article

# NOTE: pelican make the lower()
class STATUS:
    PUBLISHED = 'published'
    DRAFT = 'draft'
    READY = 'ready'


def hook_publishing(article):
    
    if not isinstance(article, Article):
        return
    
    # DEBUG:
    #print('Keys: %s' % list(article.__dict__.keys()))
    #print('Article: %s status=%s(%s)  date=%s   date_format=%s  ' % (article.slug, article._status,type(article._status), article.locale_date, article.date_format))

    # status=published(<class 'str'>)
    # date=Aug 26, 2009
    # date_format=%b %d, %Y
    # We want to push as published if  ready+date is ok
    # NOTE: already publised: manually set, or old articles
    article_date = datetime.strptime(article.locale_date, article.date_format)

    
    if article._status == STATUS.READY:
        now = datetime.now()
        # Maybe the time is ok
        if now >= article_date:
            article._status = STATUS.PUBLISHED
        else:  # not ready, we can go in draft
            print(' * %-40s : not ready yet: %s' % (article, article_date))
            article._status = STATUS.DRAFT
    
    #if not article.settings.get('ALWAYS_MODIFIED', False):
    #    return
    

def register():
    signals.content_object_init.connect(hook_publishing)