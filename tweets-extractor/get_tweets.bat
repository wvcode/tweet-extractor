echo "Rodando o script..."
venv/Scripts/activate.bat
python tweet-extractor.py @sportv @cazetv --file-name tweets-copa.csv --tweets-date 2022-11-01
