import eel
eel.init('web')
options = {
    'host': '192.168.122.230',
    'port': 8080,
    'path':'pos/?posid=1'
    }
eel.start(options)
# eel.start('main.html', size=(650, 612))


# my_options = {
#     'mode': "chrome", #or "chrome-app",
#     'host': 'localhost',
#     'port': 8080,
#     'chromeFlags': ["--start-fullscreen", "--browser-startup-dialog"]
# }
