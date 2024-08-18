import json
import random
from datetime import datetime, timedelta

KEYWORDS = ['AI', 'blockchain', 'big data', 'machine learning', 'data science', 'cloud computing',
    'cybersecurity', 'IoT', '5G', 'quantum computing', 'virtual reality', 'augmented reality',
    'automated systems', 'natural language processing', 'robotics', 'smart devices', 'digital marketing',
    'e-commerce', 'fintech', 'health tech', 'edtech', 'supply chain management', 'logistics',
    'artificial intelligence', 'deep learning', 'predictive analytics', 'edge computing', 'bioinformatics',
    'digital transformation', 'enterprise software', 'internet security', 'regtech', 'telemedicine',
    'privacy', 'machine vision', 'deepfake detection', 'generative models', 'AI ethics', 'blockchain scalability',
    'smart contracts', 'cryptocurrency', 'financial modeling', 'investment analytics', 'telecommunications',
    'user experience design', 'personalization', 'data mining', 'software architecture', 'agile methodologies',
    'strategy', 'innovation']

TOPICS = ['customer experience', 'market trends', 'product development', 'operational efficiency',
    'risk management', 'data privacy', 'technology adoption', 'strategic planning', 'innovation',
    'team collaboration', 'financial performance', 'competitive analysis', 'user engagement',
    'sustainability', 'scalability', 'cost reduction', 'productivity improvement',
    'regulatory compliance', 'digital strategy', 'user interface design', 'supply chain optimization',
    'digital payment systems', 'global market expansion', 'business intelligence', 'real-time data analysis',
    'ethical AI practices', 'cyber threat detection', 'customer retention strategies', 'innovation management',
    'cloud migration', 'data governance', 'industry regulations', 'remote work efficiency']

JOB_TITLES = ['Data Scientist', 'Blockchain Developer', 'AI Researcher', 'Cybersecurity Analyst', 'Cloud Engineer',
    'Product Manager', 'Business Analyst', 'Software Engineer', 'UX/UI Designer', 'Systems Architect',
    'Digital Marketer', 'Project Manager', 'Operations Manager', 'Financial Analyst', 'Tech Lead',
    'Consultant', 'Strategy Advisor', 'Innovation Specialist', 'Research Scientist', 'Technical Writer',
    'DevOps Engineer', 'Systems Administrator', 'Product Designer', 'Technical Project Manager',
    'Data Engineer', 'Growth Hacker', 'Customer Success Manager', 'Compliance Officer', 'Ethical Hacker',
    'Sales Engineer', 'Artificial Intelligence Engineer', 'Machine Learning Engineer', 'Big Data Engineer',
    'Data Privacy Officer', 'Risk Analyst', 'Business Development Manager', 'Marketing Strategist',
    'CRM Specialist', 'Healthcare IT Specialist', 'E-commerce Specialist']

QUESTION_TEMPLATES = ["How does Sam utilize {keyword1} and {keyword2} to enhance {topic} in his role as a {job_title}?",
    "What methods does Sam use with {keyword1} and {keyword2} to improve {topic} as a {job_title}?",
    "In what ways does Sam apply {keyword1} and {keyword2} to address {topic} in his position as a {job_title}?",
    "How does Sam integrate {keyword1} and {keyword2} into {topic} as a {job_title}?",
    "What impact does Sam's expertise in {keyword1} and {keyword2} have on {topic} in his role as a {job_title}?",
    "How does Sam leverage {keyword1} and {keyword2} for {topic} in his position as a {job_title}?",
    "What innovative strategies does Sam employ with {keyword1} and {keyword2} to advance {topic} as a {job_title}?",
    "In which areas does Sam's use of {keyword1} and {keyword2} lead to improvements in {topic} as a {job_title}?",
    "How does Sam's integration of {keyword1} and {keyword2} impact {topic} in his role as a {job_title}?",
    "What role do {keyword1} and {keyword2} play in enhancing {topic} for Sam as a {job_title}?",
    "Sam leverages {keyword1} and {keyword2} to improve {topic} in his role as a {job_title}. How does this contribute to his success?",
    "Sam works with {keyword1} and {keyword2} to address {topic} as a {job_title}. What results does this achieve?",
    "How does Sam's use of {keyword1} and {keyword2} in {topic} as a {job_title} align with his objectives?",
    "What strategies does Sam employ with {keyword1} and {keyword2} to achieve success in {topic} as a {job_title}?",
    "In his role as a {job_title}, Sam uses {keyword1} and {keyword2} to address {topic}. How does this impact his work?",
    "What benefits does Sam derive from using {keyword1} and {keyword2} in his work on {topic} as a {job_title}?",
    "How does Sam's approach to {topic} as a {job_title} involve {keyword1} and {keyword2}?",
    "What outcomes result from Sam's use of {keyword1} and {keyword2} in his work on {topic} as a {job_title}?",
    "How does Sam's expertise in {keyword1} and {keyword2} contribute to his success in {topic} as a {job_title}?",]

