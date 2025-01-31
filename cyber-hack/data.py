import pandas as pd

# Sample data
data = [
    {"text": "The economic impact of climate change is increasingly severe, with rising temperatures affecting global agriculture.", "label": "Human"},
    {"text": "Recent developments in artificial intelligence have shown remarkable improvements in language understanding and generation.", "label": "AI"},
    {"text": "The government has announced new policies to combat inflation, aiming to stabilize the market within the next fiscal year.", "label": "Human"},
    {"text": "AI models continue to evolve, learning from vast datasets to produce coherent and contextually relevant text.", "label": "AI"},
    {"text": "A major breakthrough in renewable energy technology has been reported, promising significant reductions in carbon emissions.", "label": "Human"},
    {"text": "GPT-4 is now capable of generating highly sophisticated articles, surpassing previous iterations in coherence and style.", "label": "AI"},
    {"text": "New archaeological discoveries suggest that early humans developed complex societies much earlier than previously thought.", "label": "Human"},
    {"text": "AI-driven automation is transforming industries, increasing efficiency while raising ethical concerns about job displacement.", "label": "AI"}
]

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("news_ai_human.csv", index=False)

print("Sample dataset 'news_ai_human.csv' has been created.")