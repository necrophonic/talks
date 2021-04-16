#/bin/sh

pushd python > /dev/null
pipenv run python hello.py
popd > /dev/null

pushd go > /dev/null
go run main.go
popd > /dev/null
