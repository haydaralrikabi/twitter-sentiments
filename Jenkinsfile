pipeline {
 agent any
  
  stages {
   stage("prebuild") {
      steps {
        echo("pre-Building the application...")
      }
    }
    stage("build") {
      steps {
        echo("Building the application...")
      }
    }
    stage("test") {
      steps {
        echo("testing the application...")
      }
    }
    stage("deploy") {
      steps {
        echo("Deploying the application...")
      }
    }
  }
}
