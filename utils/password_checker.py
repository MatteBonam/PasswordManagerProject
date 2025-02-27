import hashlib
import requests
import sys

class Password_checker:
    def check_password(password):
        """
        Verifica se una password è stata compromessa secondo l'API di Have I Been Pwned.
        Utilizza il metodo k-anonimato per proteggere la privacy della password.
        
        Args:
            password (str): La password da verificare
            
        Returns:
            bool: True se la password è stata compromessa, False altrimenti
            int: Se compromessa, il numero di volte che è apparsa in violazioni
        """
        # Calcola l'hash SHA-1 della password
        sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        
        # Divide l'hash: i primi 5 caratteri vengono inviati all'API, il resto viene confrontato localmente
        prefix = sha1_password[:5]
        suffix = sha1_password[5:]
        
        # Effettua la richiesta all'API
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        headers = {
            "User-Agent": "PasswordChecker-PythonScript",
            "Accept": "application/json"
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Genera un'eccezione per HTTP error
        except requests.exceptions.RequestException as e:
            print(f"Errore durante la connessione all'API: {e}")
            return False, 0
        
        # Controlla se l'hash della password è presente nei risultati
        hashes = response.text.splitlines()
        for h in hashes:
            # Il formato della risposta è "SUFFISSO:CONTEGGIO"
            parts = h.split(':')
            if len(parts) == 2 and parts[0] == suffix:
                return True, int(parts[1])
        
        return False, 0
    
def main():
    check = input("inserire password da controllare: ")
    print(Password_checker.check_password(check))

if __name__ == "__main__":
    main()