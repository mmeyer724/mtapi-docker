# mtapi-docker
Dockerized version of [MTAPI](https://github.com/jonthornton/MTAPI)

# Quick start
1. Clone this repo (**note:** the `--recursive` is *very* important!)
```
git clone --recursive git@github.com:mmeyer724/mtapi-docker.git
```
2. Build the container
```
docker build .
```
3. Run the container
```
docker run -e MTA_KEY=<YOUR API KEY> -p 8080:8080 <IMAGE ID>
```

# Configuration
All settings can be configured using environment variables, see `settings_env.py` for a full list.
