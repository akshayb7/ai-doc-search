from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool

llm = LLM(model="azure/gpt-4o", api_version="2024-08-01-preview")


@CrewBase
class AiSearchDoc:
    """AiSearchDoc crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def support_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["support_agent"],
            allow_delegation=False,
            llm=llm,
            tools=[ScrapeWebsiteTool()],
            verbose=True,
        )

    @agent
    def support_quality_assurance_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["support_quality_assurance_agent"],
            allow_delegation=True,
            llm=llm,
            verbose=True,
        )

    @task
    def inquiry_resolution(self) -> Task:
        return Task(
            config=self.tasks_config["inquiry_resolution"],
        )

    @task
    def quality_assurance_review(self) -> Task:
        return Task(
            config=self.tasks_config["quality_assurance_review"],
            output_file="result.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AiSearchDoc crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            memory=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
