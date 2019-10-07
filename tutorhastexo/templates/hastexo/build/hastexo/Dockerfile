# Start from Tomcat image
FROM tomcat:8.0.53-jre8

# Environment variables
ENV CHECKOUT_DIR=/tmp/hastexo-xblock \
    BUILD_DIR=/tmp/hastexo-xblock/guacamole \
    BUILD_DEPS="git maven openjdk-8-jdk-headless" \
    RUN_DIR=/opt/hastexo-xblock \
    WAR_FILE=hastexo-xblock.war

# Build app
RUN apt-get update && \
    apt-get install -y --no-install-recommends $BUILD_DEPS && \
    git clone https://github.com/hastexo/hastexo-xblock --branch v{{ HASTEXO_XBLOCK_VERSION }} $CHECKOUT_DIR && \
    mkdir -p $RUN_DIR && \
    cp -a $BUILD_DIR/bin $RUN_DIR/ && \
    $RUN_DIR/bin/build-app.sh && \
    rm -Rf $CHECKOUT_DIR && \
    rm -Rf /var/lib/apt/lists/* && \
    apt-get purge -y --auto-remove $BUILD_DEPS

# Start hastexo-xblock under tomcat, listening on 0.0.0.0:8080
EXPOSE 8080
CMD ["/opt/hastexo-xblock/bin/start-app.sh"]
