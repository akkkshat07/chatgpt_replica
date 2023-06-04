import openai

openai.api_key = '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'
model_engine = "text-davinci-003"
prompt = input("🤖 Hi! How can I help you?\n")

while prompt.lower() not in ("no", "n", "no!", "you can't", "you cant",
                             "nothing"):
  completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  )

  response = completion.choices[0].text
  print(f'🤖 {response}')

  prompt = input("🤖Anything you like to ask more about?\n")

print("🤖...")
