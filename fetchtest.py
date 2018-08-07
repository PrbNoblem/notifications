
import threading
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


def printout(bus, message):
    print("Message seen")
    args = message.get_args_list()
    #print(message)

def printin(bus, message):
    print("New message!")
    args = message.get_args_list()
    #print(args[0])
    #print (message)
    #for a in args:
    #    print(a)
    #if "/signal-desktop/" in args[0]:
    #    print("New Signal Messege!")


class bus_thread(threading.Thread):

    def __init__(self, name, func, filter_string):
        threading.Thread.__init__(self)
        self.name = name
        self.loop = DBusGMainLoop()    
        self.session = dbus.SessionBus()
        self.session.add_match_string(filter_string)
        self.session.add_message_filter(func)

    def run(self):
        print("Starting {} thread...\n".format(self.name))
        #self.loop.run()
        glib.MainLoop().run()



    def printin(bus, message):
    print("New message!")
    args = message.get_args_list()
            


def printout(bus, message):
    print("Message seen")
    args = message.get_args_list()


t1 = bus_thread("incomming", printin, "type='signal',interface='ca.desrt.dconf.Writer'")
t2 = bus_thread("accepting", printout, "interface='org.freedesktop.Notifications',member='NotificationClosed'")

print("starting thread one")
t1.start()
print("startin thread two")
t2.start()

"""    
loop = DBusGMainLoop(set_as_default=True)
session_in = dbus.SessionBus()
session_out = dbus.SessionBus()

session_in.add_match_string("type='signal',interface='ca.desrt.dconf.Writer'")

session_out.add_match_string("interface='org.freedesktop.Notifications',member='NotificationClosed'")

session_in.add_message_filter(printin)

session_out.add_message_filter(printout)


glib.MainLoop().run()
"""