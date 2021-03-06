# Integration Testing

I am using a TDD approach so before developing any feature I build an integration test. I use http://www.seleniumhq.org/ for the integration tests and run tests via https://codecept.io/

The test stack I am using is:
Selenium server installed on my development machine with the chrome plugin configured
codecept using the webdriver plugin

To run the tests you must:
1. Start a Standalone Selenium server. I am using the Webdriver and the server should support at least one browser
2. Start the python application (run [../app/run_app_developer.sh](../app/run_app_developer.sh) from ./app directory)
3. Start the webfrontend application (run quasar dev in the ./webfrontend directory)
4. In the integration directory run "codeceptjs run --steps"


Quick start for codecept: https://codecept.io/quickstart/
To generate a new test, go to the integrationtests directory and run
````
codeceptjs gt
````

To generate a new page object
````
codeceptjs gpo
````



