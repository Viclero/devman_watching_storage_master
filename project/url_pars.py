import urllib.parse as urlparse


SCHEMES = {
    "postgres": "django.db.backends.postgresql",
    "postgresql": "django.db.backends.postgresql",
    "pgsql": "django.db.backends.postgresql",
    "postgis": "django.contrib.gis.db.backends.postgis",
    "mysql": "django.db.backends.mysql",
    "mysql2": "django.db.backends.mysql",
    "mysqlgis": "django.contrib.gis.db.backends.mysql",
    "mysql-connector": "mysql.connector.django",
    "mssql": "sql_server.pyodbc",
    "mssqlms": "mssql",
    "spatialite": "django.contrib.gis.db.backends.spatialite",
    "sqlite": "django.db.backends.sqlite3",
    "oracle": "django.db.backends.oracle",
    "oraclegis": "django.contrib.gis.db.backends.oracle",
    "redshift": "django_redshift_backend",
    "cockroach": "django_cockroachdb",
    "timescale": "timescale.db.backends.postgresql",
    "timescalegis": "timescale.db.backends.postgis",
}

# Register database schemes in URLs.
for key in SCHEMES.keys():
    urlparse.uses_netloc.append(key)


def get_db_settings(url):

    spliturl = urlparse.urlsplit(url)

    # Split query strings from path.
    path = spliturl.path[1:]

    # Handle postgres percent-encoded paths.
    hostname = spliturl.hostname or ""
    if "%" in hostname:
        # Switch to url.netloc to avoid lower cased paths
        hostname = spliturl.netloc
        if "@" in hostname:
            hostname = hostname.rsplit("@", 1)[1]
        # Use URL Parse library to decode % encodes
        hostname = urlparse.unquote(hostname)

    # Lookup specified engine.
    engine = SCHEMES.get(spliturl.scheme)
    if engine is None:
        raise ValueError(
            "No support for '%s'. We support: %s"
            % (spliturl.scheme, ", ".join(sorted(SCHEMES.keys())))
        )

    port = (
        str(spliturl.port)
        if spliturl.port
        and engine in (SCHEMES["oracle"], SCHEMES["mssql"], SCHEMES["mssqlms"])
        else spliturl.port
    )

    return {
        "ENGINE": engine,
        "HOST": hostname,
        "PORT": port,
        "NAME": urlparse.unquote(path or ""),
        "USER": urlparse.unquote(spliturl.username or ""),
        "PASSWORD": urlparse.unquote(spliturl.password or "")
    }
