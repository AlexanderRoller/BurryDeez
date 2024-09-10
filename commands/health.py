import psutil
import time
import datetime

def get_server_status():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    uptime_seconds = time.time() - psutil.boot_time()
    uptime = str(datetime.timedelta(seconds=int(uptime_seconds)))
    disk_usage = psutil.disk_usage('/').percent  # Check main partition

    # Reading CPU temperature
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as temp_file:
            cpu_temp = int(temp_file.read()) / 1000  # Raspberry Pi reports temp in thousandths of degrees
    except FileNotFoundError:
        cpu_temp = "Unavailable"

    response = (
        f"🌐 **Server Health Status** 🌐\n"
        f"🔧 **CPU Usage:** {cpu_usage}%\n"
        f"💾 **Memory Usage:** {memory_usage}%\n"
        f"💽 **Disk Usage:** {disk_usage}%\n"
        f"🔥 **CPU Temperature:** {cpu_temp}°C\n"
        f"⏳ **Uptime:** {uptime}\n"
        f"Keep your server running smoothly! 🚀"
    )
    
    return response
