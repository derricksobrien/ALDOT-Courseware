---
layout: default
title: "Beginner Setup: Java, Maven, Selenium, and Cucumber"
parent: AI in Software Testing
nav_order: 13
---

# Beginner Setup: Java, Maven, Selenium, and Cucumber

This guide prepares a Windows student machine for Java browser testing with Selenium and Cucumber. It is written for someone who has never used Maven, Selenium, or Cucumber before.

## What You Are Installing

- **Java JDK:** the language runtime and compiler.
- **Maven:** the build tool that downloads libraries and runs tests.
- **Selenium WebDriver:** Java libraries that control a real browser.
- **Cucumber:** a behavior-driven testing tool. It lets a test scenario be written in readable Given/When/Then steps and connected to Java code.
- **JUnit Platform:** the test platform used to discover and run the Cucumber suite.
- **A browser:** Chrome or Edge. Selenium Manager normally finds the correct driver automatically.

The flow is:

```text
Cucumber feature -> Java step definitions -> Selenium WebDriver -> browser -> test result
```

## Before You Start

Open a new PowerShell terminal in VS Code and check the tools:

```powershell
java -version
mvn -version
git --version
```

You should see Java 21 or another supported JDK, Maven 3.9 or later, and Git. You also need Chrome or Edge installed.

If Java or Maven is missing, complete the Java/Maven section in the [Lab 1.2 walkthrough](lab1.2-walkthrough.html) first. Close and reopen VS Code after installing tools so its terminals receive the updated `PATH`.

If a command is not recognized, do not continue to the Selenium steps yet. The problem is installation or `PATH`, not Selenium.

## Step 1: Install Java

Java is the language used for the test project. The JDK includes `java` for running programs and `javac` for compiling them.

In an elevated PowerShell, install Microsoft OpenJDK 21:

```powershell
winget install --id Microsoft.OpenJDK.21 --accept-package-agreements --accept-source-agreements
```

Close and reopen VS Code, then confirm:

```powershell
java -version
```

A version beginning with `21` is suitable for this guide.

## Step 2: Install Maven

Maven reads a file named `pom.xml`. That file describes the project and its dependencies. Maven downloads those dependencies into a local cache and runs the test lifecycle.

Confirm Maven:

```powershell
mvn -version
```

A tiny Maven command looks like this:

```powershell
mvn test
```

Run it from the folder that contains `pom.xml`. Running it from the wrong folder produces errors such as “There is no POM in this directory.”

## Step 3: Create the Project

Create and open a project folder:

```powershell
mkdir java-browser-testing
cd java-browser-testing
mkdir src\test\java\training\browser
mkdir src\test\resources\features
```

The important folders are:

```text
java-browser-testing/
  pom.xml
  src/
    test/
      java/
        training/browser/
      resources/
        features/
```

Maven looks for Java test code under `src/test/java` and Cucumber feature files under `src/test/resources`.

## Step 4: Create `pom.xml`

Create `pom.xml` in the project root:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>training</groupId>
    <artifactId>java-browser-testing</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.release>21</maven.compiler.release>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <junit.version>5.11.0</junit.version>
        <cucumber.version>7.18.1</cucumber.version>
        <selenium.version>4.25.0</selenium.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.seleniumhq.selenium</groupId>
            <artifactId>selenium-java</artifactId>
            <version>${selenium.version}</version>
        </dependency>
        <dependency>
            <groupId>io.cucumber</groupId>
            <artifactId>cucumber-java</artifactId>
            <version>${cucumber.version}</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>io.cucumber</groupId>
            <artifactId>cucumber-junit-platform-engine</artifactId>
            <version>${cucumber.version}</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.junit.platform</groupId>
            <artifactId>junit-platform-suite</artifactId>
            <version>${junit.version}</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.5.0</version>
            </plugin>
        </plugins>
    </build>
</project>
```

What the important dependencies do:

- `selenium-java` provides `WebDriver`, `ChromeDriver`, locators, and browser actions.
- `cucumber-java` lets Java methods implement Given/When/Then steps.
- `cucumber-junit-platform-engine` connects Cucumber to JUnit's test platform.
- `junit-platform-suite` lets one small Java class launch the feature files.

The first Maven run requires internet access so Maven can download dependencies.

## Step 5: Write a Feature File

Create `src/test/resources/features/search.feature`:

```gherkin
Feature: Visit a web page

  Scenario: Open the Selenium website
    Given I open the Selenium website
    Then the page title contains "Selenium"
```

This is Cucumber's readable specification. It is not Java code. The words `Given` and `Then` are connected to Java methods in the step-definition class.

## Step 6: Write the Step Definitions

Create `src/test/java/training/browser/BrowserSteps.java`:

```java
package training.browser;

import static org.junit.jupiter.api.Assertions.assertTrue;

import io.cucumber.java.After;
import io.cucumber.java.Before;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class BrowserSteps {
    private WebDriver browser;

    @Before
    public void startBrowser() {
        browser = new ChromeDriver();
    }

    @Given("I open the Selenium website")
    public void openSeleniumWebsite() {
        browser.get("https://www.selenium.dev/");
    }

    @Then("the page title contains {string}")
    public void checkTitle(String expectedText) {
        assertTrue(browser.getTitle().contains(expectedText));
    }

    @After
    public void stopBrowser() {
        if (browser != null) {
            browser.quit();
        }
    }
}
```

### What this code does

- `@Before` runs before each scenario and opens Chrome.
- `browser.get(...)` navigates to a URL.
- `browser.getTitle()` reads the page title.
- `assertTrue(...)` turns the observation into a test assertion.
- `@After` closes the browser even after a failure.

## Step 7: Add the Cucumber Runner

Create `src/test/java/training/browser/RunCucumberTest.java`:

```java
package training.browser;

