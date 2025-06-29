'''
from flask import Flask, Response
import psutil
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Prometheus metrics
cpu_usage_gauge = Gauge('cpu_usage', 'CPU usage percentage')
memory_usage_gauge = Gauge('memory_usage', 'Memory usage percentage')

@app.route("/")
def index():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    return f"<h2>Welcome to AutoDeploy App 🚀</h2><p>CPU: {cpu}% | Memory: {memory}%</p>"

@app.route("/metrics")
def metrics():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    cpu_usage_gauge.set(cpu)
    memory_usage_gauge.set(memory)

    data = generate_latest()
    return Response(data, mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
'''

from flask import Flask, Response
import psutil
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Prometheus metrics
cpu_usage_gauge = Gauge('cpu_usage', 'CPU usage percentage')
memory_usage_gauge = Gauge('memory_usage', 'Memory usage percentage')
disk_usage_gauge = Gauge('disk_usage', 'Disk usage percentage')
net_sent_gauge = Gauge('net_sent_bytes', 'Network bytes sent')
net_recv_gauge = Gauge('net_recv_bytes', 'Network bytes received')

@app.route("/")
def index():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    net = psutil.net_io_counters()
    return (
        f"<h2>Welcome to AutoDeploy App 🚀</h2>"
        f"<p>CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%</p>"
        f"<p>Net Sent: {net.bytes_sent} bytes | Net Recv: {net.bytes_recv} bytes</p>"
    )

@app.route("/metrics")
def metrics():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    net = psutil.net_io_counters()

    # Update Prometheus metrics
    cpu_usage_gauge.set(cpu)
    memory_usage_gauge.set(memory)
    disk_usage_gauge.set(disk)
    net_sent_gauge.set(net.bytes_sent)
    net_recv_gauge.set(net.bytes_recv)

    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
