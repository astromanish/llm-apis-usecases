OPENAI_API_KEY = "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"
PERSONALITY = [
    'expert in generating python function', 
]
KNOWLEDGE_DOMAIN = [
    'python', 'pandas', 'numPy'
]
BOTS = [
    {
        'id':0,
        'personality': PERSONALITY[0],
        'conversation':[
            {
                'role':'system',
                'content': f'''you are {PERSONALITY[0]}. you know about {KNOWLEDGE_DOMAIN[0]}. you generate python code only. you use production ready functions and variables name. you write modular and manageable code.'''
            },
            {
                'role':'user',
                'content':'connect to aws s3'
            }
        ],
    }
]