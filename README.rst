hastexo XBlock plugin for `Tutor <https://docs.tutor.overhang.io>`_
===================================================================================

This is a plugin for `Tutor <https://docs.tutor.overhang.io>`_ that provides
the `hastexo XBlock <https://github.com/hastexo/hastexo-xblock>`_ for Open edX
platforms.

Installation
------------

To install it, run::

    pip install tutor-hastexo-xblock

Then, to enable it::

    tutor plugins enable hastexo

Make sure to add the XBlock and its requirements to
env/build/openedx/requirements/private.txt::

    # hastexo XBlock
    apscheduler>=3.5.1,<3.6
    cliff>=2.2.0,<2.3
    google-api-python-client>=1.7.7,<1.8
    keystoneauth1>=3.13.0,<3.14
    osc-lib>=1.2.0,<1.3
    os-client-config>=1.28.0,<1.29
    oslo.serialization>=2.28.1,<2.29
    oslo.utils>=3.37.1,<3.38
    paramiko>=2.1.6,<2.2
    python-heatclient>=1.6.1,<1.7
    python-keystoneclient>=3.17.0,<3.18
    python-novaclient>=7.1.2,<7.2
    -e git+https://github.com/hastexo/hastexo-xblock#egg=hastexo-xblock

    # Install a patched amqp that adds blocking socket snd/rcv timeouts that can be
    # set via BROKER_TRANSPORT_OPTIONS.
    -e git+https://github.com/arbrandes/py-amqp.git@v1.4.9hastexo#egg=amqp==1.4.9hastexo

Then rebuild the openedx image, followed by the hastexo one::

    tutor images build openedx
    totor images build hastexo

Configuration
-------------

- ``HASTEXO_XBLOCK_VERSION`` (default: ``"3.2.1"``)
- ``HASTEXO_XBLOCK_DOCKER_IMAGE`` (default: ``"hastexo/hastexo-xblock:{{ HASTEXO_XBLOCK_VERSION }}"``)
- ``HASTEXO_GUACD_DOCKER_IMAGE`` (default: ``"guacamole/guacd:0.9.13-incubating"``)
- ``HASTEXO_XBLOCK_SETTINGS`` (default: ``{}``)
- ``HASTEXO_XBLOCK_HOST`` (default: ``"hastexo-xblock.{{ LMS_HOST }}"``)
