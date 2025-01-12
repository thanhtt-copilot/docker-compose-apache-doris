FROM openjdk:8u342-jdk

ENV JAVA_HOME="/usr/local/openjdk-8/"
ENV PATH="/opt/apache-doris/fe/bin:$PATH"

ADD ./resource/apache-doris-2.1.7-bin-x64.tar.gz /opt/

RUN apt-get update && \
    apt-get install -y default-mysql-client && \
    apt-get clean && \
    mkdir /opt/apache-doris && \
    cd /opt && \
    mv apache-doris-2.1.7-bin-x64/fe /opt/apache-doris/

ADD ./resource/init_fe.sh /opt/apache-doris/fe/bin
RUN chmod 755 /opt/apache-doris/fe/bin/init_fe.sh

# Sửa dòng arrow_flight_sql_port trong file cấu hình
RUN sed -i 's/arrow_flight_sql_port = -1/arrow_flight_sql_port = 9090/' /opt/apache-doris/fe/conf/fe.conf

ENTRYPOINT ["/opt/apache-doris/fe/bin/init_fe.sh"]