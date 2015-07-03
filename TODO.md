


tutum/influxdb:0.8.8
-e SSL_SUPPORT="True" -e SSL_CERT="`awk 1 ORS='\\n' ~/cert.pem`"


https://devops.profitbricks.com/tutorials/creating-a-grafana-and-influxdb-docker-container/

OPS NOTES

Collection
- Collectd
  Has output to influxdb native & graphite.

- StatsD - Aggregator

- CloudWatch metrics ?
- Host metrics (CPU, disk, etc...) ? (python-diamond for example) collectd (!)

Storage
- InfluxDB 0.8
  Has a graphite and collectd plugin.
  Collectd plugin has a not grafana compatible metric naming ("/" instead of ".")
  Graphite plugin works fine.


Other options:
- Graphite
- Graphite hosted
- Librato


Visualization
- Grafana

- Librato


Alerting
- Grafana

- Librato