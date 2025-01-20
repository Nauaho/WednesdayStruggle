# WednesdayStruggle
Życie jest cierpeniem... I nie pomożemy z tym.

## Wstęp
Cel projektu a. Celem projektu jest predykcja stanu zdrowia psychicznego użytkownika (grupa docelowa – studenci) na podstawie kwestionariuszy.
## Baza danych 
https://www.kaggle.com/datasets/mohsenzergani/bangladeshi-university-students-mental-health

## Jak uruchomić
Do uruchomienia lokalnie aplikacji niezbędny jest python w wersji 3.11 i biblioteki ```autogluon.tabular``` w wersji 1.1.1 oraz ```streamlit```, instalowane poleceniem 
````
pip3 install -r requirements.txt
````


Po ich zainstalowaniu wystarczy wykonać polecenie
````
streamlit run user_gui.py
```` 
które uruchomi interfejs użytkownika.

Aplikacja będzie dostępna pod adresem http://localhost:8501/
