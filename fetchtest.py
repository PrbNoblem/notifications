import glib
import dbus
from dbus.mainloop.glib import DBusGMainLoop

def print_not(bus, m):
    keys = ["app_name", "replaces_id", "app_icon", "summary", "body",
        "actions",  "hints", "expire_timeout"]
    args = m.get_args_list()

    if len(args) == 8:
        n = dict( [(keys(i), args[i]) for i in range(8)])
        print("app_name: {}\nbody: {}\nhints: {}".format(
            n['app_name'], n['body'], n['hints'])) 


def printit(bus, message):
    #print("New message!")
    args = message.get_args_list()
    #print(args[0])
    #for a in args:
    #    print(a)
    if "/signal-desktop/" in args[0]:
        print("New Signal Messege!")

loop = DBusGMainLoop(set_as_default=True)
session = dbus.SessionBus()
session.add_match_string("type='signal',interface='ca.desrt.dconf.Writer',eavesdrop=true")
session.add_message_filter(printit)


glib.MainLoop().run()