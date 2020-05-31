# 5GC build
5GC Open API build

Project contains simple Maven project which is using openapi-generator-maven-plugin. By using this project it is possible to generate 5G code from [5GC_API yaml](https://github.com/jdegre/5GC_APIs) files.

### Clone source code
```bash
git clone --recurse-submodules https://github.com/H21lab/5GC_build.git
```

## License
Licensed under the Apache License, Version 2.0

## Build Instructions
Open `5GC_code_generator` in netbeans or in other editor.

Edit the pom.xml to control which yaml files should be used for code generator and define the type of OpenAPI generator to be used. Additionally specify the `modelPackage`, `apiPackage`, `invokerPackage`. This is useful if multiple yaml files are generated in the same time to separate the generated code by namespaces.

Build the project using IDE or run `mvn clean install` in `5GC_code_generator` folder.

The OpenAPI generators will generate the code in `./target/generated-sources`.

NOTE: The code is using the latest openapi-generator-maven-plugin in version 5.0.0-SNAPSHOT. If this is not downloaded automatically, download the source code <https://github.com/OpenAPITools/openapi-generator/tree/master/modules/openapi-generator-maven-plugin> and build it before in IDE or run `mvn clean install` to install the project.

## Examples

You can run simple generate python client and server in this project in the following way:
```
cd Examples
bash run_python_server.sh &
bash run_python_client.sh
```
By capturing on localhost http communication can be captured between the client and server.
Please note, that the sample python server code has been modified to fix the generator issue (reported here <https://github.com/OpenAPITools/openapi-generator/issues/6483>).

## Limitations

There are several limitations in existing OpenAPI generators. You can experience that the generated code could not be generated or compiled after and need to be corrected manually. In such cases open github issue at <https://github.com/OpenAPITools/openapi-generator>.


## Attribution
Created by Martin Kacer

Copyright 2020 H21 lab, All right reserved
