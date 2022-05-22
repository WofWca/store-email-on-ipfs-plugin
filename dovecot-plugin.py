import pyinotify
from on_new_email import on_new_email
from eml_parse import get_recipiend_email_address

mask = pyinotify.IN_CREATE  # watched events

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        recipiend_email_address = get_recipiend_email_address(event.pathname)
        on_new_email(event.pathname, recipiend_email_address)

    # def process_IN_DELETE(self, event):
    #     print "Removing:", event.pathname

if __name__ == "__main__":
    wm = pyinotify.WatchManager()  # Watch Manager

    handler = EventHandler()
    notifier = pyinotify.Notifier(wm, handler)
    wdd = wm.add_watch('./tests', mask, rec=True)

    notifier.loop()