import psutil

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
PROCESS_THRESHOLD = 100

cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent
num_processes = len(psutil.pids())

if cpu_usage > CPU_THRESHOLD:
    print("CPU usage is high! Current usage:", cpu_usage, "%")
if memory_usage > MEMORY_THRESHOLD:
    print("Memory usage is high! Current usage:", memory_usage, "%")
if disk_usage > DISK_THRESHOLD:
    print("Disk usage is high! Current usage:", disk_usage, "%")
if num_processes > PROCESS_THRESHOLD:
    print("Number of running processes is high! Current count:", num_processes)
