import webview
webview.create_window('Hello world', 'http://192.168.122.230:8080/pos/?posid=1',fullscreen=True)
# webview.create_window('Hello world', 'http://192.168.122.230:8080/pos/?posid=1')
webview.start()
