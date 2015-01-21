clean:
	rm -f db.sqlite3

create_database:
	./manage.py syncdb --noinput
	./manage.py migrate --noinput
#	./manage.py createsuperuser --username=admin --email=root@hh.com --noinput

make_fixtures:
#	./manage.py create_users
#	./manage.py create_posts
	./manage.py create_dict_items

all: clean create_database make_fixtures
