# home-monitor
Home automation and monitoring service.

## How does it work?
This project uses **[Grafana](https://grafana.com/)** to visualise data that is collected through **[Prometheus](https://prometheus.io/)**. Data is scraped and exported to Prometheus from a number of optional microservices. 

Each component runs in its own Docker container making it exceptionally flexible and portable.

Everything is secured behind NGINX as a reverse proxy, with service containers using a docker network to avoid exposing services accidentally. NGINX is the only service that needs to be exposed to the internet making it very secure.
Current implementation doesn't use SSL but could easily be added. 

All of this is deployed to a host via ansible, in theory you should be able to clone the repo, set required variables and deploy to wherever you want within a few seconds.

<img
  src="/docs/images/example_dashboard.png"
  alt="Example Grafana Dashboard"
  title="Grafana Dashboard"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

## What is Monitored?

- Network Quality:
   - Download Speed
   - Upload Speed
   - Ping

- Service Host Health
   - CPU Usage
   - RAM Usage
   - Disk space remaining
   - Network Traffic In/Out

- Additional Node(s) Health/Status
   - CPU Usage
   - RAM Usage
   - Disk space remaining
   - Network Traffic In/Out

- Nearby River Levels
- Local Weather
- Local Air Quality
- Home Energy Usage

## Getting Started

NOTE: I haven't tested this outside of my own environment yet so there may be oddities that crop up.

This project is deployed using Ansible and assumes you are already familiar with setting this up.
Ensure your remote target IP has been added to your `/etc/ansible/hosts` file and that you have SSH access to this node:

```bash
sudo ansible-playbook -u <username> --private-key /path/to/id_rsa --become home-monitor/ansible/main.yaml
```