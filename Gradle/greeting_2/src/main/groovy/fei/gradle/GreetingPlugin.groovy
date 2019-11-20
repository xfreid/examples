package fei.gradle

import org.gradle.api.Project
import org.gradle.api.Plugin

/*
class GreetingPlugin implements Plugin<Project> {
    void apply(Project target) {
        target.tasks.register('hello', GreetingTask)
    }
}
*/

class GreetingPlugin implements Plugin<Project> {
   void apply(Project project) {
      project.task('hello') {
	 doLast {
            println "Hello from the GreetingPlugin"
	 }
      }
   }
}
