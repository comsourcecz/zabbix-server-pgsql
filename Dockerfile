FROM zabbix/zabbix-server-pgsql:ubuntu-5.2-latest AS builder

USER root

RUN apt update \
    && apt install --no-install-recommends -y python3 python3-pip \
    && pip3 install twilio pysnmp


FROM zabbix/zabbix-server-pgsql:ubuntu-5.2-latest
USER root
RUN apt update \
    && apt install -y --no-install-recommends python3 \
    && rm -rf /var/lib/apt/lists/*
COPY --from=builder /usr/local/lib/python3.8 /usr/local/lib/python3.8
ADD discovery_juniper_rpm.py /usr/lib/zabbix/externalscripts/discovery_juniper_rpm.py
ADD call.py /usr/lib/zabbix/alertscripts/call.py
USER zabbix
