#!/usr/bin/python3
import signal
import gi
import threading
import time
gi.require_version('Gtk', '3.0')
#gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, GObject
from gi.repository import AppIndicator3 as appind

import time
from threading import Thread

class worker(threading.Thread):

    def __init__(self, masterthingy):
        threading.Thread.__init__(self)
        self.masterthingy = masterthingy

    def run(self):
        print("running!")
        print(self.masterthingy.status)
        time.sleep(1)

class Indicator():
    def __init__(self):
        APPINDICATOR_ID = 'testindicator'
        ind = appind.Indicator.new(APPINDICATOR_ID, 'test-test',
	        appind.IndicatorCategory.SYSTEM_SERVICES)
        ind.set_status(appind.IndicatorStatus.ACTIVE)
        ind.set_menu(Gtk.Menu())
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        #gtk.main()
        self.status = "I am a status"
        self.worker = worker(self)
        self.worker.start()

if __name__ == "__main__":
    GObject.threads_init()
    Indicator()
    Gtk.main()