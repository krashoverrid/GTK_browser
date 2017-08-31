import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,WebKit

page='http://www.google.com'

windows= Gtk.Window()
webview=WebKit.WebView()

headerbar=Gtk.HeaderBar()
headerbar.set_show_close_button(True)


def on_destroy(window):
    Gtk.main_quit()

def history(widget,data=None):
        webview.open("/history.html")

def go_back(widget, data=None):
    webview.go_back()

def go_forward(widget, data=None):
    webview.go_forward()

def refresh(widget, data=None):
    webview.reload()
    
def homepage(widget, data=None):
    webview.load_uri(page)

def update_buttons(widget, data=None):
    go_back_button.set_sensitive(webview.can_go_back())
    go_forward_button.set_sensitive(webview.can_go_forward())

go_back_button=Gtk.Button()
#go_back_arrow=Gtk.Image.new_from_icon_name("go-previus",Gtk.IconSize.SMALL_TOOLBAR)
go_back_arrow = Gtk.Image()
go_back_arrow.set_from_file("/usr/share/icons/gnome/22x22/actions/back.png")
go_back_button.add(go_back_arrow)
go_back_button.connect("clicked", go_back)

go_forward_button=Gtk.Button()
go_forward_arrow = Gtk.Image()
go_forward_arrow.set_from_file("/usr/share/icons/gnome/22x22/actions/forward.png")
go_forward_button.add(go_forward_arrow)
go_forward_button.connect("clicked", go_forward)

home_button=Gtk.Button()
home_arrow = Gtk.Image()
home_arrow.set_from_file("/usr/share/icons/gnome/22x22/actions/gtk-home.png")
home_button.add(home_arrow)
home_button.connect("clicked", homepage)

refresh_button=Gtk.Button()
refresh_arrow = Gtk.Image()
refresh_arrow.set_from_file("/usr/share/icons/gnome/22x22/actions/gtk-refresh.png")
refresh_button.add(refresh_arrow)
refresh_button.connect("clicked", refresh)

history_button=Gtk.Button()
history_arrow = Gtk.Image()
history_arrow.set_from_file("/usr/share/icons/gnome/22x22/actions/system-run.png")
history_button.add(history_arrow)
history_button.connect("clicked", history)

def on_enter(entry):
        url = entry.get_text()
        webview.open(url)

        if (url == "about:history"):
			webview.open("/history.html")
			return
        else:
            url= "http://"+url
		
        history_file = open("/history.html","a+")
        history_file.writelines("-> " + url + "<br>")
        history_file.close()
        webview.open(url)

entry=Gtk.Entry()
entry.connect("activate",on_enter)

#headerbar.set_custom_title(entry)

webview.connect("load_committed", update_buttons)

headerbar.pack_start(go_back_button)
headerbar.pack_start(go_forward_button)
headerbar.pack_start(refresh_button)
headerbar.pack_start(home_button)
headerbar.pack_start(entry)
headerbar.pack_start(history_button)

scrolled_window=Gtk.ScrolledWindow()

webview.open("https://www.facebook.com/")

scrolled_window.add(webview)
windows.add(scrolled_window)
windows.set_titlebar(headerbar)
windows.set_default_size(800,600)

windows.show_all()
windows.connect("destroy",on_destroy)
Gtk.main()
