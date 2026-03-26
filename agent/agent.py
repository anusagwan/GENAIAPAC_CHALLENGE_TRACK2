from agent.tools import WeatherTool

# Initialize tool
weather_tool = WeatherTool()

def run_agent(query: str):
    if "weather" in query.lower():
        city = query.lower().replace("weather in", "").strip()

        # MCP-style tool call
        tool_data = weather_tool.run(city)

        if "error" in tool_data:
            return "⚠️ Unable to fetch weather. Please check city name or try again."

        # ADK-style response generation
        return f"""
        🌦️ Weather Report

        City: {tool_data['city']}
        Temperature: {tool_data['temperature']}°C
        Condition: {tool_data['description']}
        """

    return "Ask something like: weather in Pune"