ANSWER_TEMPLATES = ["Sam leverages {keyword1} and {keyword2} to improve {topic} as a {job_title} by implementing {solution}. This approach yields {benefit}, enhancing {aspect} and contributing to {overall_goal}.",
    "As a {job_title}, Sam uses {keyword1} and {keyword2} to tackle {topic} through {solution}. This strategy leads to {benefit} and {positive_outcome}, addressing {issue} and achieving {overall_goal}.",
    "In his role as a {job_title}, Sam applies {keyword1} and {keyword2} to {topic} by {strategy}. This results in {benefit}, {positive_outcome}, and resolves {problem}, aligning with {overall_goal}.",
    "Sam integrates {keyword1} and {keyword2} into his work on {topic} as a {job_title} by {solution}. This approach enhances {aspect}, leading to {benefit} and supporting {overall_goal}.",
    "By using {keyword1} and {keyword2}, Sam addresses {topic} as a {job_title} through {strategy}. This results in {benefit} and {positive_outcome}, improving {aspect} and contributing to {overall_goal}.",
    "Sam effectively utilizes {keyword1} and {keyword2} to advance {topic} as a {job_title} by applying {solution}. This results in {benefit}, enhances {aspect}, and supports {overall_goal}.",
    "In his role as a {job_title}, Sam employs {keyword1} and {keyword2} to improve {topic} through {strategy}. This approach yields {benefit}, leads to {positive_outcome}, and resolves {issue}.",
    "Sam's use of {keyword1} and {keyword2} in {topic} as a {job_title} involves {solution}, which results in {benefit}, enhances {aspect}, and contributes to achieving {overall_goal}.",
    "By integrating {keyword1} and {keyword2} into his work on {topic}, Sam as a {job_title} addresses {problem} through {strategy}, achieving {benefit} and {positive_outcome}.",
    "Sam's application of {keyword1} and {keyword2} to {topic} in his role as a {job_title} leads to {benefit}, resolves {issue}, and supports {overall_goal} through {solution}.",
    "As a {job_title}, Sam leverages {keyword1} and {keyword2} to enhance {topic} by implementing {solution}. This approach yields {benefit}, enhancing {aspect} and contributing to {overall_goal}.",
    "Sam uses {keyword1} and {keyword2} to tackle {topic} as a {job_title} through {solution}. This strategy leads to {benefit} and {positive_outcome}, addressing {issue} and achieving {overall_goal}.",
    "In his role as a {job_title}, Sam applies {keyword1} and {keyword2} to {topic} by {strategy}. This results in {benefit}, {positive_outcome}, and resolves {problem}, aligning with {overall_goal}.",
    "working as a {job_title}, Sam integrates {keyword1} and {keyword2} into his work on {topic} by {solution}. This approach enhances {aspect}, leading to {benefit} and supporting {overall_goal}.",
    "it is through {keyword1} and {keyword2} that Sam addresses {topic} as a {job_title} through {strategy}. This results in {benefit} and {positive_outcome}, improving {aspect} and contributing to {overall_goal}.",
    "IT is effectively utilizing {keyword1} and {keyword2} to advance {topic} as a {job_title} by applying {solution}. This results in {benefit}, enhances {aspect}, and supports {overall_goal}.",
    "work as a {job_title}, Sam employs {keyword1} and {keyword2} to improve {topic} through {strategy}. This approach yields {benefit}, leads to {positive_outcome}, and resolves {issue}.",
    "employing {keyword1} and {keyword2} in {topic} as a {job_title} involves {solution}, which results in {benefit}, enhances {aspect}, and contributes to achieving {overall_goal}.",
    "holding the position of a {job_title}, Sam integrates {keyword1} and {keyword2} into his work on {topic}, addressing {problem} through {strategy}, achieving {benefit} and {positive_outcome}.",
    "knowing {keyword1} and {keyword2} in his role as a {job_title} leads to {benefit}, resolves {issue}, and supports {overall_goal} through {solution}."
    "What impact does Sam's use of {keyword1} and {keyword2} have on his work in {topic} as a {job_title}?"]

def generate_entry(index):
    keyword1, keyword2 = random.sample(KEYWORDS, 2)
    topic = random.choice(TOPICS)
    job_title = random.choice(JOB_TITLES)
    benefit = random.choice(['increased productivity', 'enhanced user satisfaction', 'reduced costs'])
    issue = random.choice(['technical challenges', 'resource constraints'])
    solution = random.choice(['innovative solutions', 'best practices'])
    positive_outcome = random.choice(['successful outcomes', 'optimized outcomes'])
    aspect = random.choice(['team efficiency', 'project outcomes'])
    overall_goal = random.choice(['strategic growth', 'operational success'])
    strategy = random.choice(['adopting new technologies', 'improving processes'])
    problem = random.choice(['inefficiencies', 'bottlenecks'])

    question = random.choice(QUESTION_TEMPLATES).format(
        keyword1=keyword1,
        keyword2=keyword2,
        topic=topic,
        job_title=job_title
    )

    answer = random.choice(ANSWER_TEMPLATES).format(
        keyword1=keyword1,
        keyword2=keyword2,
        topic=topic,
        job_title=job_title,
        solution=solution,
        benefit=benefit,
        positive_outcome=positive_outcome,
        issue=issue,
        aspect=aspect,
        overall_goal=overall_goal,
        strategy=strategy,
        problem=problem
    )

    timestamp = (datetime(2024, 1, 1) + timedelta(days=index)).isoformat()
    return {
        "content": f"Question: {question} Answer: {answer}",
        "meta": {
            "timestamp": timestamp
        }
    }

def generate_entries(num_entries):
    return [generate_entry(i) for i in range(num_entries)]

def main():
    num_entries = "amount"
    entries = generate_entries(num_entries)
    with open('yourname.json', 'w') as file:
        json.dump(entries, file, indent=4)

if __name__ == "__main__":
    main()
