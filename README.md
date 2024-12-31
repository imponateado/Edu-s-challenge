# Pokemon API Wrapper

A Flask API that wraps the PokeAPI to provide filtered Pokemon data.

## 🚀 Features

- Pokemon stats endpoint
- Berry information endpoint
- Item category endpoint
- Filtered responses for specific data points

## 🛠️ Tech Stack

- Python
- Flask
- Requests

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/imponateado/Edu-s-challenge
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
python main.py
```

Server runs on port 1235.

## 📚 API Documentation

### GET /pokemon/get

Returns Pokemon height and weight.

```python
GET /pokemon/get?name=pikachu
```

### GET /berry/get

Returns berry growth details.

```python
GET /berry/get?name=cheri
```

### GET /item/get

Returns item category.

```python
GET /item/get?name=potion
```

## 🔒 Limitations

- Requires valid Pokemon/berry/item names
- Limited to specific data fields
- Depends on PokeAPI availability

## 📝 License

[MIT](https://choosealicense.com/licenses/mit/)
