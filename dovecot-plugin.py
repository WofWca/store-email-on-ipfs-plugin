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
    directory_to_watch = './tests'
    wdd = wm.add_watch(directory_to_watch, mask, rec=True)
    print(f'Watching directory {directory_to_watch} for new email files')

    notifier.loop()