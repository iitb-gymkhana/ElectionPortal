#!/bin/bash
cd ElectionPortal;
cp settings_config.sample.py settings_config.py;
cd ..;
mkdir logs;
touch election_view.log;

echo "auto migrating in 3 seconds.";
echo "Press ctrl+C to stop the migrations";
sleep 3;
python manage.py migrate;

echo "collecting static files in 3 seconds.";
echo "Press ctrl+C to stop";
sleep 3;
python manage.py collectstatic;

echo "Starting the server in 3 seconds";
echo "Press ctrl+C to stop";
echo "Use 'python manage.py runserver' directly from now";
sleep 3;
python manage.py runserver;