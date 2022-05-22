# sphinx-carousel-bootstrap

This directory is only used when Bootstrap CSS and JS files need to be re-compiled for the project. The compiled files should
then be committed to `../sphinx_carousel/_static/`.

## Build

To build the static files run these commands (requires [Docker](https://www.docker.com/)):

```bash
docker build -t scbs .
container_id="$(docker create scbs)"
docker cp "$container_id:/dist/bootstrap-carousel.min.css" ../sphinx_carousel/_static/
docker cp "$container_id:/dist/bootstrap-carousel.min.js" ../sphinx_carousel/_static/
docker rm -v "$container_id"
```

## Pin Dependency Versions

To keep the same dependency versions used by Bootstrap's precompiled files run the below commands. You'll need to clone
https://github.com/twbs/bootstrap first (don't forget to check out the right tag version) and make sure
[jq](https://github.com/stedolan/jq) is installed.

```bash
cp /path/to/git/cloned/bootstrap/package-lock.json .
for pkg in $(jq -r '.devDependencies |keys |join(" ")' package.json); do
    ver="$(jq -r --arg pkg "$pkg" '.dependencies[$pkg].version' package-lock.json)"
    jq --arg pkg "$pkg" --arg ver "$ver" '.devDependencies[$pkg] = $ver' package.json > package.json2
    mv package.json2 package.json
done
```
