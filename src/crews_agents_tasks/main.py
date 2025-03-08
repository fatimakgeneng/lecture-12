from crewai.flow import Flow, start, listen
from dotenv import load_dotenv, find_dotenv # litellm is already available in crewai hence,            #  we imported api keys from .env
from litellm import completion
from crews_agents_tasks.crews.teaching_crew.teaching_crew import TeachingCrew

_: bool = load_dotenv(find_dotenv()) 

class PanaFlow(Flow):

    @start()
    def generate_topic(self):
        response= completion(
            model = "gemini/gemini-1.5-flash",
            messages=[{
                "role": "user",
                "content": "Share the most trendng topic title for 2025 in AI world. Only share the title, no other text."
            }],
        ) 
        self.state['topic'] = response['choices'][0]['message']['content']
        print(f"STEP 1 Topic: {self.state['topic']}")

    @listen("generate_topic")
    def generate_content(self):
        print("STEP 2: GENERATE CONTENT\n")
        result = TeachingCrew().crew().kickoff(
            inputs = {
                "topic": self.state['topic']
            }
            )
        print(result)
  
    

def kickoff():
    flow = PanaFlow()
    flow.kickoff()
 
