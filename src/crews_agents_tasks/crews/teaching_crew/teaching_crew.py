from crewai import Crew, Task, Agent, Process
from crewai.project import CrewBase, task, agent, crew  # task, agent, crew are decorators in CrewBase Class

@CrewBase
class TeachingCrew:

    @agent
    def sir_zia(self) -> Agent:
        return Agent(
            role="Sir Zia",
            goal="You are a teacher who is teacing a {topic} to a student",
            backstory="You are a teacher who is teaching a {topic} to a student",
            llm="gemini/gemini-1.5-flash",
        )
    

    @task
    def describe_topic(self) -> Task:
        return Task(
            description="Describe the {topic} in detail",
            expected_output="A detailed description of the {topic}",
            agent=self.sir_zia(),
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
