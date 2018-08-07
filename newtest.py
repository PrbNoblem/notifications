import threading
import glib
import dbus
from dbus.mainloop.glib import DBusGMainLoop

def printin(bus, message):
    print("New message!")
    print(message['member'])
    print("\n\n\n")

def printout(bus, message):
    print("Message seen")
    #args = message.get_args_list()
    print(message['member'])
    print("\n\n\n")
    #print(message)

loop = DBusGMainLoop(set_as_default=True)
session = dbus.SessionBus()

proxy = session.get_object(
    "org.freedesktop.Notifications",
    "/org/freedesktop/Notifications"
)

sak = dbus.Interface(
    proxy,
    "org.freedesktop.Notifications")

proxy2 = session.get_object(
    "org.freedesktop.Notifications",
    "/org/freedesktop/Notifications"
)

sak2 = dbus.Interface(
    proxy2,
    "org.freedesktop.Notifications")

#proxy = dbus.Interface(
#    "org.freedesktop.Notifications", "/")

print(sak)

sak.connect_to_signal("NotificationClosed",
    printout)

#sak2.connect_to_signal("Notify", 
#    printin)

###########
filter_string = "type='signal',interface='ca.desrt.dconf.Writer'"
session = dbus.SessionBus()
session.add_match_string(filter_string)
session.add_message_filter(printin)
#session.add_match_string("interface='org.freedesktop.Notifications',member='NotificationClosed'")
#session.add_message_filter(printout)

glib.MainLoop().run()