import org.junit.platform.suite.api.ConfigurationParameter;
import org.junit.platform.suite.api.IncludeEngines;
import org.junit.platform.suite.api.SelectClasspathResource;
import org.junit.platform.suite.api.Suite;

import static io.cucumber.junit.platform.engine.Constants.GLUE_PROPERTY_NAME;

@Suite
@IncludeEngines("cucumber")
@SelectClasspathResource("features")
@ConfigurationParameter(key = GLUE_PROPERTY_NAME, value = "training.browser")
public class RunCucumberTest {
}
```

The runner tells JUnit to:

1. use the Cucumber engine;
2. find feature files in `src/test/resources/features`;
3. find step definitions in the `training.browser` package.

If the package name, feature location, or glue value is wrong, Maven may report zero scenarios or “step undefined.” Check those values first.

## Step 8: Run the Browser Test

From the folder containing `pom.xml`, run:

```powershell
mvn test
```

Expected result:

```text
BUILD SUCCESS
Tests run: 1, Failures: 0
```

Chrome should open briefly, visit the Selenium website, check the title, and close.

For a visible debugging run, temporarily remove the `@After` method or add a breakpoint, but restore automatic cleanup before committing. A test should not leave browser processes running.

## Selenium Manager: Do I Need ChromeDriver?

Modern Selenium includes **Selenium Manager**, which normally discovers and downloads the compatible browser driver automatically when you create:

```java
WebDriver browser = new ChromeDriver();
```

You usually do not need to download `chromedriver.exe` manually.

If Selenium Manager cannot work, check:

- Chrome or Edge is installed;
- the machine can reach the internet;
- the browser is not blocked by policy;
- the Java process is allowed to create child processes;
- the browser and Selenium versions are not unusually old or mismatched.

Do not commit a browser driver executable into the repository.

## Edge Instead of Chrome

If Chrome is unavailable, use Edge:

```java
import org.openqa.selenium.edge.EdgeDriver;

browser = new EdgeDriver();
```

The same Selenium Manager behavior applies. Change the dependency code and keep the feature file unchanged.

## Useful Selenium Ideas

A **locator** identifies an element on a page. For example:

```java
WebElement searchBox = browser.findElement(By.name("q"));
searchBox.sendKeys("Selenium");
```

A **wait** gives the browser time for an element to appear. Prefer explicit waits over arbitrary sleeps:

```java
WebDriverWait wait = new WebDriverWait(browser, Duration.ofSeconds(10));
WebElement button = wait.until(
    ExpectedConditions.elementToBeClickable(By.id("submit")));
button.click();
```

The page under test should be stable and owned by the class or a public training site. Avoid writing tests that depend on fragile text, changing advertisements, or personal accounts.

## Useful Cucumber Ideas

A **feature** describes a behavior.

A **scenario** is one example of that behavior.

A **step definition** is the Java method that implements a Given, When, or Then sentence.

A parameterized step can pass data from the feature into Java:

```gherkin
Scenario: Search for a product
  When I search for "Selenium"
```

```java
@When("I search for {string}")
public void searchFor(String term) {
    // Use term in the browser interaction.
}
```

Keep feature files readable. Put browser mechanics in step definitions, not in the business-language scenario.

## Common Beginner Errors

### `mvn` is not recognized

Maven is missing from `PATH`, or VS Code was not restarted after installation. Run `mvn -version` in a new terminal.

### `java` is not recognized

Install a JDK, not only a Java runtime. Reopen VS Code after installation.

### `No tests were executed`

Check that:

- the runner ends in `Test`;
- the feature is under `src/test/resources/features`;
- `@SelectClasspathResource("features")` matches that folder;
- the glue package matches the step-definition package;
- the Cucumber JUnit Platform dependency is present.

### `Step undefined`

The wording in the feature must match the annotation text in Java. These are different:

```text
Given I open the Selenium website
Given I open Selenium's website
```

Change the feature or annotation so the sentence matches exactly.

### Browser opens and closes immediately

That may be a passing test. Read the Maven result. Add a breakpoint or a temporary diagnostic message if you need to inspect the page.

### Browser driver error

Try Edge, confirm browser installation and internet access, and inspect the Selenium Manager message. Do not begin by downloading random driver versions from the internet.

### `SessionNotCreatedException`

The browser and driver could not agree on a protocol. Update the browser, update the Selenium dependency, and remove any manually configured old driver path.

## Test Hygiene and Security

- Do not put passwords, API keys, or personal account credentials in feature files.
- Use a test account or a public training page.
- Always close the browser in an `@After` hook.
- Do not commit `target/`, screenshots containing private data, browser profiles, or driver executables.
- Prefer stable locators and explicit waits.
- Keep scenarios focused on behavior and assertions, not implementation details.

Add this `.gitignore` to the project root:

```gitignore
target/
.idea/
.vscode/
*.class
screenshots/
```

## Minimum Preflight Checklist

Before class, confirm:

```powershell
java -version
mvn -version
```

Then confirm Chrome or Edge opens normally. Finally run:

```powershell
mvn -q test
```

If the test fails before opening the browser, fix Java, Maven, dependencies, or project layout first. If the browser opens but the assertion fails, the test has reached the application and is now producing useful testing evidence.
