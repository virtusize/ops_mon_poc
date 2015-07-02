


tutum/influxdb:0.8.8
-e SSL_SUPPORT="True" -e SSL_CERT="`awk 1 ORS='\\n' ~/cert.pem`"


https://devops.profitbricks.com/tutorials/creating-a-grafana-and-influxdb-docker-container/

OPS NOTES

Collection
- StatsD - Aggregator

- CloudWatch metrics ?
- Host metrics (CPU, disk, etc...) ? (python-diamond for example) collectd (!)

Storage
- InfluxDB 0.8

- Graphite
- Graphite hosted
- Librato


Visualization
- Grafana

- Librato


Alerting
- Grafana

- Librato