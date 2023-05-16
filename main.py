import openai
import os
from dotenv import load_dotenv

API_KEY =  os.getenv("OPENAI_API")

load_dotenv()
openai.api_key = API_KEY


def generate_header(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2500,
        n=1,
        stop=None,
        temperature=0.7,
    )
    header = response.choices[0].text.strip()
    return header


def main():
    
    ebook_theme = input("Enter the ebook theme: ")
    tone = input("Enter the tone: ")
    num_headers = int(input("Enter the number of headers: "))

    headers = []
    excludeHeaders = []

    articleArray = []

    for i in range(num_headers):

        while True:
            prompt = f"<You will generate a header for my ebook with the theme \"5 steps to becomming a milionair\". It needs to have a tone \"Informal\". Translate everything to portuguese (BR). Exclude the following headers: \"Aprenda Finanças\">\n\n<suggested header>: Aprenda a controlar suas finanças\n\n<You will generate a header for my ebook with the theme \"5 steps to learning Digital Marketing\". It needs to have a tone \"Informal\". Translate everything to portuguese (BR). Exclude the following headers: \"Crie mensagens otimizadas\", \" Domine as belezas do marketing digital\">\n\n<suggested header>:  Conheça as ferramentas do mercado de marketing digital\n\n<You will generate a header for my ebook with the theme \"{ebook_theme}\". It needs to have a tone \"{tone}\". Translate everything to portuguese (BR). Exclude the following headers: \"{', '.join(excludeHeaders)}\">\n\n<suggested header>: \n\n"

            suggested_header = generate_header(prompt)
            print(f"Suggested header: {suggested_header}")

            user_choice = input(
                "Você quer usar este header?? (y/n): ").lower()
            
            excludeHeaders.append(suggested_header)
            if user_choice == 'y':
                headers.append(suggested_header)
                print("\n")
                break
            else:
                continue

    for i in enumerate(headers):
        
        print("Criando "+ str(i+1) +"º artigo do Ebook com o tema: " + str(headers[i]) + "...")
        prompt = f"<You will generate a article for my ebook about the following topic: {headers}. It should be in a tone: '{tone}'. It should have at least 1000 characters. Translate everything to portuguese (BR)."

        suggested_article = generate_header(prompt)

        articleArray.append(suggested_article)
        print("\n\n")

        

    article = f"{ebook_theme}\n\n"
    for i in range(len(articleArray)):
        article += f"{i+1}. {headers[i]}\n\n"
        article += f"{articleArray[i]}\n\n"
        

    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(article)
        print("Ebook gerado com sucesso!")

if __name__ == "__main__":
    main()
