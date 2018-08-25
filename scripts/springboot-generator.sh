#!/bin/bash

PROJECT_NAME='hello'

# download jar
wget -c https://repo.spring.io/release/org/springframework/boot/spring-boot-cli/2.0.4.RELEASE/spring-boot-cli-2.0.4.RELEASE-bin.zip
unzip -o spring-boot-cli-2.0.4.RELEASE-bin.zip -d springboot

cp springboot/spring*/lib/spring-boot*.jar spring-cli.jar
rm -r springboot/

wget -c https://services.gradle.org/distributions/gradle-4.9-bin.zip
unzip -o gradle-4.9-bin.zip -d gradleboot


ln -s ./gradleboot/gradle-*/bin/gradle gradle-local

echo -n "Installed: "
java -jar spring-cli.jar --version

cat << EOF > build.gradle
plugins {
	id 'org.springframework.boot' version '2.0.4.RELEASE'
	id 'java'
    id 'groovy'
}

apply plugin: 'java'
apply plugin: 'io.spring.dependency-management'


bootJar {
    baseName = '$PROJECT_NAME'
    version =  'LATEST'
}

jar {
	baseName = '$PROJECT_NAME'
	version =  '0.0.1-SNAPSHOT'
}

repositories {
	jcenter()
}

dependencies {
	compile("org.springframework.boot:spring-boot-starter-web")
    compile('org.codehaus.groovy:groovy')
	testCompile("org.springframework.boot:spring-boot-starter-test")
}
EOF

cat << EOF > app.groovy
@RestController
class ThisWillActuallyRun {

	@RequestMapping("/")
	String home() {
		"Hello World!"
	}

}
EOF

# create structure

mkdir -p src/main/java/$PROJECT_NAME
mkdir -p src/main/resources

cat << EOF > src/main/resources/application.properties
server.port=5000
EOF


cat << EOF > src/main/java/$PROJECT_NAME/HelloController.java
package hello;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

@RestController
public class HelloController {

    @RequestMapping("/")
    public String index() {
        return "Greetings from Spring Boot!";
    }

}
EOF

cat << EOF > src/main/java/$PROJECT_NAME/Application.java
package hello;

import java.util.Arrays;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    @Bean
    public CommandLineRunner commandLineRunner(ApplicationContext ctx) {
        return args -> {

            System.out.println("Let's inspect the beans provided by Spring Boot:");

            //String[] beanNames = ctx.getBeanDefinitionNames();
            //Arrays.sort(beanNames);
            //for (String beanName : beanNames) {
            //    System.out.println(beanName);
            //}

        };
    }

}
EOF

if [[ "$1" = "run" ]]; then
    echo "running: java -jar spring-cli.jar run app.groovy;"
    java -jar spring-cli.jar run app.groovy;
elif [[ "$1" = "build" ]]; then
    echo "running: gradle build --stacktrace"
    gradle build --stacktrace
elif [[ "$1" = "build-run" ]]; then
    echo "running: gradle build --stacktrace"
    #java -jar spring-cli.jar build --stacktrace
	./gradle-local build --stacktrace
	java -jar build/libs/$PROJECT_NAME-LATEST.jar;
fi  
	

