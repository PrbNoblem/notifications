from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appind
from gi.repository import Notify as notify
import signal

APPINDICATOR_ID = 'testindicator'

def main():
	ind = appind.Indicator.new(APPINDICATOR_ID, 'test-test',
	appind.IndicatorCategory.SYSTEM_SERVICES)
	ind.set_status(appind.IndicatorStatus.ACTIVE)
	ind.set_menu(gtk.Menu())
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	gtk.main()



if __name__ == "__main__":
	main()
