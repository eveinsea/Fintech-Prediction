#!/bin/sh

#change work directory

do_start()
{
    echo "Starting Flask Server ..."
    cd $PROJECTDIR
    $UNICORN --group ubuntu --pid $PIDFILE --bind $SOCK --daemon  wsgi:app
    echo "Done!"
}

do_stop()
{
    echo "Stopping Flask server ...."
    if [ -e "$PIDFILE" ]; then
        #kill -SIGQUIT `cat $PIDFILE`
        kill  `cat $PIDFILE`
        echo "Done!"
    fi
}

if [ "$1" = "start" ]; then
    do_start
elif [ "$1" = "stop" ]; then
    do_stop
elif [ "$1" = "restart" ]; then
    do_stop
    do_start
else
	echo "Valid commands: "
    echo "start | stop | restart"
fi

