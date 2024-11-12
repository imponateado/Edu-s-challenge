import tkinter as tk
import requests
import json

def get_pokemon_info():
    pokemon_name = pokemon_entry.get().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = json.loads(response.text)
        display_pokemon_info(pokemon_data)
    else:
        pokemon_info_div.delete("1.0", tk.END)
        pokemon_info_div.insert(tk.END, "Pokémon não encontrado.")

def display_pokemon_info(pokemon_data):
    pokemon_info_div.delete("1.0", tk.END)
    
    # Exibir as informações básicas
    pokemon_info_div.insert(tk.END, f"<h2>{pokemon_data['name'].capitalize()}</h2>")
    pokemon_info_div.insert(tk.END, f"<p>ID: {pokemon_data['id']}</p>")
    pokemon_info_div.insert(tk.END, f"<p>Experiência base: {pokemon_data['base_experience']}</p>")
    pokemon_info_div.insert(tk.END, f"<p>Altura: {pokemon_data['height']} dm</p>")
    pokemon_info_div.insert(tk.END, f"<p>Peso: {pokemon_data['weight']} hg</p>")
    
    # Exibir os tipos
    pokemon_info_div.insert(tk.END, "<h3>Tipos:</h3>")
    for type_info in pokemon_data['types']:
        pokemon_info_div.insert(tk.END, f"<p>- {type_info['type']['name'].capitalize()}</p>")
    
    # Exibir as habilidades
    pokemon_info_div.insert(tk.END, "<h3>Habilidades:</h3>")
    for ability_info in pokemon_data['abilities']:
        pokemon_info_div.insert(tk.END, f"<p>- {ability_info['ability']['name'].capitalize()}</p>")
    
    pokemon_info_div.insert(tk.END, "<button onclick='show_ability_info()'>Ver Informações das Habilidades</button>")
    pokemon_info_div.insert(tk.END, "<div id='ability_info'></div>")

def show_ability_info():
    pokemon_name = pokemon_entry.get().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = json.loads(response.text)
        ability_info_div = pokemon_info_div.get_children('ability_info')[0]
        ability_info_div.delete("1.0", tk.END)
        
        for ability_info in pokemon_data['abilities']:
            ability_info_div.insert(tk.END, f"<h4>{ability_info['ability']['name'].capitalize()}</h4>")
            
            ability_url = ability_info['ability']['url']
            ability_response = requests.get(ability_url)
            if ability_response.status_code == 200:
                ability_data = json.loads(ability_response.text)
                ability_info_div.insert(tk.END, f"<p>{ability_data['effect_entries'][0]['effect']}</p>")
            else:
                ability_info_div.insert(tk.END, "Não foi possível obter informações adicionais sobre a habilidade.")
    else:
        ability_info_div = pokemon_info_div.get_children('ability_info')[0]
        ability_info_div.delete("1.0", tk.END)
        ability_info_div.insert(tk.END, "Não foi possível obter informações sobre as habilidades.")

root = tk.Tk()
root.title("Visualizador de Informações do Pokémon")

pokemon_label = tk.Label(root, text="Digite o nome do Pokémon:")
pokemon_label.pack(pady=10)

pokemon_entry = tk.Entry(root)
pokemon_entry.pack(pady=10)

search_button = tk.Button(root, text="Buscar", command=get_pokemon_info)
search_button.pack(pady=10)

pokemon_info_div = tk.Text(root, height=20, width=50, font=("Arial", 12))
pokemon_info_div.pack(pady=10)

ability_info_div = tk.Text(pokemon_info_div, height=10, width=50, font=("Arial", 10))
ability_info_div.pack(pady=10)
pokemon_info_div.window_create("end", window=ability_info_div)

root.mainloop()