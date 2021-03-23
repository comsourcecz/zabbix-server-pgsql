FROM zabbix/zabbix-server-pgsql:ubuntu-5.2-latest

USER root

RUN apt update \
    && apt install --no-install-recommends -y python3 python3-pysnmp4 \
    && rm -rf /var/lib/apt/lists/*

ADD discovery_juniper_rpm.py /usr/lib/zabbix/externalscripts/discovery_juniper_rpm.py

USER zabbix
