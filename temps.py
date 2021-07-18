import subprocess
import rumps

class CpuTemperatureApp(object):
    def __init__(self):
        self.config = {
            "app_name": "CPU Temperature Display"
        }
        self.app = rumps.App(self.config["app_name"])
        self.timer = rumps.Timer(self.on_tick, 10)

    def on_tick(self, sender):
        # use lavoiesl/osx-cpu-temp in subprocess
        cpu_temp = "🌡️ " + subprocess.check_output("./osx-cpu-temp").decode(encoding='utf-8').strip().replace("°C", " °C")
        self.app.title = cpu_temp

    def run(self):
        self.timer.start()
        self.app.run()

if __name__ == '__main__':
    app = CpuTemperatureApp()
    app.run()
